from config import BASE_URL
from locators import MainPageLocators


def test_main_page(browser):
    browser.get(BASE_URL)
    browser.find_element(*MainPageLocators.CART)
    browser.find_element(*MainPageLocators.NAVBAR)
    browser.find_element(*MainPageLocators.SEARCH)
    browser.find_element(*MainPageLocators.SWIPER)
    products = browser.find_elements(*MainPageLocators.PRODUCTS)
    assert len(products) > 0, 'did not find products on the main page'


