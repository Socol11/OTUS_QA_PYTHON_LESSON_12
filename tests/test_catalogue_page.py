from page.CataloguePage import CataloguePage


class TestCataloguePage:
    """Тестируем разные страницы каталога товаров"""

    WAIT = 5
    DESKTOPS_PAGE = "/desktops"
    MP3_PAGE = "/mp3-players"
    SMARTPHONE_PAGE = "/smartphone"
    LAPTOP_PAGE = "/laptop-notebook"
    TABLET_PAGE = "/tablet"

    def test_enter_random_catalogue_page_via_navbar(self, browser, url, wait=5):
        """Проверяем возможность попасть в каталог через рандомно выбранный элемент меню"""
        browser.get(url)
        catalogue_page = CataloguePage(browser)
        catalogue_h2_tag, li_element_text = catalogue_page.get_navbar_random_element(browser, wait)
        assert catalogue_h2_tag.text == li_element_text

    def test_presence_of_catalogue_menu(self, browser, url, wait=5):
        """This test checks if the side catalogue menu is present on the /desktops page"""
        browser.get(url + self.DESKTOPS_PAGE)
        catalogue_page = CataloguePage(browser)
        catalogue_page.get_catalogue_menu(wait)

    def test_presence_of_category_img_thumbnail(self, browser, url, wait=WAIT):
        """This test checks if the img thumbnail of the category is present on the /mp3-players page"""
        browser.get(url + self.MP3_PAGE)
        catalogue_page = CataloguePage(browser)
        catalogue_page.get_category_img_thumbnail(wait)

    def test_presence_of_display_mode_button(self, browser, url, wait=WAIT):
        """This test checks if the display mode buttons of the category are present on the /smartphone page"""
        browser.get(url + self.SMARTPHONE_PAGE)
        catalogue_page = CataloguePage(browser)
        catalogue_page.get_display_mode_button(wait)

    def test_presence_of_sort_by_dropdown(self, browser, url, wait=WAIT):
        """This test checks if the sort_by_dropdown element is present on the /laptop-notebook page"""
        browser.get(url + self.LAPTOP_PAGE)
        catalogue_page = CataloguePage(browser)
        assert catalogue_page.get_sort_by_dropdown(wait).text == "Sort By:"

    def test_presence_of_show_limit_dropdown(self, browser, url, wait=WAIT):
        """This test checks if the show limit dropdown element is present on the /tablet page"""
        browser.get(url + self.TABLET_PAGE)
        catalogue_page = CataloguePage(browser)
        assert catalogue_page.get_limit_dropdown(wait).text == "Show:"

# def test_enter_random_catalogue_page_via_navbar(browser, url):
#     """Проверяем возможность попасть в каталог через меню"""
#
#     browser.get(url)
#     wait = WebDriverWait(browser, 5)
#
#     # Get the list of li elements of menu
#     ul_navbar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-nav")))
#     li_elements = ul_navbar.find_elements(By.XPATH, './*')
#
#     # Choose the random li element
#     number = random.randint(0, len(li_elements)-1)
#     li_element = li_elements[number]
#     menu_link_title = li_element.text    # Save for assertion below
#
#     # Move the cursor to li_element
#     ActionChains(browser).move_to_element(li_element).perform()
#
#     time.sleep(1)
#     # Click on the appropriate link
#     try:
#         li_element.find_element(By.CLASS_NAME, 'see-all').click()
#     except NoSuchElementException:
#         li_element.click()
#
#     # Check the h2 header of opened catalogue page
#     assert wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h2'))).text == menu_link_title


# def test_presence_of_catalogue_menu(browser, url):
#     browser.get(url + "/desktops")
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-group")))
#     except TimeoutException:
#         raise AssertionError(f"Меню каталога отсутствует на странице!")


# def test_presence_of_category_img_thumbnail(browser, url):
#     browser.get(url + "/mp3-players")
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".img-thumbnail")))
#     except TimeoutException:
#         raise AssertionError(f"Миниатюра категории отсутствует на странице!")


# def test_presence_of_button_view(browser, url):
#     browser.get(url + "/smartphone")
#     wait = WebDriverWait(browser, 5)
#     try:
#         wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-group")))
#     except TimeoutException:
#         raise AssertionError(f"Кнопки переключения режима отображения товаров отсутствуют на странице!")


# def test_presence_of_sort_by_dropdown(browser, url):
#     browser.get(url + "/laptop-notebook")
#     wait = WebDriverWait(browser, 5)
#     assert (wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[3]/div/label"))).text
#             == "Sort By:")


# def test_presence_of_limit_dropdown(browser, url):
#     browser.get(url + "/tablet")
#     wait = WebDriverWait(browser, 5)
#     assert (wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[4]/div/label"))).text
#             == "Show:")
