# Cloud Infrastructure & Deployment Platform

A production-style cloud deployment platform demonstrating containerized application deployment, CI/CD automation, environment configuration, health monitoring, versioned releases, and rollback workflows.

## Architecture

```text
Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions
   │
   ├── Install Dependencies
   ├── Run Automated Tests
   └── Build Docker Image
          │
          ▼
      Render Cloud
          │
          ├── FastAPI Application
          ├── Health Check
          ├── Metrics Endpoint
          └── Version Information