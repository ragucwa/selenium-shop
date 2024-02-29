from pages.main_page import MainPage
from utils.util import get_excel_data


class TestItemsList:
    def test_available_items(self, driver, login_before_tests):
        """
        Verifies that all items are displayed on the main page.
        """
        main_page = MainPage(driver)

        items_names = get_excel_data("test_data/items_list.xlsx")[0]

        assert main_page.are_correct_items_names_displayed(items_names)

    def test_available_items_descriptions(self, driver, login_before_tests):
        """
        Verifies that all items have a description.
        """
        main_page = MainPage(driver)

        items_data = get_excel_data("test_data/items_list.xlsx")
        items_descriptions = dict(zip(items_data[0], items_data[1]))

        assert main_page.are_correct_items_descriptions_displayed(items_descriptions)
