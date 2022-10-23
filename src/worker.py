#!/usr/bin/env python3

import atexit
import logging
from threading import Event

from src.releases import check_saved_searches

logger = logging.getLogger("worker")

event = Event()


def main():
    logger.info("Worker starting")

    while True:
        check_saved_searches()

        if event.wait(timeout=30 * 60):
            break


if __name__ == '__main__':
    atexit.register(lambda: event.set())
    main()
