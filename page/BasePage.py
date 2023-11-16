"""
Класс абстрактной базовой страницы, от которого можно наследовать другие классы сраниц для поиска элементов
"""


from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for the {locator} element to be visible!")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Didn't wait for the {locator} elements to be visible!")
