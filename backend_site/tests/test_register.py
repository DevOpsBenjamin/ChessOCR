import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.db import Base, Club, get_db  # noqa: E402
from app.main import app  # noqa: E402


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
        club = Club(name="Club A", referral_code="abc123")
        db.add(club)
        db.commit()

    with TestClient(app) as c:
        c.session_maker = TestingSessionLocal
        yield c

    app.dependency_overrides.clear()


def test_register_with_referral(client):
    response = client.post(
        "/register",
        json={"username": "bob", "password": "pw", "referral_code": "abc123"},
    )
    assert response.status_code == 200
    assert response.json()["club"] == "Club A"

    with client.session_maker() as db:
        user_club = db.query(Club).filter_by(name="Club A").first()
        assert user_club.members[0].username == "bob"
