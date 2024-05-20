from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.ID, "login-button")

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def log_in(self, username: str, password: str):
        self.fill(self.username_field, username)
        self.fill(self.password_field, password)
        self.click(self.login_button)

    def is_login_page_displayed(self):
        return self.is_displayed(self.username_field)