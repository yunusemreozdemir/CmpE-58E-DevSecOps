"""Main application entrypoint."""

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
def health_check():
    """Returns a simple health check status."""
    return {"status": "ok"}

@app.get("/demo/{code}")
def demo_vulnerability(code: str):
    """Demo endpoint - will trigger CodeQL."""
    eval(code)
    return {"executed": code}