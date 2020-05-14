from config import CATALOG
from locators import CatalogPageLocators


def test_catalog_page(browser):
    browser.get(CATALOG)
    browser.find_element(*CatalogPageLocators.HEADER)
    browser.find_element(*CatalogPageLocators.SIDEBAR)
    browser.find_element(*CatalogPageLocators.CURRENT_CATEGORY)
    browser.find_element(*CatalogPageLocators.CATEGORY_DESCRIPTION)
    products = browser.find_elements(*CatalogPageLocators.PRODUCTS)
    assert len(products) > 0, 'did not find products on the catalog page'
