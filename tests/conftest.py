from datetime import datetime
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from test_data.test_config import PASSWORD


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver_option = webdriver.ChromeOptions()
        driver_option.add_argument("--window-size=1920,1080")
        driver_option.add_argument("incognito")
        driver_option.add_argument("--headless")
        driver_option.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=driver_option)
    elif browser == "firefox":
        driver_option = webdriver.FirefoxOptions()
        driver_option.add_argument("--width=1920,height=1080")
        driver_option.add_argument("-private")
        driver_option.add_argument("-headless")
        driver = webdriver.Firefox(options=driver_option)
    else:
        raise Exception(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login_before_tests(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.log_in("standard_user", PASSWORD)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        print(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        )
        driver = item.funcargs["driver"]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        driver.save_screenshot(f"test_results/{item.name}_{timestamp}_screenshot.png")
