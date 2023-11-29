from page.MainPage import MainPage


class TestMainPageAddProductIntoCart:

    def test_add_product_into_cart(self, browser, url, wait=5):
        """This test adds a randomly selected item from the home page to the cart
        and then checks if the product has been added to the cart"""

        browser.get(url)
        main_page = MainPage(browser)

        product_title, cart_product_title, product_price, cart_product_price = main_page.add_random_product_into_cart(wait)

        assert product_title == cart_product_title
        assert product_price == cart_product_price
