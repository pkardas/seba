from unittest import mock

from src.releases import (
    check_saved_searches,
    SAVED_ITEMS,
)
from tests.conftest import load_example


@mock.patch("src.releases.get_page", lambda _: load_example("nike-search.html"))
@mock.patch("src.releases.notify_about_new_release")
def test_check_saved_searches(notify_about_new_release):
    check_saved_searches()
    check_saved_searches()
    check_saved_searches()

    assert len(SAVED_ITEMS) == 20
    assert notify_about_new_release.call_count == 20
