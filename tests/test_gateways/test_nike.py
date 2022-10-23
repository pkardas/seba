from src.gateways.nike import get_search_results
from src.models import NikeSearchResult
from tests.conftest import load_example


def test_get_search_results():
    page = load_example("nike-search.html")

    assert get_search_results(page) == [
        NikeSearchResult(name="Nike Air Max Plus", price="619,97 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-Hddz5c/DX2663-001"),
        NikeSearchResult(name="Nike Air Max Plus III", price="584,97 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-iii-3dNGrn/CD7005-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="584,97 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-7gK574/DX8962-100"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-P39sRg/DZ4507-600"),
        NikeSearchResult(name="Nike Air Max Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-CrzK8K/604133-050"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-72rq9g/DQ3977-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-NRJN5h/DZ4501-700"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-P1Fh7n/AJ2029-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-RcgCMh/DX2652-001"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-Nc2zZ7/DC6078-100"),
        NikeSearchResult(name="Nike Air Max Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-7vV0WK/DQ3983-001"),
        NikeSearchResult(name="Nike Air Max Plus III", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-iii-3BSBtx/DJ4600-001"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-sZN2jD/DR8588-400"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-KTxG6S/DX2664-001"),
        NikeSearchResult(name="Nike Air VaporMax Plus", price="999,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-vapormax-plus-Z9THdk/924453-004"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-H4CqjB/DN4590-004"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-9j8t5J/DM2573-001"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-0WBPLx/DX2653-100"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-ppK6P9/DN4587-200"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-rLd4bx/DZ4502-200")
    ]
