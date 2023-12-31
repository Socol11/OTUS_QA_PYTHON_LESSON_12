from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_first_name_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-firstname']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")


def test_last_name_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-lastname']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода фамилии пользователя отсутствует на странице!")


def test_email_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-email']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода емейла пользователя отсутствует на странице!")


def test_telephone_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-telephone']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода телефона пользователя отсутствует на странице!")


def test_password_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода пароля пользователя отсутствует на странице!")


def test_password_confirm_field_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-confirm']")))
    except TimeoutException:
        raise AssertionError(f"Поле подтверждения пароля пользователя отсутствует на странице!")


def test_submit_button_presence(browser, url):
    browser.get(url + 'index.php?route=account/register')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.btn-primary[value='Continue']")))
    except TimeoutException:
        raise AssertionError(f"Кнопка Continue отсутствует на странице!")
