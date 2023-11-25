from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator: tuple, wait: int):
        return WebDriverWait(self.browser, wait).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, wait: int):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for the {locator} elements to be visible!")

    def type_text_action(self, locator, text_type):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).send_keys(text_type)

    def click_action(self, locator):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).click()

    def get_element_text(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).text()

    def get_page_title(self):
        return self.browser.title
