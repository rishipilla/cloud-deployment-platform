import os
from datetime import datetime, timezone

from fastapi import FastAPI


APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")


app = FastAPI(
    title="Cloud Deployment Platform",
    description="Production-style application used to demonstrate CI/CD and container deployment.",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "service": "cloud-deployment-platform",
        "status": "running",
        "version": APP_VERSION,
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
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
        "release": "1.2.0",
    }

