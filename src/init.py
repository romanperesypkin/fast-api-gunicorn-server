"""Fast api startup and shutdown handlers."""
import logging
from typing import Callable

from fastapi import FastAPI

from src.configs.server_config import get_config
from src.services.engine import Engine


def startup_handler(app: FastAPI) -> Callable:
    """
    Fast API startup app handler.

    :param app: Fast API app instance
    :return: Async startup app handler
    """
    async def wrapper() -> None:
        """
        Fast API async startup app handler.

        Initializes business logic classes.
        """
        app.log = logging.getLogger()
        app.log.info('Running app start handler')

        app.config = get_config()
        app.engine = Engine()
        await app.engine.start()
    return wrapper


def shutdown_handler(app: FastAPI) -> Callable:
    """
    Fast API startup app handler.

    :param app: Fast API app instance
    :return: Async startup app handler
    """
    async def wrapper() -> None:
        """
        Fast API async startup app handler.

        Initialize business logic classes.
        """
        await app.engine.stop()
        app.log.info('Running app shutdown handler')
    return wrapper
