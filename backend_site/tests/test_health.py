import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.main import app
from fastapi.testclient import TestClient


def test_health():
    client = TestClient(app)
    response = client.get('/health')
    assert response.json() == {'status': 'ok'}
