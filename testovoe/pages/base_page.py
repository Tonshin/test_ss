from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from data.data import TIME_WAIT


class BasePage:
    def __init__(self, browser, url=None, timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def element_is_visible(self, locator: WebElement or tuple[str, str], timeout: int = TIME_WAIT) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator: WebElement or tuple[str, str], timeout: int = TIME_WAIT) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))