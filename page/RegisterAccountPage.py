import random
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RegisterAccountPage(BasePage):
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-firstname']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-lastname']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='input-email']")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "input[id='input-telephone']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[id='input-password']")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "input[id='input-confirm']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input.btn-primary[value='Continue']")

    def get_first_name_field(self, wait):
        try:
            self.get_element(self.FIRST_NAME_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")

    def get_last_name_field(self, wait):
        try:
            self.get_element(self.LAST_NAME_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода фамилии пользователя отсутствует на странице!")

    def get_email_field(self, wait):
        try:
            self.get_element(self.EMAIL_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода емейла пользователя отсутствует на странице!")

    def get_telephone_field(self, wait):
        try:
            self.get_element(self.TELEPHONE_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода телефона пользователя отсутствует на странице!")

    def get_password_field(self, wait):
        try:
            self.get_element(self.PASSWORD_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле ввода пароля пользователя отсутствует на странице!")

    def get_password_confirm_field(self, wait):
        try:
            self.get_element(self.PASSWORD_CONFIRM_FIELD, wait)
        except TimeoutException:
            raise AssertionError(f"Поле подтверждения пароля пользователя отсутствует на странице!")

    def get_submit_button(self, wait):
        try:
            self.get_element(self.SUBMIT_BUTTON, wait)
        except TimeoutException:
            raise AssertionError(f"Кнопка Continue отсутствует на странице!")
