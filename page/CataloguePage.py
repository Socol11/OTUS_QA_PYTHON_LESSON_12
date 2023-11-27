import random
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

    def get_navbar_elements_list(self, wait):
        """Gets the list of li elements of menu"""
        ul_navbar = self.get_element(CataloguePage.NAVBAR_NAV, wait)
        li_elements = ul_navbar.find_elements(*CataloguePage.LI_ELEMENTS)
        return li_elements

    def get_navbar_random_element(self, navbar_elements_list):
        """Choose the random li element"""
        number = random.randint(0, len(navbar_elements_list) - 1)
        random_li_element = navbar_elements_list[number]
        return random_li_element

    def get_catalogue_menu(self, wait):
        """"""
        try:
            self.get_element(self.LIST_GROUP, wait)
        except TimeoutException:
            raise AssertionError(f"Меню каталога отсутствует на странице!")

    def get_category_img_thumbnail(self, wait):
        """"""
        try:
            self.get_element(self.IMG_THUMBNAIL, wait)
        except TimeoutException:
            raise AssertionError(f"Миниатюра категории отсутствует на странице!")

    def get_display_mode_button(self, wait):
        """"""
        try:
            self.get_element(self.BTN_GROUP, wait)
        except TimeoutException:
            raise AssertionError(f"Кнопки переключения режима отображения товаров отсутствуют на странице!")

    def get_sort_by_dropdown(self, wait):
        """"""
        sort_by = self.get_element(self.SORT_BY_DROPDOWN, wait)
        return sort_by

    def get_limit_dropdown(self, wait):
        """"""
        show = self.get_element(self.LIMIT_DROPDOWN, wait)
        return show
