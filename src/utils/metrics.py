"""Metrics."""
import os

from prometheus_client import multiprocess


def on_worker_died(pid: int) -> None:
    """
    Delete prometheus client metrics files created by multiprocess mode for each process/thread.

    :param pid: pid of exited/died process
    """
    if 'prometheus_multiproc_dir' in os.environ or 'PROMETHEUS_MULTIPROC_DIR' in os.environ:
        multiprocess.mark_process_dead(pid)
