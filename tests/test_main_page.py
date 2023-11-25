from page.MainPage import MainPage


class TestMainPage:

    def test_presence_of_a_slider(self, browser, url, wait=5):
        """This test checks if the slider is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_slider(wait)

    def test_presence_of_slider_pagination(self, browser, url, wait=5):
        """This test checks if the slider pagination element is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_slider_pagination(wait)

    def test_presence_of_product_layout(self, browser, url, wait=5):
        """This test checks if the block of products is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_product_layout(wait)

    def test_presence_of_carousel(self, browser, url, wait=5):
        """This test checks if the carousel of brands is present on the main page"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_carousel(wait)

    def test_presence_of_buttons_in_product_layout(self, browser, url, wait=5):
        """This test randomly checks if the group of buttons is present in a product layout"""
        browser.get(url)
        main_page = MainPage(browser)
        main_page.get_buttons_in_product_layout(wait)

# def test_presence_of_a_slider(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slideshow")))
#     except TimeoutException:
#         raise AssertionError(f"Слайдер отсутствует на странице")


# def test_presence_of_slider_pagination(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-pagination")))
#     except TimeoutException:
#         raise AssertionError(f"Пагинация слайдера отсутствует на странице")


# def test_presence_of_product_layout(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#     product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
#     assert len(product_layout_list) > 0


# def test_presence_of_buttons_in_product_layout(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#     product_layout_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
#     number = random.randint(0, len(product_layout_list)-1)
#     # Выбираем случайный элемент из имеющихся
#     random_product_layout = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))[number]
#     try:
#         random_product_layout.find_element(By.CSS_SELECTOR, ".button-group")
#     except TimeoutException:
#         raise AssertionError(f"Нет группы кнопок в product layout")


# def test_presence_of_carousel(browser, url):
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".carousel")))
#     except TimeoutException:
#         raise AssertionError(f"Карусель отсутствует на странице")
