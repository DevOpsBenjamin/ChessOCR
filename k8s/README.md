# Kubernetes Manifests

This directory will contain Kubernetes manifests for deploying the three services:

- `frontend`
- `backend_site`
- `backend_ia`

Manifests are not yet defined. Each service will have its own Deployment and Service. The `backend_ia` deployment should target GPU-enabled nodes. Kubernetes Services will expose stable DNS names and load balance traffic across replicas. `backend_site` will call the `backend_ia` service to distribute OCR requests among available pods.
