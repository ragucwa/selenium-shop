from datetime import datetime
import time
import allure
import pytest
import requests
from selenium import webdriver

from pages.login_page import LoginPage
from test_data.test_config import PASSWORD, GRID_ADDRESS


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request, wait_for_grid):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
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
    elif browser == "firefox":
        driver_option = webdriver.FirefoxOptions()
        driver_option.add_argument("--width=1920,height=1080")
        driver_option.add_argument("-private")
        driver_option.add_argument("-headless")
        driver = webdriver.Firefox(options=driver_option)
    elif browser == "chrome_grid":
        driver_option = webdriver.ChromeOptions()
        driver_option.add_argument("--window-size=1920,1080")
        driver_option.add_argument("incognito")
        driver_option.add_argument("--disable-extensions")
        driver = webdriver.Remote(
            command_executor=f"http://{GRID_ADDRESS}:4444/wd/hub",
            options=driver_option,
        )
    elif browser == "firefox_grid":
        driver_option = webdriver.FirefoxOptions()
        driver_option.add_argument("--width=1920,height=1080")
        driver_option.add_argument("-private")
        driver_option.add_argument("-headless")
        driver = webdriver.Remote(
            command_executor="http://{GRID_ADDRESS}:4444/wd/hub",
            options=driver_option,
        )
    else:
        raise Exception(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def login_before_tests(driver, request):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.log_in("standard_user", PASSWORD)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.failed:
#         driver = item.funcargs["driver"]
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#         screenshot_name = f"{item.name}_{timestamp}_screenshot.png"
#         driver.save_screenshot(f"test_results/{screenshot_name}")
#         with open(f"test_results/{screenshot_name}", "rb") as f:
#             allure.attach(
#                 f.read(),
#                 name=screenshot_name,
#                 attachment_type=allure.attachment_type.PNG,
#             )


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
