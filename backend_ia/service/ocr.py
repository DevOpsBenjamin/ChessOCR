from .model import MoveModel


class OcrPipeline:
    """Placeholder OCR processing pipeline."""

    def __init__(self, model: MoveModel):
        self.model = model

    def load_image(self, image_path: str) -> str:
        """Load image from disk (placeholder)."""
        return image_path

    def preprocess(self, image_data: str) -> str:
        """Preprocess image data (placeholder)."""
        return image_data

    def infer(self, preprocessed: str) -> str:
        """Run model inference on preprocessed data."""
        return self.model.predict(preprocessed)

    def postprocess(self, move: str) -> str:
        """Post-process model output (placeholder)."""
        return move

    def run(self, image_path: str) -> str:
        """Full OCR pipeline from image to move."""
        image = self.load_image(image_path)
        pre = self.preprocess(image)
        raw_move = self.infer(pre)
        return self.postprocess(raw_move)
