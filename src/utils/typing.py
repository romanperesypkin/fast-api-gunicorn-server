"""Typing."""

from src.schema.cars import Color

CarsT = list[dict[str, str | Color]]
