"""API routes module."""

from fastapi import APIRouter

router = APIRouter()

@router.post("/echo")
def echo(data: dict):
    """Returns the same data sent by the user."""
    return {"you_sent": data}
