from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils import util
from decimal import Decimal


EXPECTED_SUMMARY_ITEMS = [
    "Payment Information",
    "Shipping Information",
    "Price Total",
    "Total",
]


class OverviewPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.summary_block = (By.CLASS_NAME, "summary_info")
        self.items_price_field = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_field = (By.CLASS_NAME, "summary_tax_label")
        self.total_price_field = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

    def finish_purchase(self):
        self.click(self.finish_button)

    def is_correct_item_displayed(self, item_name: str):
        return self.get_text(self.inventory_item_name) == item_name

    def is_summary_information_available(self):
        actual_summary_text = self.get_text(self.summary_block)

        return all(item in actual_summary_text for item in EXPECTED_SUMMARY_ITEMS)

    def is_price_correct(self, price: str):
        items_price = util.extract_price_from_text(
            self.get_text(self.items_price_field)
        )
        tax = util.extract_price_from_text(self.get_text(self.tax_field))
        total_price = util.extract_price_from_text(
            self.get_text(self.total_price_field)
        )
        return all(
            [
                Decimal(items_price) + Decimal(tax) == Decimal(total_price),
                Decimal(items_price) == Decimal(price),
            ]
        )
