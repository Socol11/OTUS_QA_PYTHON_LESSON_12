from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_thumbnails_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.thumbnails")))
    except TimeoutException:
        raise AssertionError(f"Слайдер с продуктом отсутствует на странице!")


def test_h1_title_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        assert wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1"))).text == 'iPhone'
    except TimeoutException:
        raise AssertionError(f"Название продукта не соответствует требуемому!")


def test_brand_info_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        assert wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[1]/li[1]/a"))).text == 'Apple'
    except TimeoutException:
        raise AssertionError(f"Название бренда не соответствует требуемому!")


def test_price_info_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        assert wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[2]/li[1]/h2"))).text == '$123.20'
    except TimeoutException:
        raise AssertionError(f"Цена товара неверна!")


def test_input_quantity_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='quantity']")))
    except TimeoutException:
        raise AssertionError(f"Поле ввода количества товаров отсутствует!")


def test_add_to_cart_button_presence(browser, url):
    browser.get(url + '/iphone')
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
    except TimeoutException:
        raise AssertionError(f"Кнопка добавления в корзину отсутствует!")
