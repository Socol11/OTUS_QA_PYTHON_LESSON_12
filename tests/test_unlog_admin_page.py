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
