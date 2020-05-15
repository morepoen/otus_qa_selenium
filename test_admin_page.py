from config import ADMIN, ADMIN_LOGIN, ADMIN_PASSWORD
from locators import LoginAdminPageLocators, AdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_admin_page_elements(browser):
    browser.get(ADMIN)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-username')))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.panel-title')))
    browser.find_element(*LoginAdminPageLocators.PASSWORD)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type=submit]')))
    browser.find_element(*LoginAdminPageLocators.FORGOT_PASSWORD)


def test_admin_login_and_logout(browser):
    wait = WebDriverWait(browser, 3)
    browser.get(ADMIN)
    browser.find_element(*LoginAdminPageLocators.USERNAME).send_keys(ADMIN_LOGIN)
    browser.find_element(*LoginAdminPageLocators.PASSWORD).send_keys(ADMIN_PASSWORD)
    browser.find_element(*LoginAdminPageLocators.LOGIN_BUTTON).click()
    wait.until(EC.url_contains('/admin/index.php?route=common/dashboard&user_token='))
    browser.find_element(*AdminPageLocators.LOGOUT_BUTTON).click()
    wait.until(EC.url_contains('/admin/index.php?route=common/login'))


def test_admin_go_to_products_page(browser):
    wait = WebDriverWait(browser, 3)
    browser.get(ADMIN)
    browser.find_element(*LoginAdminPageLocators.USERNAME).send_keys(ADMIN_LOGIN)
    browser.find_element(*LoginAdminPageLocators.PASSWORD).send_keys(ADMIN_PASSWORD)
    browser.find_element(*LoginAdminPageLocators.LOGIN_BUTTON).click()
    browser.find_element(*AdminPageLocators.CATALOG).click()
    browser.find_element(*AdminPageLocators.CATALOG_PRODUCTS).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table.table-bordered.table-hover')))
    browser.find_element(*AdminPageLocators.LOGOUT_BUTTON).click()
