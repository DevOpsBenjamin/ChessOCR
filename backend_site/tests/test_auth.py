import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.db import Base, ChessGame, User, get_db  # noqa: E402
from app.main import app, pwd_context  # noqa: E402


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestingSessionLocal() as db:
        user = User(username="admin", password_hash=pwd_context.hash("secret"))
        db.add(user)
        db.add(ChessGame(owner=user, pgn="1. e4 e5"))
        db.commit()

    with TestClient(app) as c:
        c.session_maker = TestingSessionLocal
        yield c

    app.dependency_overrides.clear()


def test_auth_required(client):
    response = client.get("/secure")
    assert response.status_code == 401


def test_auth_success(client):
    response = client.get("/secure", auth=("admin", "secret"))
    assert response.json() == {"hello": "admin"}


def test_user_has_game(client):
    with client.session_maker() as db:
        user = db.query(User).filter_by(username="admin").first()
        assert user.games[0].pgn.startswith("1. e4")
