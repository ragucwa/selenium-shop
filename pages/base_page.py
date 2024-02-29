from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found")
            assert False, f"Element with locator {locator} not found"

    def fill(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found")
            assert False, f"Element with locator {locator} not found"

    def is_displayed(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found")
            return False

    def get_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found")
            assert False, f"Element with locator {locator} not found"

    def get_multiple_elements_text(self, locator):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return [element.text for element in elements]
        except TimeoutException:
            logging.error(f"Elements with locator {locator} not found")
            assert False, f"Elements with locator {locator} not found"

    def select_item_from_dropdown(self, locator, item_text):
        try:
            element = Select(
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(locator)
                )
            )
            element.select_by_visible_text(item_text)
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found")
            assert False, f"Element with locator {locator} not found"
