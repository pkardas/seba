from typing import List

from pydantic import BaseModel


class SavedSearches(BaseModel):
    saved_searches: List[str]
