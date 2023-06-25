"""Logging."""
from datetime import datetime
from logging import LogRecord

from pythonjsonlogger import jsonlogger

from src.configs.server_config import get_config


class ElkJsonFormatter(jsonlogger.JsonFormatter):
    """Json log formatter for python log subsystem."""

    def add_fields(self, log_record: dict[str, str], record: LogRecord, message_dict: dict[str, str]) -> None:
        """
        Allow add custom fileds to be logged.

        :param log_record: Custom fields to be added to
        :param record: LogRecord logging contains general log data
        :param message_dict: LogRecord msg instance
        """
        super().add_fields(log_record, record, message_dict)

        log_record['@timestamp'] = datetime.now().isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['app'] = get_config().service
