import json
from functools import cache
from pathlib import Path
from typing import Set

from src.gateways.nike import (
    get_page,
    get_search_results,
)
from src.gateways.slack import notify_about_new_release
from src.models import (
    Config,
    NikeSearchResult,
)

saved_items: Set[NikeSearchResult] = set()


@cache
def get_config() -> Config:
    with open(Path(__file__).parent / "../config.json") as file:
        return Config(**json.loads(file.read()))


def check_saved_searches() -> None:
    for saved_search in get_config().saved_searches:
        page = get_page(saved_search)

        if not page:
            return

        search_results = get_search_results(page)

        for new_item in set(search_results) - saved_items:
            notify_about_new_release(new_item)
            saved_items.add(new_item)
