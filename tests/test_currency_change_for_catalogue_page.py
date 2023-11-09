import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_currency_change_for_catalogue_page(browser, url):
    browser.get(url + 'smartphone')
    wait = WebDriverWait(browser, 5)

    # Проверяем валюту по умолчанию
    # Собираем полный список всех товаров на главной странице
    product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    number = random.randint(0, len(product_layout_list) - 1)

    # Выбираем случайный товар из имеющихся
    random_product_layout = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]

    # Сохраняем символ валюты случайно выбранного товара в переменную
    product_currency_symbol = random_product_layout.find_element(By.CSS_SELECTOR, "p.price").text[0]

    assert product_currency_symbol == "$"

    # Меняем валюту на EUR
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.dropdown-toggle"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.currency-select[name='EUR']"))).click()

    # Проверяем валюту после её смены
    # Собираем полный список всех товаров на главной странице
    product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    number = random.randint(0, len(product_layout_list) - 1)

    # Выбираем случайный товар из имеющихся
    random_product_layout = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]

    # Сохраняем символ валюты случайно выбранного товара в переменную
    product_currency_symbol = random_product_layout.find_element(By.CSS_SELECTOR, "p.price").text.splitlines()[0][-1]

    assert product_currency_symbol == "€"
