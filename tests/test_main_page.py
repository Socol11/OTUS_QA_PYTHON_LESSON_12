import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_presence_of_a_slider(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slideshow")))
    except TimeoutException:
        raise AssertionError(f"Слайдер отсутствует на странице")


def test_presence_of_slider_pagination(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-pagination")))
    except TimeoutException:
        raise AssertionError(f"Пагинация слайдера отсутствует на странице")


def test_presence_of_product_layout(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    assert len(product_layout_list) > 0


def test_presence_of_buttons_in_product_layout(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    number = random.randint(0, len(product_layout_list)-1)
    # Выбираем случайный элемент из имеющихся
    random_product_layout = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]
    try:
        random_product_layout.find_element(By.CSS_SELECTOR, ".button-group")
    except TimeoutException:
        raise AssertionError(f"Нет группы кнопок в product layout")


def test_presence_of_carousel(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".carousel")))
    except TimeoutException:
        raise AssertionError(f"Карусель отсутствует на странице")
