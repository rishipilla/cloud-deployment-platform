from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="Cloud Deployment Platform",
    description="Production-style application used to demonstrate CI/CD and container deployment.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "cloud-deployment-platform",
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloud-deployment-platform",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "environment": "development",
    }