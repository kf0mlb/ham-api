"""app/routes/index.py.

Main API Router.
"""

from fastapi import APIRouter
from app.routes import repeaters

router = APIRouter(prefix='/v1')
router.include_router(repeaters.router)
