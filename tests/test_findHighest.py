import json
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.shopPage import ShopPage

import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sourceDemo_data.json')
file_path = os.path.abspath(file_path)

with open(file_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_find_highest_price(browserInstance, test_list_item):
    driver = browserInstance
    login_page = LoginPage(driver)
    login_page.login(test_list_item["userName"], test_list_item["password"])

    shop_page = ShopPage(driver)

    totalPrice, highPrice = shop_page.add_highest_priced_item_to_cart()

    print("Total in cart is:", totalPrice)
    print("Highest price found:", highPrice)

    assert totalPrice == highPrice, f"Expected {highPrice}, got {totalPrice}"
