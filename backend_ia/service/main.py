from fastapi import FastAPI
from pydantic import BaseModel

from .model import MoveModel
from .ocr import OcrPipeline

app = FastAPI()
model = MoveModel()
pipeline = OcrPipeline(model)


class AnalysisRequest(BaseModel):
    image: str
    state: str
    legal_moves: list[str]


class MoveCandidate(BaseModel):
    move: str
    confidence: float


class AnalysisResponse(BaseModel):
    candidates: list[MoveCandidate]


def process_move(image_path: str) -> str:
    """Return the move predicted by the OCR pipeline."""
    return pipeline.run(image_path)


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(data: AnalysisRequest) -> AnalysisResponse:
    move = process_move(data.image)
    candidate = MoveCandidate(move=move, confidence=1.0)
    return AnalysisResponse(candidates=[candidate])


def main() -> None:
    print("backend_ia ready")


if __name__ == "__main__":
    main()

