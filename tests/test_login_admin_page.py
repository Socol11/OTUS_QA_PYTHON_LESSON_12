from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_name_field_presence(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")


def test_password_field_presence(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода пароля отсутствует на странице!")


def test_login_button_presence(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))
    except TimeoutException:
        raise AssertionError(f"Кнопка логина отсутствует на странице!")


def test_forgotten_password_link_presence(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    selector = "a[href='" + url + "admin/index.php?route=common/forgotten']"
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        raise AssertionError(f"Ссылка на восстановление пароля отсутствует на странице!")


def test_login_admin_page(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']"))).send_keys('user')

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']"))).send_keys('bitnami')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary"))).click()

        h1_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text

        assert h1_header == "Dashboard"

    except TimeoutException:
        raise AssertionError(f"Вход в панель управления не удался!")
