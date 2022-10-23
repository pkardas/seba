import json
from functools import cache
from pathlib import Path

from src.gateways.nike import (
    get_page,
    get_search_results,
)
from src.gateways.slack import notify_about_new_release
from src.models import Config

SAVED_ITEMS = set()


@cache
def get_config() -> Config:
    with open(Path(__file__).parent / "../config.json") as file:
        return Config(**json.loads(file.read()))


def check_saved_searches():
    for saved_search in get_config().saved_searches:
        page = get_page(saved_search)

        if not page:
            return

        search_results = get_search_results(page)

        new_items = [
            item
            for item in search_results
            if item not in SAVED_ITEMS
        ]

        for new_item in new_items:
            notify_about_new_release(new_item)
            SAVED_ITEMS.add(new_item)
