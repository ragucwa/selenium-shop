from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class TopBarPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.open_cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.number_of_items_in_cart_field = (By.CLASS_NAME, "shopping_cart_badge")

    def number_of_items_in_cart(self):
        try:
            number_of_items = int(self.get_text(self.number_of_items_in_cart_field))
        except AssertionError:
            number_of_items = 0
        return number_of_items

    def open_cart(self):
        self.click(self.open_cart_button)
