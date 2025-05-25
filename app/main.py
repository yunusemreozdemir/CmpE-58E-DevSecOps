"""Main application entrypoint."""

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
github_pat = "ghp_1234567890abcdefghijklmnopqrstuvwxyz12345"
slack_webhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
password = "supersecretpassword123"

@app.get("/health")
def health_check():
    """Returns a simple health check status."""
    return {"status": "ok"}
