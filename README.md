# ChessOCR

ChessOCR is an open source platform for digitizing and analyzing chess games from scanned scoresheets.

## Components

- **frontend**: Vue 3 SPA that allows users to upload scans, review OCR moves, and manage games.
- **backend_site**: FastAPI service offering authentication, REST APIs, and orchestration for OCR requests.
- **backend_ia**: Python worker service running on GPU nodes to perform OCR and chess move validation.

Each component is containerized so they can be deployed independently in Kubernetes.

## Service communication and scaling

`backend_site` and `backend_ia` run as separate microservices. Multiple replicas of
each component can be deployed across Kubernetes nodes. Cluster-internal
Services expose the deployments under stable DNS names, allowing
`backend_site` to call `backend_ia` while Kubernetes load balances requests to
all available IA pods.

The IA service receives a scoresheet image, the current game state, and the
list of legal moves. It responds with candidate moves and confidence scores.
`backend_site` validates these suggestions, orchestrates additional passes when
results are ambiguous, and can request human review if no suggestion meets the
required accuracy.

## Development

See the `AGENTS.md` file for contribution and testing guidelines. This repository is in an early scaffold state; features will be added incrementally.

