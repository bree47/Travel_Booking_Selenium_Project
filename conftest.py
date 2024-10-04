import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    """Fixture to initialize the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
