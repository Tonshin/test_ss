import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Remote(
        command_executor="http://localhost:4444/" + "wd/hub",
        options=webdriver.ChromeOptions()
    )

    yield browser
    browser.quit()