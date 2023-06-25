"""Cars endpoints."""
import orjson
from fastapi import APIRouter, Request, Response

from src.schema.cars import Cars


router = APIRouter()


@router.get('/cars', response_model=Cars)
async def cars(request: Request) -> Response:
    """
    Cars endpoint.

    :return: Cars
    """
    return Response(
        content=orjson.dumps(await request.app.engine.get_cars()),
        media_type='application/json'
    )
