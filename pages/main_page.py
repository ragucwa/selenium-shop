import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.inventory_container = (By.ID, "inventory_container")
        self.side_menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.add_to_cart_button = (
            By.XPATH,
            "//div[contains(text(), '{}')]/ancestor::div/div/button",
        )
        self.item_description_by_name = (
            By.XPATH,
            "//div[contains(text(), '{}')]/ancestor::div[@class='inventory_item_label']/div[@class='inventory_item_desc']",
        )
        self.item_title = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.remove_from_cart_button = (By.ID, "remove-sauce-labs-bike-light")
        self.sorting_dropdown = (By.CLASS_NAME, "product_sort_container")

    def is_main_page_displayed(self):
        return self.is_displayed(self.inventory_container)

    def logout(self):
        self.click(self.side_menu_button)
        self.click(self.logout_button)

    def add_item_to_cart(self, item_name: str):
        add_to_cart_button = (
            self.add_to_cart_button[0],
            self.add_to_cart_button[1].format(item_name),
        )
        self.click(add_to_cart_button)

    def remove_item_from_cart(self):
        self.click(self.remove_from_cart_button)

    def sort_items(self, sorting: str):
        self.select_item_from_dropdown(self.sorting_dropdown, sorting)

    def are_items_sorted_by_name(self, sorting: str):
        items = self.get_multiple_elements_text(self.item_title)
        if sorting == "Name (A to Z)":
            return items == sorted(items, reverse=False)
        elif sorting == "Name (Z to A)":
            return items == sorted(items, reverse=True)
        else:
            raise ValueError(f"Sorting option {sorting} is not supported")

    def are_items_sorted_by_price(self, sorting: str):
        prices = self.get_multiple_elements_text(self.item_price)
        prices = [float(price.replace("$", "")) for price in prices]
        if sorting == "Price (low to high)":
            return prices == sorted(prices, reverse=False)
        elif sorting == "Price (high to low)":
            return prices == sorted(prices, reverse=True)
        else:
            raise ValueError(f"Sorting option {sorting} is not supported")

    @allure.step("Verify that the correct items names are displayed")
    def are_correct_items_names_displayed(self, expected_items_names: list):
        actual_items_names = self.get_multiple_elements_text(self.item_title)
        return sorted(actual_items_names) == sorted(expected_items_names)

    @allure.step("Verify that the correct items descriptions are displayed")
    def are_correct_items_descriptions_displayed(
        self, expected_items_descriptions: dict
    ):
        for item_name in expected_items_descriptions:
            item_description = self.get_text(
                (
                    self.item_description_by_name[0],
                    self.item_description_by_name[1].format(item_name),
                )
            )
            if item_description == expected_items_descriptions[item_name]:
                return False
        return True
