"""Service status endpoints."""
from fastapi import APIRouter, Request, Response
from fastapi import status as status_code
from starlette_exporter import handle_metrics
from src.configs.server_config import get_config
from datetime import datetime


router = APIRouter()


@router.get('/')
async def status() -> Response:
    """
    Status endpoint.

    :return: general info about service
    """
    return {
        'service': get_config().service,
        'time': datetime.now()
    }


@router.get('/health')
async def health() -> Response:
    """
    Health endpoint.

    :return: 200 status_code
    """
    return Response(status_code=status_code.HTTP_200_OK)


@router.get('/metrics')
async def metrics(request: Request) -> str:
    """
    Metrics endpoint.

    :param request: Fast API request instance
    :return: Metrics
    """
    return handle_metrics(request)
