from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from pages.top_bar_page import TopBarPage
from pages.cart_page import CartPage
from pages.thank_you_page import ThankYouPage

from test_data.test_config import ITEM_NAME, FIRST_NAME, LAST_NAME, ZIP_CODE


class TestPurchaseProcess:
    def test_verify_overview_information(self, driver, login_before_tests):
        """
        Automates the purchase process on the Sauce Demo website using Selenium
        WebDriver.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        overview_page = OverviewPage(driver)

        main_page.add_item_to_cart(ITEM_NAME)
        top_bar.open_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_delivery_information(FIRST_NAME, LAST_NAME, ZIP_CODE)
        checkout_page.go_to_overview()

        assert overview_page.is_correct_item_displayed(ITEM_NAME)
        assert overview_page.is_summary_information_available()

    def test_verify_final_price(self, driver, login_before_tests):
        """
        Automates the purchase process on the Sauce Demo website using Selenium
        WebDriver.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        overview_page = OverviewPage(driver)
        main_page.add_item_to_cart(ITEM_NAME)
        top_bar.open_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_delivery_information(FIRST_NAME, LAST_NAME, ZIP_CODE)
        checkout_page.go_to_overview()

        assert overview_page.is_price_correct(price="9.99")

    def test_full_purchase_process(self, driver, login_before_tests):
        """
        Automates the purchase process on the Sauce Demo website using Selenium
        WebDriver.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        overview_page = OverviewPage(driver)
        thank_you_page = ThankYouPage(driver)

        main_page.add_item_to_cart(ITEM_NAME)
        top_bar.open_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_delivery_information(FIRST_NAME, LAST_NAME, ZIP_CODE)
        checkout_page.go_to_overview()
        overview_page.finish_purchase()

        assert thank_you_page.is_thank_you_page_displayed()
