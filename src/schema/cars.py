"""Car schemas."""
from enum import Enum, auto
from typing import Any

from pydantic import BaseModel, Field


class AutoName(Enum):
    """Auto naming for enums."""

    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> str:  # noqa: WPS120
        return name


class Color(AutoName):
    """Enum for Model typing."""

    red = auto()
    blue = auto()


class Car(BaseModel):
    """Car."""

    name: str = Field(example='Bob')
    color: Color = Field(example=Color.red)


class Cars(BaseModel):
    """Cars."""

    __root__: list[Car] = Field(
        example=[
            Car(name='BMW', color=Color.red),
            Car(name='Toyota', color=Color.blue),
        ]
    )
