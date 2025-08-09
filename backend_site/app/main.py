from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import httpx
import os

from .db import Club, User, get_db, init_db

app = FastAPI()
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

init_db()


def get_current_username(
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> str:
    """Validate basic auth credentials against the database."""
    user = db.query(User).filter_by(username=credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user.username


class RegisterRequest(BaseModel):
    username: str
    password: str
    referral_code: str | None = None


class RegisterResponse(BaseModel):
    username: str
    club: str | None = None


class MoveCandidate(BaseModel):
    move: str
    confidence: float


class AnalysisRequest(BaseModel):
    image: str
    state: str
    legal_moves: list[str]


class AnalysisResponse(BaseModel):
    candidates: list[MoveCandidate]


# Allow overriding the IA service URL via environment variable for different
# deployment environments. Defaults to the Docker compose service name.
IA_SERVICE_URL = os.getenv("IA_SERVICE_URL", "http://backend-ia:8000")


def call_backend_ia(data: AnalysisRequest) -> AnalysisResponse:
    url = IA_SERVICE_URL.rstrip("/") + "/analyze"
    response = httpx.post(url, json=data.dict())
    response.raise_for_status()
    return AnalysisResponse(**response.json())


@app.post("/register", response_model=RegisterResponse)
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=data.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    club = None
    if data.referral_code:
        club = db.query(Club).filter_by(referral_code=data.referral_code).first()
    user = User(
        username=data.username,
        password_hash=pwd_context.hash(data.password),
        club=club,
    )
    db.add(user)
    db.commit()
    return {"username": user.username, "club": club.name if club else None}


@app.get("/login")
def login(username: str = Depends(get_current_username)) -> dict[str, str]:
    return {"username": username}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/secure")
async def secure(username: str = Depends(get_current_username)) -> dict[str, str]:
    """An endpoint protected by basic authentication."""
    return {"hello": username}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(data: AnalysisRequest) -> AnalysisResponse:
    return call_backend_ia(data)
