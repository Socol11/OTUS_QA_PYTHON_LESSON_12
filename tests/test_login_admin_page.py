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
        """This test checks if it possible to enter to admin panel from the /admin page"""
        browser.get(url + self.PAGE)
        admin_page = AdminPage(browser)
        admin_page.enter_admin_page(wait, username, password)
