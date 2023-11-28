from page.AdminPage import AdminPage


class TestUnlogAdminPage:
    """Тестируем разлогинивание из панели администратора"""

    PAGE = '/admin'
    WAIT = 5
    USERNAME = 'user'
    PASSWORD = 'bitnami'

    def test_unlog_admin_page(self, browser, url, wait=WAIT):
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.enter_admin_page(wait, username=self.USERNAME, password=self.PASSWORD)
        admin_page.quit_admin_page(wait)

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
#         h1_header_logged = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
#
#         assert h1_header_logged == "Dashboard"
#
#     except TimeoutException:
#         raise AssertionError(f"Вход в панель управления не удался!")


# def test_login_unlog_admin_page(browser, url):
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
#         h1_header_logged = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
#
#         assert h1_header_logged == "Dashboard"
#
#         wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()
#
#         h1_header_unlog = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text
#
#         assert h1_header_unlog == "Please enter your login details."
#
#     except TimeoutException:
#         raise AssertionError(f"Разлогиниться не удалось!")
