"""app/dependencies.py.

FastAPI Dependency Injection; anything used with the `Depends` keyword.  Shared
logic, database connections, enforced security, etc.
"""

import logging
from os import environ as ENV
from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.routes import index

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """FastAPI Lifespan Events.

    Code above the `yield` will be executed on Start-up.
    Code below the `yield` will be executed on Shutdown.

    URL: [FastAPI Lifespan Events](https://fastapi.tiangolo.com/advanced/events/#lifespan-function)
    """
    # app start-up
    logging.info('Starting Ham API app...')

    logging.info('Building database from local files...')

    logging.info('Database built...')

    logging.info('Building app routes...')
    app.include_router(index.router)

    yield
    # app shutdown
    logging.info('Shutting down Ham API app...')
