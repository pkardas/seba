from typing import (
    List,
    Optional,
)

import requests
from bs4 import (
    BeautifulSoup,
    Tag,
)

from src.logger import get_logger
from src.models import NikeSearchResult

logger = get_logger("nike")


def get_page(url: str) -> Optional[str]:
    try:
        return requests.get(url).text
    except Exception as e:
        logger.error(e)
        return None


def get_search_results(page: str) -> List[NikeSearchResult]:
    soup = BeautifulSoup(page, "html.parser")

    return [
        _get_product(product)
        for product in soup.find("div", class_="product-grid__items")
        if isinstance(product, Tag) and _get_product(product)
    ]


def _get_product(product: Tag) -> Optional[NikeSearchResult]:
    product_card_a = product.find("a", class_="product-card__img-link-overlay", href=True)
    product_price_div = product.find("div", class_="product-price")

    if not product_card_a or not product_price_div:
        return None

    return NikeSearchResult(
        name=product_card_a["aria-label"],
        price=product_price_div.string.replace(' ', '').replace("\xa0", ' ').strip(),
        url=product_card_a["href"],
    )
