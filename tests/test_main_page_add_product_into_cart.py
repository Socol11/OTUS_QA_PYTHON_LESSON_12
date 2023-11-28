from page.MainPage import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class TestMainPageAddProductIntoCart:

    def test_add_product_into_cart(self, browser, url, wait=5):
        """This test adds a randomly selected item from the home page to the cart
        and then checks if the product has been added to the cart"""

        browser.get(url)
        main_page = MainPage(browser)

        product_title, cart_product_title, product_price, cart_product_price = main_page.add_random_product_into_cart(wait)

        assert product_title == cart_product_title
        assert product_price == cart_product_price


# def test_add_product_into_cart(browser, url):
#     """This test adds a randomly selected item
#     from the home page to the cart and then the test
#     check if the product has been added to the cart"""
#
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#
#     # Собираем полный список всех товаров на главной странице
#     product_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
#     number = random.randint(0, len(product_list) - 3)
#     # -3, так как 3 и 4 товар содержат баг в Add to cart - происходит переход на страницу товара
#
#     # Выбираем случайный товар из имеющихся
#     random_product = wait.until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]
#
#     # Сохраняем название случайно выбранного товара и его цену в переменные
#     product_title = random_product.find_element(By.TAG_NAME, "h4").text
#     product_price = random_product.find_element(
#         By.CSS_SELECTOR, "p.price"
#     ).text.splitlines()[0]  # Строка содержит доп. символы и имеет вид '$123.20\nEx Tax: $101.00', поэтому делаем split
#
#     # Добавляем выбранный товар в корзину кликом по кнопке Add to cart
#     random_product.find_element(By.CSS_SELECTOR, "span.hidden-md").click()
#
#     # Переходим в корзину
#     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[id='cart-total']"))).click()
#     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa-shopping-cart"))).click()
#
#     # Проверяем соответствие добавленного в корзину товара
#     cart_product_title = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"))).text
#     cart_product_price = wait.until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[5]"))).text
#
#     assert product_title == cart_product_title
#     assert product_price == cart_product_price
