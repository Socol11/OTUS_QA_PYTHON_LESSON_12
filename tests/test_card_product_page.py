from page.ProductPage import ProductPage


class TestCardProductPage:
    """Тестируем карточку товара"""

    PAGE = '/iphone'
    WAIT = 5
    NAME = 'iPhone'
    BRAND = 'Apple'
    PRICE = '$123.20'

    def test_thumbnails_presence(self, browser, url, wait=WAIT):
        """This test checks if a product thumbnail is available"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_thumbnail(wait)

    def test_h1_title_presence(self, browser, url, wait=WAIT, name=NAME):
        """This test checks if the content of the H1 tag matches the product name"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_h1_title(wait, name)

    def test_brand_info_presence(self, browser, url, wait=WAIT, brand=BRAND):
        """This test checks if the content of the brand name element matches the product brand"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_brand_info(wait, brand)

    def test_price_info_presence(self, browser, url, wait=WAIT, price=PRICE):
        """This test checks if the product price info from H2 tag matches the real product price"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_price_info(wait, price)

    def test_input_quantity_presence(self, browser, url, wait=WAIT):
        """This test checks if the element for selecting the quantity
        of the product is present on the page"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_input_quantity(wait)

    def test_add_to_cart_button_presence(self, browser, url, wait=WAIT):
        """This test check if the 'Add to cart' button is present on the page"""
        browser.get(url + self.PAGE)
        product_page = ProductPage(browser)
        product_page.get_add_to_cart_button(wait)
