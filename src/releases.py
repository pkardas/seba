import json
from collections import defaultdict
from functools import cache
from pathlib import Path
from typing import (
    Set,
    Dict,
)

from src.gateways.nike import (
    get_page,
    get_search_results,
)
from src.gateways.slack import notify_about_new_release
from src.models import (
    Config,
    NikeSearchResult,
)

saved_items: Dict[str, Set[NikeSearchResult]] = defaultdict(set)


@cache
def get_config() -> Config:
    with open(Path(__file__).parent / "../config.json") as file:
        return Config(**json.loads(file.read()))


def check_saved_searches() -> None:
    for url in get_config().saved_searches:
        check_saved_search(url)


def check_saved_search(url: str) -> None:
    if not (page := get_page(url)):
        return

    search_results = get_search_results(page)
    new_products = set(search_results) - saved_items[url]

    if not saved_items[url]:
        saved_items[url] = new_products
    else:
        for new_item in new_products:
            notify_about_new_release(new_item)
            saved_items[url].add(new_item)
