"""Check elements of a product page"""

from page.ProductPage import ProductPage


class TestCardProductPage:

    def test_thumbnails_presence(self, browser, url, wait=5):
        """This test checks if a product thumbnail is available"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_thumbnail(wait)

    def test_h1_title_presence(self, browser, url, wait=5, name='iPhone'):
        """This test checks if the content of the H1 tag matches the product name"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_h1_title(wait, name)

    def test_brand_info_presence(self, browser, url, wait=5, brand='Apple'):
        """This test checks if the content of the brand name element matches the product brand"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_brand_info(wait, brand)

    def test_price_info_presence(self, browser, url, wait=5, price='$123.20'):
        """This test checks if the product price info from H2 tag matches the real product price"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_price_info(wait, price)

    def test_input_quantity_presence(self, browser, url, wait=5):
        """This test checks if the element for selecting the quantity
        of the product is present on the page"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_input_quantity(wait)

    def test_add_to_cart_button_presence(self, browser, url, wait=5):
        """This test check if the 'Add to cart' button is present on the page"""
        browser.get(url + '/iphone')
        product_page = ProductPage(browser)
        product_page.get_add_to_cart_button(wait)

# def test_thumbnails_presence(browser, url):
#     """This test checks if a product thumbnail is available"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.thumbnails")))
#     except TimeoutException:
#         raise AssertionError(f"Миниатюра товара отсутствует на странице!")


# def test_h1_title_presence(browser, url):
#     """This test checks if the content of the H1 tag matches the product name"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         assert wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text == 'iPhone'
#     except TimeoutException:
#         raise AssertionError(f"Название продукта не соответствует требуемому!")


# def test_brand_info_presence(browser, url):
#     """This test checks if the content of the brand name element matches the product brand"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         assert wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[1]/li[1]/a"))).text == 'Apple'
#     except TimeoutException:
#         raise AssertionError(f"Название бренда не соответствует требуемому!")
#
#
# def test_price_info_presence(browser, url):
#     """This test checks if the product price info from H2 tag matches the real product price"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         assert wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[2]/li[1]/h2"))).text == '$123.20'
#     except TimeoutException:
#         raise AssertionError(f"Цена товара неверна!")
#
#
# def test_input_quantity_presence(browser, url):
#     """This test checks if the element for selecting the quantity
#     of the product is present on the page"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='quantity']")))
#     except TimeoutException:
#         raise AssertionError(f"Поле ввода количества товаров отсутствует!")
#
#
# def test_add_to_cart_button_presence(browser, url):
#     """This test check if the 'Add to cart' button is present on the page"""
#     browser.get(url + '/iphone')
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
#     except TimeoutException:
#         raise AssertionError(f"Кнопка добавления в корзину отсутствует!")
