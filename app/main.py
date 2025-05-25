"""Main application entrypoint."""

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/health")
def health_check():
    """Returns a simple health check status."""
    return {"status": "ok"}

@app.post("/unsafe")
def unsafe_endpoint(data: dict):
    """Unsafe endpoint with multiple vulnerabilities."""
    import subprocess
    import os
    command = data.get("cmd", "ls")
    os.system(command)
    eval(data.get("code", "1+1"))  
    exec(data.get("script", "pass"))  
    return {"status": "executed"}