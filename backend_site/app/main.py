from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from .db import User, get_db, init_db

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


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/secure")
async def secure(username: str = Depends(get_current_username)) -> dict[str, str]:
    """An endpoint protected by basic authentication."""
    return {"hello": username}
