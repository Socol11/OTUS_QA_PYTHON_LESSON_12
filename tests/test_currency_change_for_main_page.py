from page.MainPage import MainPage


class TestCurrencyChangeForMainPage:
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
