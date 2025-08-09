# ChessOCR

ChessOCR is an open source platform for digitizing and analyzing chess games from scanned scoresheets.

## Components

- **frontend**: Vue 3 SPA that allows users to upload scans, review OCR moves, and manage games.
- **backend_site**: FastAPI service offering authentication, REST APIs, and orchestration for OCR requests.
- **backend_ia**: Python worker service running on GPU nodes to perform OCR and chess move validation.

Each component is containerized so they can be deployed independently in Kubernetes.

## Development

See the `AGENTS.md` file for contribution and testing guidelines. This repository is in an early scaffold state; features will be added incrementally.

