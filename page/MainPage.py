import random
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    SLIDER = (By.CSS_SELECTOR, ".slideshow")
    SLIDER_PAGINATION = (By.CSS_SELECTOR, ".swiper-pagination")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, ".product-layout")
    CAROUSEL = (By.CSS_SELECTOR, ".carousel")
    BUTTON_GROUP = (By.CSS_SELECTOR, ".button-group")

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

    def get_product_layout(self, wait):
        product_layout_list = self.get_elements(MainPage.PRODUCT_LAYOUT, wait)
        try:
            assert len(product_layout_list) > 0
        except TimeoutException:
            raise AssertionError(f"Блоки с товарами отсутствует на странице")

    def get_carousel(self, wait):
        try:
            self.get_element(MainPage.CAROUSEL, wait)
        except TimeoutException:
            raise AssertionError(f"Карусель отсутствует на странице")

    def get_buttons_in_product_layout(self, wait):
        product_layout_list = self.get_elements(MainPage.PRODUCT_LAYOUT, wait)
        # Выбираем случайное число из диапазона от 0 до количества продуктов
        number = random.randint(0, len(product_layout_list) - 1)
        # Выбираем случайный элемент из имеющихся
        random_product_layout = self.get_elements(MainPage.PRODUCT_LAYOUT, wait)[number]
        try:
            random_product_layout.find_element(*MainPage.BUTTON_GROUP)
        except TimeoutException:
            raise AssertionError(f"Нет группы кнопок в product layout")
