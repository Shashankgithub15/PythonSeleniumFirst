import json

import pytest
from FrameWorkWithDesign.pageObjects.checkout_confirmation import Checkout_Confirmation
from FrameWorkWithDesign.pageObjects.login import LoginPage
from FrameWorkWithDesign.pageObjects.shopPage import ShopPage

test_data_path = './TestData/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_data_list = test_data["data2"]
    print(test_data_list)
#
# @pytest.mark.parametrize("test_data_item", test_data_list)
# def test_e2e(browserInstance, test_data_item):
#     driver = browserInstance
#     driver.get("https://rahulshettyacademy.com/loginpagepractise/")
#
#     loginPage = LoginPage(driver)
#     loginPage.login(test_data_item["username"], test_data_item["password"])
#
#     shop_Page = ShopPage(driver)
#     shop_Page.add_product_to_cart(test_data_item["product"])
#     print(test_data_item["product"])
#     shop_Page.go_To_Cart()
#
#     check_confirmationclass = Checkout_Confirmation(driver)
#     check_confirmationclass.checkout()
#     check_confirmationclass.enter_delivery_address(test_data_item["deliveryAddress"])
#     check_confirmationclass.validate_order()
#
#     driver.close()
