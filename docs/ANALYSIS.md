# Project Analysis

## Goals

ChessOCR aims to let users digitize chess games from paper scoresheets. The platform will:

1. Accept scanned images of scoresheets.
2. Perform OCR on each move while validating against chess rules.
3. Allow users to correct moves and visualize the board.
4. Store games, track usage costs, and support clubs for sharing games.

## Architecture

The system is split into three services:

- **frontend**: Vue SPA served as static assets.
- **backend_site**: FastAPI web service handling users, games, and communication with the AI service.
- **backend_ia**: Python service dedicated to OCR and chess logic, expected to run on GPU-enabled nodes.

All services will be containerized and deployed on Kubernetes. Separate Docker images (`frontend`, `backend_site`, `backend_ia`) allow independent scaling.

## Open Questions

- Which OCR engine to use (e.g., Tesseract, custom model).
- Database choice for user and game storage.
- Specific Kubernetes deployment strategy and CI/CD pipeline.

