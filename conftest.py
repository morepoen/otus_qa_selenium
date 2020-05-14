import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions


def pytest_addoption(parser):

    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = ChromeOptions()
        # options.add_argument("headless")
        options.add_argument("start-maximized")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        # options.headless = True
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
