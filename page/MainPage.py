import random
import time

from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    """This class gets elements from tne main page"""

    SLIDER = (By.CSS_SELECTOR, ".slideshow")
    SLIDER_PAGINATION = (By.CSS_SELECTOR, ".swiper-pagination")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, ".product-layout")
    CAROUSEL = (By.CSS_SELECTOR, ".carousel")
    BUTTON_GROUP = (By.CSS_SELECTOR, ".button-group")
    PRODUCT_CURRENCY_SYMBOL = (By.CSS_SELECTOR, "p.price")
    CURRENCY_DROPDOWN_TOGGLE = (By.CSS_SELECTOR, "button.dropdown-toggle")
    CURRENCY_SELECT_EUR = (By.CSS_SELECTOR, "button.currency-select[name='EUR']")
    PRODUCT_TITLE_H4 = (By.TAG_NAME, "h4")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "span.hidden-md")
    CART_TOTAL_SPAN = (By.CSS_SELECTOR, "span[id='cart-total']")
    VIEW_CART_LINK = (By.CSS_SELECTOR, "i.fa-shopping-cart")
    CART_PRODUCT_TITLE = (By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[2]/a")
    CART_PRODUCT_PRICE = (By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[5]")



    def get_slider(self, wait):
        try:
            self.get_element(self.SLIDER, wait)
        except TimeoutException:
            raise AssertionError(f"Слайдер отсутствует на странице")

    def get_slider_pagination(self, wait):
        try:
            self.get_element(self.SLIDER_PAGINATION, wait)
        except TimeoutException:
            raise AssertionError(f"Пагинация слайдера отсутствует на странице")

    def get_product_layout(self, wait):
        product_layout_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
        try:
            assert len(product_layout_list) > 0
        except TimeoutException:
            raise AssertionError(f"Блоки с товарами отсутствует на странице")

    def get_carousel(self, wait):
        try:
            self.get_element(self.CAROUSEL, wait)
        except TimeoutException:
            raise AssertionError(f"Карусель отсутствует на странице")

    def get_buttons_in_product_layout(self, wait):
        product_layout_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
        # Выбираем случайное число из диапазона от 0 до количества продуктов
        number = random.randint(0, len(product_layout_list) - 1)
        # Выбираем случайный элемент из имеющихся
        random_product_layout = self.get_elements(self.PRODUCT_LAYOUT, wait)[number]
        try:
            random_product_layout.find_element(*self.BUTTON_GROUP)
        except TimeoutException:
            raise AssertionError(f"Нет группы кнопок в product layout")

    # def get_default_currency(self, wait):
    #     # Проверяем валюту по умолчанию
    #     # Собираем полный список всех товаров на главной странице
    #     product_layout_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
    #     number = random.randint(0, len(product_layout_list) - 1)
    #
    #     # Выбираем случайный товар из имеющихся
    #     random_product = self.get_elements(self.PRODUCT_LAYOUT, wait)[number]
    #
    #     # Сохраняем символ валюты случайно выбранного товара в переменную
    #     product_currency_symbol = random_product.find_element(*self.PRODUCT_CURRENCY_SYMBOL).text[0]
    #     return product_currency_symbol
    #
    # def change_currency(self, wait):
    #     # Меняем валюту на EUR
    #     self.get_element(self.CURRENCY_DROPDOWN_TOGGLE, wait).click()
    #     self.get_element(self.CURRENCY_SELECT_EUR, wait).click()
    #
    #     # Проверяем валюту после её смены
    #     # Собираем полный список всех товаров на главной странице
    #     product_layout_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
    #     number = random.randint(0, len(product_layout_list) - 1)
    #
    #     # Выбираем случайный товар из имеющихся
    #     random_product = self.get_elements(self.PRODUCT_LAYOUT, wait)[number]
    #
    #     # Сохраняем символ валюты случайно выбранного товара в переменную
    #     product_currency_symbol = random_product.find_element(By.CSS_SELECTOR, "p.price").text.splitlines()[0][-1]
    #     return product_currency_symbol

    # def get_random_product_currency_symbol(self, wait):
    #     # Собираем полный список всех товаров на главной странице
    #     product_layout_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
    #     number = random.randint(0, len(product_layout_list) - 1)
    #     # Выбираем случайный товар из имеющихся
    #     random_product = self.get_elements(self.PRODUCT_LAYOUT, wait)[number]
    #     # Сохраняем символ валюты случайно выбранного товара в переменную
    #     product_currency_symbol = random_product.find_element(*self.PRODUCT_CURRENCY_SYMBOL)
    #     return product_currency_symbol
    #
    # def get_default_currency(self, wait):
    #     # Проверяем валюту по умолчанию
    #     return self.get_random_product_currency_symbol(wait).text[0]
    #
    # def change_currency(self, wait):
    #     # Меняем валюту на EUR
    #     self.get_element(self.CURRENCY_DROPDOWN_TOGGLE, wait).click()
    #     self.get_element(self.CURRENCY_SELECT_EUR, wait).click()
    #     # Проверяем валюту после её смены
    #     return self.get_random_product_currency_symbol(wait).text.splitlines()[0][-1]

    def get_random_product(self, wait, n=1):
        # Собираем полный список всех товаров на главной странице
        product_list = self.get_elements(self.PRODUCT_LAYOUT, wait)
        number = random.randint(0, len(product_list) - n)
        # Выбираем случайный товар из имеющихся
        random_product = self.get_elements(self.PRODUCT_LAYOUT, wait)[number]
        return random_product

    def get_default_currency(self, wait):
        # Выбираем случайный товар на странице
        random_product = self.get_random_product(wait)
        # Сохраняем символ валюты случайно выбранного товара в переменную
        product_currency_symbol = random_product.find_element(*self.PRODUCT_CURRENCY_SYMBOL)
        # Возвращаем символ валюты
        return product_currency_symbol.text[0]

    def change_currency(self, wait):
        # Меняем валюту на EUR
        self.get_element(self.CURRENCY_DROPDOWN_TOGGLE, wait).click()
        self.get_element(self.CURRENCY_SELECT_EUR, wait).click()
        # Выбираем случайный товар на странице
        random_product = self.get_random_product(wait)
        # Сохраняем символ валюты случайно выбранного товара в переменную
        product_currency_symbol = random_product.find_element(*self.PRODUCT_CURRENCY_SYMBOL)
        # Возвращаем символ валюты
        return product_currency_symbol.text.splitlines()[0][-1]

    def add_random_product_into_cart(self, wait):
        # Выбираем случайный товар на странице
        random_product = self.get_random_product(wait, n=3)  # для этого теста n=3, так как кнопки добавить в корзину работают только у двух первых продуктов

        # Сохраняем название случайно выбранного товара и его цену в переменные
        product_title = random_product.find_element(*self.PRODUCT_TITLE_H4).text
        product_price = random_product.find_element(*self.PRODUCT_CURRENCY_SYMBOL).text.splitlines()[0]
        # Строка содержит доп. символы и имеет вид '$123.20\nEx Tax: $101.00', поэтому делаем split

        # Добавляем выбранный товар в корзину кликом по кнопке Add to cart
        random_product.find_element(*self.ADD_TO_CART_BUTTON).click()

        # Переходим в корзину
        self.get_element(self.CART_TOTAL_SPAN, wait).click()
        self.get_element(self.VIEW_CART_LINK, wait).click()

        # Проверяем соответствие добавленного в корзину товара
        cart_product_title = self.get_element(self.CART_PRODUCT_TITLE, wait).text
        cart_product_price = self.get_element(self.CART_PRODUCT_PRICE, wait).text

        return product_title, cart_product_title, product_price, cart_product_price
