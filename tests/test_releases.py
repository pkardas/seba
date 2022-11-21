from unittest import mock

from src.releases import (
    check_saved_searches,
    saved_items,
)
from tests.conftest import load_example

NIKE_TN_URL = "https://www.nike.com/pl/w/mezczyzni-nik1?q=Air%20Max%20Plus"


@mock.patch("src.releases.get_page", lambda _: load_example("nike-tn-search.html"))
@mock.patch("src.releases.notify_about_new_release")
def test_check_saved_searches(notify_about_new_release):
    check_saved_searches()
    saved_items[NIKE_TN_URL].pop()
    check_saved_searches()

    assert len(saved_items[NIKE_TN_URL]) == 27
    assert notify_about_new_release.call_count == 1
