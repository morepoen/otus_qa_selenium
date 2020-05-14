from config import PRODUCT
from locators import ProductPageLocators


def test_product_page(browser):
    browser.get(PRODUCT)
    browser.find_element(*ProductPageLocators.DESCRIPTION)
    browser.find_element(*ProductPageLocators.PRICE)
    browser.find_element(*ProductPageLocators.QUANTITY_FIELD)
    browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
    browser.find_elements(*ProductPageLocators.PRODUCT_PICTURES)
