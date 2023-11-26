from page.RegisterAccountPage import RegisterAccountPage


class TestRegisterAccountPage:
    PAGE = 'index.php?route=account/register'
    WAIT = 5

    def test_first_name_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the first name field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_first_name_field(wait)

    def test_last_name_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the last name field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_last_name_field(wait)

    def test_email_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the email field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_email_field(wait)

    def test_telephone_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the telephone field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_telephone_field(wait)

    def test_password_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the password field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_password_field(wait)

    def test_password_confirm_field_presence(self, browser, url, wait=WAIT):
        """This test checks if the password confirm field is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_password_confirm_field(wait)

    def test_submit_button_presence(self, browser, url, wait=WAIT):
        """This test checks if the submit button is present on the register account page"""
        browser.get(url + self.PAGE)
        name_field = RegisterAccountPage(browser)
        name_field.get_submit_button(wait)

# def test_first_name_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-firstname']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода имени пользователя отсутствует на странице!")


# def test_last_name_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-lastname']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода фамилии пользователя отсутствует на странице!")


# def test_email_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-email']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода емейла пользователя отсутствует на странице!")


# def test_telephone_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-telephone']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода телефона пользователя отсутствует на странице!")
#
#
# def test_password_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-password']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода пароля пользователя отсутствует на странице!")
#
#
# def test_password_confirm_field_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='input-confirm']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле подтверждения пароля пользователя отсутствует на странице!")
#
#
# def test_submit_button_presence(browser, url):
#     browser.get(url + 'index.php?route=account/register')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.btn-primary[value='Continue']")))
#     except TimeoutException:
#         raise AssertionError(f"Кнопка Continue отсутствует на странице!")
