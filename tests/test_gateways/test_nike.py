from src.gateways.nike import get_search_results
from src.models import NikeSearchResult
from tests.conftest import load_example


def test_get_search_results():
    page = load_example("nike-tn-search.html")

    assert get_search_results(page) == [
        NikeSearchResult(name="Nike Air Max Plus", price="619,97 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-Hddz5c/DX2663-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-P39sRg/DZ4507-600"),
        NikeSearchResult(name="Nike Air Max Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-CrzK8K/604133-050"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-RcgCMh/DX2652-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-P1Fh7n/AJ2029-001"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-72rq9g/DQ3977-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-NRJN5h/DZ4501-700"),
        NikeSearchResult(name="Nike Air Max Plus III", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-iii-3BSBtx/DJ4600-001"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-Nc2zZ7/DC6078-002"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-sZN2jD/DR8588-400"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-9j8t5J/DM2573-001"),
        NikeSearchResult(name="Nike Air VaporMax Plus", price="999,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-vapormax-plus-Z9THdk/924453-004"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-H4CqjB/DN4590-004"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-KTxG6S/DX2664-001"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-0WBPLx/DX2653-100"),
        NikeSearchResult(name="Nike Air Max Terrascape Plus", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-terrascape-plus-ppK6P9/DN4590-100"),
        NikeSearchResult(name="Nike Air Max Plus „FFF”", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-fff-G12bXh/FB3350-400"),
        NikeSearchResult(name="Nike Air Max Plus 3 Leather", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-leather-m0Vpt4/CK6716-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="799,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-5LXG7K/DM0032-100"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-hDKsmT/DV3488-100"),
        NikeSearchResult(name="Nike Air Max Plus SE", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-se-5XWW0c/DQ8960-100"),
        NikeSearchResult(name="Nike Air Tuned Max", price="519,97 zł", url="https://www.nike.com/pl/t/buty-meskie-air-tuned-max-CM4rj5/DC9288-002"),
        NikeSearchResult(name="Nike Air Max Plus 3 Air Max Month", price="829,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-air-max-month-KC9Crq/DR8602-001"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-rLd4bx/DZ4502-200"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-N5svjS/DX8971-001"),
        NikeSearchResult(name="Nike Air Max Plus 3", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-3-bZgw6c/FB3352-001"),
        NikeSearchResult(name="Nike Air Max Plus", price="879,99 zł", url="https://www.nike.com/pl/t/buty-meskie-air-max-plus-FgcpPC/DX2665-001")
    ]
