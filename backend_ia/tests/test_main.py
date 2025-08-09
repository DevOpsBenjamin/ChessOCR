import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient

from service.main import app, process_move


def test_process_move():
    assert process_move("dummy_path") == "d4"


def test_analyze_endpoint():
    client = TestClient(app)
    payload = {"image": "path", "state": "fen", "legal_moves": ["e4", "d4"]}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    assert response.json() == {"candidates": [{"move": "d4", "confidence": 1.0}]}
