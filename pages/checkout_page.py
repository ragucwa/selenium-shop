from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.continoue_button = (By.ID, "continue")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")

    def fill_delivery_information(self, first_name: str, last_name: str, zip_code: str):
        self.fill(self.first_name_field, first_name)
        self.fill(self.last_name_field, last_name)
        self.fill(self.zip_code_field, zip_code)

    def go_to_overview(self):
        self.click(self.continoue_button)
