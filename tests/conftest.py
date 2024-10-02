import time
import pytest
import requests
from selenium import webdriver

from pages.login_page import LoginPage
from test_data.test_config import PASSWORD, GRID_ADDRESS


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if "local" in browser:
        driver = local_driver(browser)
    else:
        driver = remote_driver(browser)

    yield driver

    driver.quit()


def local_driver(browser):
    if browser == "chrome_local":
        driver_option = webdriver.ChromeOptions()
        driver_option.add_argument("--window-size=1920,1080")
        driver_option.add_argument("incognito")
        driver_option.add_argument("--headless")
        driver_option.add_argument("--disable-extensions")
        driver_option.add_argument("--no-sandbox")
        driver_option.add_argument("--disable-dev-shm-usage")
        driver_option.experimental_options["prefs"] = {
            "default_content_settings": {"images": 2}
        }
        driver = webdriver.Chrome(options=driver_option)
    elif browser == "firefox_local":
        driver_option = webdriver.FirefoxOptions()
        driver_option.add_argument("--width=1920,height=1080")
        driver_option.add_argument("-private")
        driver_option.add_argument("-headless")
        driver = webdriver.Firefox(options=driver_option)
    else:
        raise Exception(f"Unsupported browser: {browser}")

    return driver


def remote_driver(browser, wait_for_grid):
    if browser == "chrome":
        driver_option = webdriver.ChromeOptions()
        driver_option.add_argument("--window-size=1920,1080")
        driver_option.add_argument("incognito")
        driver_option.add_argument("--disable-extensions")
        driver = webdriver.Remote(
            command_executor=f"http://{GRID_ADDRESS}:4444/wd/hub",
            options=driver_option,
        )
    elif browser == "firefox":
        driver_option = webdriver.FirefoxOptions()
        driver_option.add_argument("--width=1920,height=1080")
        driver_option.add_argument("-private")
        driver_option.add_argument("-headless")
        driver = webdriver.Remote(
            command_executor=f"http://{GRID_ADDRESS}:4444/wd/hub",
            options=driver_option,
        )
    else:
        raise Exception(f"Unsupported browser: {browser}")

    return driver


@pytest.fixture(autouse=True)
def login_before_tests(driver, request):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.log_in("standard_user", PASSWORD)


@pytest.fixture
def wait_for_grid():
    end_time = time.time() + 30

    while time.time() < end_time:
        try:
            response = requests.get(f"http://{GRID_ADDRESS}:4444/status")
            print(response.json()["value"]["ready"])
            if response.json()["value"]["ready"]:
                print("Grid is ready!")
                return
        except requests.exceptions.RequestException:
            pass

        time.sleep(1)

    raise Exception("Timed out waiting for Grid to be ready")
