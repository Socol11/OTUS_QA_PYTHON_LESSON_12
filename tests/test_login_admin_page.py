from page.AdminPage import AdminPage


class TestLoginAdminPage:
    """Тестируем страницу входа в панель администратора"""

    PAGE = '/admin'
    WAIT = 5
    USERNAME = 'user'
    PASSWORD = 'bitnami'

    def test_user_name_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the username field is present on the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.get_user_name_field(wait)

    def test_password_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the password field is present on the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.get_password_field(wait)

    def test_login_button_presence(self, browser, url, wait=WAIT):
        """This test checks if the login button is present on the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.get_login_button(wait)

    def test_forgotten_password_link_presence(self, browser, url, wait=WAIT):
        """This test checks if the forgotten password link is present on the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.get_forgotten_password_link(wait, url)

    def test_enter_admin_page(self, browser, url, wait=WAIT, username=USERNAME, password=PASSWORD):
        """This test checks if possible to enter to admin panel from the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.enter_admin_page(wait, url, username, password)

# def test_user_name_field_presence(browser, url):
#     browser.get(url + '/admin')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")


# def test_password_field_presence(browser, url):
#     browser.get(url + '/admin')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода пароля отсутствует на странице!")


# def test_login_button_presence(browser, url):
#     browser.get(url + '/admin')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))
#     except TimeoutException:
#         raise AssertionError(f"Кнопка логина отсутствует на странице!")


# def test_forgotten_password_link_presence(browser, url):
#     browser.get(url + '/admin')
#     wait = WebDriverWait(browser, 5)
#     selector = "a[href='" + url + "admin/index.php?route=common/forgotten']"
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
#     except TimeoutException:
#         raise AssertionError(f"Ссылка на восстановление пароля отсутствует на странице!")


# def test_login_admin_page(browser, url):
#     browser.get(url + '/admin')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-username']"))).send_keys('user')
#
#         wait.until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']"))).send_keys('bitnami')
#
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary"))).click()
#
#         h1_header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
#
#         assert h1_header == "Dashboard"
#
#     except TimeoutException:
#         raise AssertionError(f"Вход в панель управления не удался!")
