from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


class Config(BaseModel):
    saved_searches: List[str]


@dataclass
class NikeSearchResult:
    name: str
    price: str
    url: str

    def __hash__(self) -> int:
        return hash(self.url)
