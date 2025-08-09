# TODO

- [x] Implement authentication in `backend_site`.
- [ ] Add OCR processing pipeline in `backend_ia`.
- [ ] Define API between `backend_site` and `backend_ia` for submitting sheet
      images, game state, and legal moves and returning candidate moves with
      confidence scores.
- [ ] Build Vue components for uploading scans and reviewing moves.
- [ ] Add database schema and migrations.
- [ ] Create Kubernetes manifests for deployment.
- [ ] Configure Kubernetes Services so `backend_site` can load balance across
      multiple `backend_ia` instances.
- [ ] Implement user game history and club sharing features.
- [ ] Add validation and retry flow in `backend_site` to handle ambiguous
      results and request human input when confidence is low.

