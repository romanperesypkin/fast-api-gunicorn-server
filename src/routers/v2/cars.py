"""Cars endpoints."""
import orjson
from fastapi import APIRouter, Request, Response, Query

from src.schema.cars import Cars


router = APIRouter()


@router.get('/cars', response_model=Cars)
async def cars(
    request: Request,
    offset: int | None = Query(default=0, ge=0),  # noqa: WPS404, B008
    limit: int | None = Query(default=10, ge=1),  # noqa: WPS404, B008
) -> Response:
    """
    Cars endpoint.
    :param offset: offset
    :param limit: limit

    :return: Cars
    """
    return Response(
        content=orjson.dumps(await request.app.engine.get_cars(offset=offset, limit=limit)),
        media_type='application/json'
    )
