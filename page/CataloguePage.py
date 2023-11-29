import random
from selenium.webdriver import ActionChains
from page.BasePage import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class CataloguePage(BasePage):
    NAVBAR_NAV = (By.CLASS_NAME, "navbar-nav")
    LI_ELEMENTS = (By.XPATH, './*')
    SEE_ALL = (By.CLASS_NAME, 'see-all')
    H2_TAG = (By.TAG_NAME, 'h2')
    LIST_GROUP = (By.CSS_SELECTOR, ".list-group")
    IMG_THUMBNAIL = (By.CSS_SELECTOR, ".img-thumbnail")
    BTN_GROUP = (By.CSS_SELECTOR, ".btn-group")
    SORT_BY_DROPDOWN = (By.XPATH, "//*[@id='content']/div[3]/div[3]/div/label")
    LIMIT_DROPDOWN = (By.XPATH, "//*[@id='content']/div[1]/div[4]/div/label")
    PRODUCT_LAYOUT = (By.CSS_SELECTOR, ".product-layout")
    PRODUCT_CURRENCY_SYMBOL = (By.CSS_SELECTOR, "p.price")
    CURRENCY_DROPDOWN_TOGGLE = (By.CSS_SELECTOR, "button.dropdown-toggle")
    CURRENCY_SELECT_EUR = (By.CSS_SELECTOR, "button.currency-select[name='EUR']")
    CURRENCY_SELECT_GBP = (By.CSS_SELECTOR, "button.currency-select[name='GBP']")

    def get_navbar_random_element(self, browser, wait):
        # Get the list of li elements of menu
        ul_navbar = self.get_element(CataloguePage.NAVBAR_NAV, wait)
        li_elements = ul_navbar.find_elements(*CataloguePage.LI_ELEMENTS)
        # Choose the random li element
        number = random.randint(0, len(li_elements) - 1)
        random_li_element = li_elements[number]
        li_element_text = random_li_element.text
        # Move the cursor to li_element
        ActionChains(browser).move_to_element(random_li_element).perform()
        # Click on the appropriate link
        try:
            random_li_element.find_element(*self.SEE_ALL).click()
        except NoSuchElementException:
            random_li_element.click()
        catalogue_h2_tag = self.get_element(self.H2_TAG, wait)
        return catalogue_h2_tag, li_element_text

    def get_catalogue_menu(self, wait):
        try:
            self.get_element(self.LIST_GROUP, wait)
        except TimeoutException:
            raise AssertionError(f"Меню каталога отсутствует на странице!")

    def get_category_img_thumbnail(self, wait):
        try:
            self.get_element(self.IMG_THUMBNAIL, wait)
        except TimeoutException:
            raise AssertionError(f"Миниатюра категории отсутствует на странице!")

    def get_display_mode_button(self, wait):
        try:
            self.get_element(self.BTN_GROUP, wait)
        except TimeoutException:
            raise AssertionError(f"Кнопки переключения режима отображения товаров отсутствуют на странице!")

    def get_sort_by_dropdown(self, wait):
        sort_by = self.get_element(self.SORT_BY_DROPDOWN, wait)
        return sort_by

    def get_limit_dropdown(self, wait):
        show = self.get_element(self.LIMIT_DROPDOWN, wait)
        return show

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
