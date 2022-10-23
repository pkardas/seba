import logging
from typing import (
    List,
    Optional,
)

import requests
from bs4 import (
    BeautifulSoup,
    Tag,
)

from src.models import NikeSearchResult

logger = logging.getLogger("nike")


def get_page(url: str) -> Optional[str]:
    try:
        return requests.get(url).text
    except Exception as e:
        logger.error(e)
        return None


def get_search_results(page: str) -> List[NikeSearchResult]:
    soup = BeautifulSoup(page, "html.parser")

    return [
        NikeSearchResult(
            name=product.find("a", class_="product-card__img-link-overlay")["aria-label"],
            price=product.find("div", class_="product-price").string.replace(' ', '').replace("\xa0", ' ').strip(),
            url=product.find("a", class_="product-card__img-link-overlay", href=True)["href"]
        )
        for product in soup.find("div", class_="product-grid__items")
        if isinstance(product, Tag)
    ]
