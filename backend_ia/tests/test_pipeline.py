import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from service.model import MoveModel
from service.ocr import OcrPipeline


def test_pipeline_runs():
    pipeline = OcrPipeline(MoveModel())
    assert pipeline.run("dummy_path") == "d4"
