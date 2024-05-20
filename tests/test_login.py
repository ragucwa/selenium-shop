import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from test_data.test_config import PASSWORD


@pytest.mark.login
class TestLogin:
    @pytest.mark.parametrize(
        "login",
        [
            "standard_user",
            "problem_user",
            "performance_glitch_user",
            "error_user",
        ],
    )
    def test_standard_login(self, driver, login):
        """
        Automates the login process on the Sauce Demo website using Selenium
        WebDriver.
        """
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open_login_page()
        login_page.log_in(login, PASSWORD)

        assert main_page.is_main_page_displayed()

    @pytest.mark.parametrize(
        "login",
        ["locked_out_user"],
    )
    def test_locked_user_can_not_login(self, driver, login):
        """
        Automates the login process on the Sauce Demo website using Selenium
        WebDriver.
        """
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open_login_page()
        login_page.log_in(login, PASSWORD)

        assert not main_page.is_main_page_displayed()

    def test_logout(self, driver, login_before_tests):
        """
        Automates the logout process on the Sauce Demo website using Selenium
        WebDriver.
        """
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        main_page.logout()

        assert login_page.is_login_page_displayed()
