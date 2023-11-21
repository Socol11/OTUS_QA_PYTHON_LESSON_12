from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    SLIDER = (By.CSS_SELECTOR, ".slideshow")
    SLIDER_PAGINATION = (By.CSS_SELECTOR, ".swiper-pagination4")

    def get_slider(self, wait):
        try:
            self.get_element(MainPage.SLIDER, wait)
        except TimeoutException:
            raise AssertionError(f"Слайдер отсутствует на странице")

    def get_slider_pagination(self, wait):
        try:
            self.get_element(MainPage.SLIDER_PAGINATION, wait)
        except TimeoutException:
            raise AssertionError(f"Пагинация слайдера отсутствует на странице")
