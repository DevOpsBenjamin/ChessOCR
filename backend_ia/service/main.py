from .model import MoveModel
from .ocr import OcrPipeline

model = MoveModel()
pipeline = OcrPipeline(model)


def process_move(image_path: str) -> str:
    """Return the move predicted by the OCR pipeline."""
    return pipeline.run(image_path)


def main() -> None:
    print("backend_ia ready")


if __name__ == "__main__":
    main()
