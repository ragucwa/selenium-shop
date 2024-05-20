import pytest
from pages.main_page import MainPage
from pages.top_bar_page import TopBarPage
from pages.cart_page import CartPage
from test_data.test_config import ITEM_NAME


@pytest.mark.usefixtures("login_before_tests")
@pytest.mark.cart_items
class TestCartItems:
    def test_add_item_to_cart(self, driver):
        """
        Automates adding an item to the cart and checks if the item is in the cart.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)
        cart_page = CartPage(driver)

        main_page.add_item_to_cart(ITEM_NAME)

        assert top_bar.number_of_items_in_cart() == 1

        top_bar.open_cart()

        assert top_bar.number_of_items_in_cart() == 1
        assert cart_page.is_item_in_the_cart()

    def test_remove_cart_item_from_main_page(self, driver):
        """
        Automates adding an item to the cart and removing it from the main page.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)

        main_page.add_item_to_cart(ITEM_NAME)
        main_page.remove_item_from_cart()

        assert top_bar.number_of_items_in_cart() == 0

    def test_remove_cart_item_from_cart_page(self, driver):
        """
        Automates adding an item to the cart and removing it from the cart page.
        """
        main_page = MainPage(driver)
        top_bar = TopBarPage(driver)
        cart_page = CartPage(driver)

        main_page.add_item_to_cart(ITEM_NAME)
        top_bar.open_cart()
        cart_page.remove_item_from_cart()

        assert top_bar.number_of_items_in_cart() == 0
        assert not cart_page.is_item_in_the_cart()
