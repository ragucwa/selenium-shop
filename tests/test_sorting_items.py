import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("login_before_tests")
@pytest.mark.sorting_items
class TestSortingItems:
    @pytest.mark.parametrize(
        "sorting",
        [
            "Name (A to Z)",
            "Name (Z to A)",
        ],
    )
    def test_sorting_items_by_name(self, driver, sorting):
        """
        Automates the sorting items process on the Sauce Demo website using Selenium
        WebDriver.
        """
        main_page = MainPage(driver)

        main_page.sort_items(sorting)

        assert main_page.are_items_sorted_by_name(sorting)

    @pytest.mark.parametrize(
        "sorting",
        [
            "Price (low to high)",
            "Price (high to low)",
        ],
    )
    def test_sorting_items_by_price(self, driver, sorting):
        """
        Automates the sorting items process on the Sauce Demo website using Selenium
        WebDriver.
        """
        main_page = MainPage(driver)

        main_page.sort_items(sorting)

        assert main_page.are_items_sorted_by_price(sorting)
