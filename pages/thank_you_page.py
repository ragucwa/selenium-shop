from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ThankYouPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.thank_you_label = (By.CLASS_NAME, "complete-header")

    def is_thank_you_page_displayed(self):
        return self.get_text(self.thank_you_label) == "Thank you for your order!"
