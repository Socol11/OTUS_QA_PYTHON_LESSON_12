from page.RegisterAccountPage import RegisterAccountPage


class TestRegisterAccountPage:
    """Тестируем страницу регистрации аккаунта"""

    PAGE = 'index.php?route=account/register'
    WAIT = 5

    def test_first_name_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the first name field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_first_name_field(wait)

    def test_last_name_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the last name field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_last_name_field(wait)

    def test_email_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the email field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_email_field(wait)

    def test_telephone_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the telephone field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_telephone_field(wait)

    def test_password_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the password field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_password_field(wait)

    def test_password_confirm_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the password confirm field is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_password_confirm_field(wait)

    def test_submit_button_presence(self, browser, url, wait=WAIT):
        """This test checks if the submit button is present on the register account page"""
        browser.get(url + self.PAGE)
        register_account_page = RegisterAccountPage(browser)
        register_account_page.get_submit_button(wait)
