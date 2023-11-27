from page.MainPage import MainPage


class TestCurrencyChange:
    """Тестируем валюты на главной странице"""

    USD = "$"
    EUR = "€"

    def test_default_currency(self, browser, url, wait=5, currency=USD):
        """This test checks default currency for main page"""
        browser.get(url)
        main_page = MainPage(browser)
        product_currency_symbol = main_page.get_default_currency(wait)
        assert product_currency_symbol == currency

    def test_change_currency(self, browser, url, wait=5, currency=EUR):
        """This test checks if it's possible to change the currency for main page"""
        browser.get(url)
        main_page = MainPage(browser)
        product_currency_symbol = main_page.change_currency(wait)
        assert product_currency_symbol == currency

# def test_default_currency(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#
#     # Проверяем валюту по умолчанию
#     # Собираем полный список всех товаров на главной странице
#     product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
#     number = random.randint(0, len(product_layout_list) - 1)
#
#     # Выбираем случайный товар из имеющихся
#     random_product_layout = wait.until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]
#
#     # Сохраняем символ валюты случайно выбранного товара в переменную
#     product_currency_symbol = random_product_layout.find_element(By.CSS_SELECTOR, "p.price").text[0]
#
#     assert product_currency_symbol == "$"


# def test_change_currency(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#
#     # Меняем валюту на EUR
#     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.dropdown-toggle"))).click()
#     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.currency-select[name='EUR']"))).click()
#
#     # Проверяем валюту после её смены
#     # Собираем полный список всех товаров на главной странице
#     product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
#     number = random.randint(0, len(product_layout_list) - 1)
#
#     # Выбираем случайный товар из имеющихся
#     random_product_layout = wait.until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]
#
#     # Сохраняем символ валюты случайно выбранного товара в переменную
#     product_currency_symbol = random_product_layout.find_element(By.CSS_SELECTOR, "p.price").text.splitlines()[0][-1]
#
#     assert product_currency_symbol == "€"
