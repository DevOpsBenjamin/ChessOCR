import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient


def test_analyze(monkeypatch):
    monkeypatch.setenv("IA_SERVICE_URL", "http://ia-service:1234")
    import app.main as m
    importlib.reload(m)

    called = {}

    def fake_post(url, json):
        called["url"] = url

        class Dummy:
            def raise_for_status(self) -> None:
                pass

            def json(self) -> dict:
                return {"candidates": [{"move": "d4", "confidence": 0.9}]}

        return Dummy()

    monkeypatch.setattr(m.httpx, "post", fake_post)
    client = TestClient(m.app)
    payload = {"image": "img", "state": "fen", "legal_moves": ["e4"]}
    response = client.post("/analyze", json=payload)
    assert called["url"] == "http://ia-service:1234/analyze"
    assert response.json() == {"candidates": [{"move": "d4", "confidence": 0.9}]}

