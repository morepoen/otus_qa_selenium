from selenium.webdriver.common.by import By


class MainPageLocators:
    NAVBAR = (By.CSS_SELECTOR, '.collapse.navbar-collapse.navbar-ex1-collapse')
    SEARCH = (By.XPATH, '//div[@id="search"]')
    CART = (By.CSS_SELECTOR, '#cart')
    SWIPER = (By.CSS_SELECTOR, '.swiper-container.swiper-container-horizontal')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb.transition')


class CatalogPageLocators:
    HEADER = (By.CSS_SELECTOR, '#top')
    SIDEBAR = (By.CSS_SELECTOR, '#column-left')
    CURRENT_CATEGORY = (By.XPATH, '//h2')
    CATEGORY_DESCRIPTION = (By.CSS_SELECTOR, '.col-sm-10')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb')


class LoginPageLocators:
    CONTINUE_BUTTON = (By.XPATH, '//div[@class="well"]/a[contains(@href, "register")]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[value=Login]')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    SIDEBAR = (By.CSS_SELECTOR, '#column-right')


class ProductPageLocators:
    DESCRIPTION = (By.CSS_SELECTOR, '#tab-description')
    PRODUCT_PICTURES = (By.XPATH, '//a[@title="Samsung Galaxy Tab 10.1"]')
    PRICE = (By.XPATH, '//li/h2')
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')


class AdminPageLocators:
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type=submit]')
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "forgotten")]')
    FORM_TITLE = (By.CSS_SELECTOR, '.panel-title')







