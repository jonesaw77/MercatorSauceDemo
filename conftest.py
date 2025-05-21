import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.headless = False
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--ignore-certificate-errors")
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)
    elif browser_name == "edge":
        edge_options = webdriver.EdgeOptions()
        # edge_options.add_argument("--headless")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(4)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()
