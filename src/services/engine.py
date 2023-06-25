"""Engine implementation."""
import logging

from src.services.service import Service
from src.schema.cars import Color
from src.utils.typing import CarsT


class Engine(Service):
    """Engine class querie services and call appropriate models."""

    def __init__(self):
        """Class constructor."""
        self.log = logging.getLogger()
        self.cars = [
            {
                'name': 'BMW',
                'color': Color.red,
            },
            {
                'name': 'Toyota',
                'color': Color.blue,
            },
        ]

    async def start(self) -> None:
        """Start internal service."""
        self.log.info('Engine start')

    async def stop(self) -> None:
        """Stop internal service."""
        self.log.info('Engine stop')

    async def get_cars(self, offset: int = 0, limit: int = 10) -> CarsT:
        """Get cars processor."""
        return self.cars[offset:limit]
