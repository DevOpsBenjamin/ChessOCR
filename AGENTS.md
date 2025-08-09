# Project Instructions

This repository uses multiple components:

- `frontend`: Vue 3 app with Node 18.
- `backend_site`: Python 3.11 FastAPI app exposing REST API and auth.
- `backend_ia`: Python service for OCR and chess logic.

## Conventions

- Use Unix-style line endings.
- Use 4 spaces for Python indentation and 2 spaces for JavaScript/Vue.
- Keep modules small and focused.

## Testing

Run the available checks for the component you modify:

- `frontend`: `npm test` inside the `frontend` directory.
- `backend_site`: `pytest` inside the `backend_site` directory.
- `backend_ia`: `pytest` inside the `backend_ia` directory.

Currently, tests are placeholders and always pass.

