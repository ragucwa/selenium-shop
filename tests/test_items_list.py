import allure
import pytest
from pages.main_page import MainPage
from utils.util import get_excel_data


@allure.epic("SwagLabs")
@allure.feature("Items list")
@allure.story("Main page")
@allure.parent_suite("SwagLabs")
@allure.suite("Items list")
@allure.sub_suite("Main page")
@pytest.mark.usefixtures("login_before_tests")
@pytest.mark.items_list
class TestItemsList:
    @allure.title("Test main page items display")
    @allure.description("Verifies that all items are displayed on the main page.")
    def test_available_items(self, driver):
        """
        Verifies that all items are displayed on the main page.
        """
        main_page = MainPage(driver)

        items_names = get_excel_data("test_data/items_list.xlsx")[0]

        assert main_page.are_correct_items_names_displayed(items_names)

    @allure.title("Test main page items description")
    @allure.description("Verifies that all items have a description.")
    def test_available_items_descriptions(self, driver):
        """
        Verifies that all items have a description.
        """
        main_page = MainPage(driver)

        items_data = get_excel_data("test_data/items_list.xlsx")
        with allure.step("Create a dictionary from the data"):
            items_descriptions = dict(zip(items_data[0], items_data[1]))

        assert main_page.are_correct_items_descriptions_displayed(items_descriptions)
