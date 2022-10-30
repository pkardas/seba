from __future__ import annotations

import logging
import os

import rollbar

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s]: %(message)s")


def get_logger(name: str) -> Logger:
    return Logger(name)


class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

        rollbar.init(
            access_token=os.getenv("ROLLBAR_TOKEN"),
            environment="prod",
            code_version="1.0"
        )

    def info(self, msg) -> None:
        self.logger.info(msg)

    def warning(self, msg) -> None:
        self.logger.warning(msg)

    def error(self, msg) -> None:
        self.logger.error(msg)
        rollbar.report_message(msg, level="error")
