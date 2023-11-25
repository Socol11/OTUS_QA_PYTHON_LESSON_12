from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    UL_THUMBNAILS = (By.CSS_SELECTOR, "ul.thumbnails")
    H1_TAG = (By.TAG_NAME, "h1")
    BRAND_INFO = (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[1]/li[1]/a")
    PRICE_INFO = (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[2]/li[1]/h2")
    INPUT_QUANTITY = (By.CSS_SELECTOR, "input[name='quantity']")
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "button[id='button-cart']")

    def get_thumbnail(self, wait):
        try:
            self.get_element(self.UL_THUMBNAILS, wait)
        except TimeoutException:
            raise AssertionError(f"Миниатюра товара отсутствует на странице!")

    def get_h1_title(self, wait, name):
        h1_tag_text = self.get_element(self.H1_TAG, wait).text
        try:
            assert h1_tag_text == name
        except TimeoutException:
            raise AssertionError(f"Название продукта не соответствует требуемому!")

    def get_brand_info(self, wait, brand):
        brand_info = self.get_element(self.BRAND_INFO, wait).text
        try:
            assert brand_info == brand
        except TimeoutException:
            raise AssertionError(f"Название бренда не соответствует требуемому!")

    def get_price_info(self, wait, price):
        try:
            assert self.get_element(self.PRICE_INFO, wait).text == price
        except TimeoutException:
            raise AssertionError(f"Цена товара неверна!")

    def get_input_quantity(self, wait):
        try:
            self.get_element(self.INPUT_QUANTITY, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода количества товаров отсутствует!")

    def get_add_to_cart_button(self, wait):
        try:
            self.get_element(self.ADD_TO_CARD_BUTTON, wait)
        except TimeoutException:
            raise AssertionError(f"Кнопка добавления в корзину отсутствует!")
