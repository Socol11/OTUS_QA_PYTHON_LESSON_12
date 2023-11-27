from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_admin_page(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']"))).send_keys('user')

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']"))).send_keys('bitnami')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary"))).click()

        h1_header_logged = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text

        assert h1_header_logged == "Dashboard"

    except TimeoutException:
        raise AssertionError(f"Вход в панель управления не удался!")


def test_login_unlog_admin_page(browser, url):
    browser.get(url + '/admin')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']"))).send_keys('user')

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']"))).send_keys('bitnami')

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary"))).click()

        h1_header_logged = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text

        assert h1_header_logged == "Dashboard"

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()

        h1_header_unlog = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text

        assert h1_header_unlog == "Please enter your login details."

    except TimeoutException:
        raise AssertionError(f"Разлогиниться не удалось!")
