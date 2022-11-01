#!/usr/bin/env python3

import atexit
from threading import Event

from src.logger import get_logger
from src.releases import check_saved_searches

logger = get_logger("worker")

event = Event()


def main():
    logger.info("Worker starting")

    while True:
        try:
            check_saved_searches()
        except Exception as e:
            logger.error(f"Worker failed: {e}")

        if event.wait(timeout=30 * 60):
            break


if __name__ == '__main__':
    atexit.register(lambda: event.set())
    main()
