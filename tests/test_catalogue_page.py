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
