"""Gunicorn config."""
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # noqa: I003
    from gunicorn.arbiter import Arbiter
    from uvicorn.workers import UvicornWorker

from src.utils.metrics import on_worker_died


def worker_exit(server: 'Arbiter', worker: 'UvicornWorker') -> None:
    """
    Gunicorn callback hook.

    Is called when worker hast exited/died.

    :param server: Gunicorn server instance
    :param worker: Worker UvicornWorker instance
    """
    on_worker_died(worker.pid)
    server.log.info(f'Worker {worker.pid} has exited')
