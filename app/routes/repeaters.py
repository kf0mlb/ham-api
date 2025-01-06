"""app/routes/repeater.py.

API Router for Repeaters.
"""

from typing import List
from fastapi import APIRouter, Depends
from app.models.repeater import Repeaters
from app.utilities import get_db

router = APIRouter(prefix='/repeaters', tags=['repeaters'])

@router.get('/', response_model=List[Repeaters],
            summary='Get a list of all repeaters.')
async def get_repeater(db: List[Repeaters] = Depends(get_db)):
    """
    # Get a list of repeaters.

    ## Returns:
    List of Repeaters: A list array of all repeaters.
    """
    return db


@router.get('/grid/{grid_id}', response_model=List[Repeaters],
            summary='Get a list of repeaters matching a specific grid square.')
async def get_repeater_grid(
    grid_id: str,
    db: List[Repeaters] = Depends(get_db)
):
    """
    # Get a list of repeaters within a specific Grid Square.

    ## Args:
    `grid_id`: any partial amount of a maidenhead, upto 6 characters. The
               more characters, the more specific the match must be.

    ## Returns:
    List of Repeaters: A list array of all repeaters.
    """
    return [r for r in db if grid_id.lower() in r.grid.lower()]
