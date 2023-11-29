from page.CataloguePage import CataloguePage


class TestCurrencyChangeForCataloguePage:
    """Тестируем валюты на странице каталога"""

    USD = "$"
    EUR = "€"
    GBP = "£"

    def test_default_currency(self, browser, url, wait=5, currency=USD):
        """This test checks default currency for /smartphone page"""
        browser.get(url + 'smartphone')
        catalogue_page = CataloguePage(browser)
        product_currency_symbol = catalogue_page.get_default_currency(wait)
        assert product_currency_symbol == currency

    def test_change_currency(self, browser, url, wait=5, currency=EUR):
        """This test checks if it's possible to change the currency for /smartphone page"""
        browser.get(url + 'smartphone')
        catalogue_page = CataloguePage(browser)
        product_currency_symbol = catalogue_page.change_currency(wait)
        assert product_currency_symbol == currency
