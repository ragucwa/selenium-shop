from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.cart_item = (By.CLASS_NAME, "cart_item")
        self.remove_item_button = (By.CLASS_NAME, "cart_button")
        self.checkout_button = (By.ID, "checkout")

    def remove_item_from_cart(self):
        self.click(self.remove_item_button)

    def go_to_checkout(self):
        self.click(self.checkout_button)

    def is_item_in_the_cart(self):
        return self.is_displayed(self.cart_item)
