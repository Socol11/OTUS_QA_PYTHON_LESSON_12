from page.BasePage import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    """This class gets elements from admin page"""

    USER_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[id='input-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    H1_TAG = (By.TAG_NAME, "h1")

    def get_user_name_field(self, wait):
        try:
            self.get_element(self.USER_NAME_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")

    def get_password_field(self, wait):
        try:
            self.get_element(self.PASSWORD_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода пароля отсутствует на странице!")

    def get_login_button(self, wait):
        try:
            self.get_element(self.LOGIN_BUTTON, wait)
        except TimeoutException:
            raise AssertionError(f"Кнопка логина отсутствует на странице!")

    def get_forgotten_password_link(self, wait, url):
        selector = "a[href='" + url + "admin/index.php?route=common/forgotten']"
        FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, selector)
        try:
            self.get_element(FORGOTTEN_PASSWORD_LINK, wait)
        except TimeoutException:
            raise AssertionError(f"Ссылка на восстановление пароля отсутствует на странице!")

    def enter_admin_page(self, wait, url, username, password):
        try:
            self.get_element(self.USER_NAME_FIELD, wait).send_keys(username)
            self.get_element(self.PASSWORD_FIELD, wait).send_keys(password)
            self.get_element(self.LOGIN_BUTTON, wait).click()

            h1_header = self.get_element(self.H1_TAG, wait).text
            assert h1_header == "Dashboard"

        except TimeoutException:
            raise AssertionError(f"Вход в панель управления не удался!")
