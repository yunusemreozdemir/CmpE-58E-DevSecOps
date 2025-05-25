"""Main application entrypoint."""

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.get("/health")
def health_check():
    """Returns a simple health check status."""
    return {"status": "ok"}
