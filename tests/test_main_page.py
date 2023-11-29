from page.MainPage import MainPage


class TestMainPage:
    """Тестируем главную страницу сайта"""

    WAIT = 5

    def test_presence_of_a_slider(self, browser, url, wait=WAIT):
        """This test checks if the slider is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_slider(wait)

    def test_presence_of_slider_pagination(self, browser, url, wait=WAIT):
        """This test checks if the slider pagination element is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_slider_pagination(wait)

    def test_presence_of_product_layout(self, browser, url, wait=WAIT):
        """This test checks if the block of products is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_product_layout(wait)

    def test_presence_of_carousel(self, browser, url, wait=WAIT):
        """This test checks if the carousel of brands is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_carousel(wait)

    def test_presence_of_buttons_in_product_layout(self, browser, url, wait=WAIT):
        """This test randomly checks if the group of buttons is present in a product layout"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_buttons_in_product_layout(wait)
