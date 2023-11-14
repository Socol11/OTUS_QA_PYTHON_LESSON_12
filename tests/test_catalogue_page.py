import random
import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_enter_random_catalogue_page_via_navbar(browser, url):
    """Проверяем возможность попасть в каталог через меню"""

    browser.get(url)
    wait = WebDriverWait(browser, 5)

    # Get the list of li elements of menu
    ul_navbar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-nav")))
    li_elements = ul_navbar.find_elements(By.XPATH, './*')

    # Choose the random li element
    number = random.randint(0, len(li_elements)-1)
    li_element = li_elements[number]
    menu_link_title = li_element.text    # Save for assertion below

    # Move the cursor to li_element
    ActionChains(browser).move_to_element(li_element).perform()

    time.sleep(1)
    # Click on the appropriate link
    try:
        li_element.find_element(By.CLASS_NAME, 'see-all').click()
    except NoSuchElementException:
        li_element.click()

    # Check the h2 header of opened catalogue page
    assert wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h2'))).text == menu_link_title


def test_presence_of_catalogue_menu(browser, url):
    browser.get(url + "/desktops")
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".list-group")))
    except TimeoutException:
        raise AssertionError(f"Меню каталога отсутствует на странице!")


def test_presence_of_category_img_thumbnail(browser, url):
    browser.get(url + "/mp3-players")
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".img-thumbnail")))
    except TimeoutException:
        raise AssertionError(f"Миниатюра категории отсутствует на странице!")


def test_presence_of_button_view(browser, url):
    browser.get(url + "/smartphone")
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-group")))
    except TimeoutException:
        raise AssertionError(f"Кнопки переключения режима отображения товаров отсутствуют на странице!")


def test_presence_of_sort_by_dropdown(browser, url):
    browser.get(url + "/laptop-notebook")
    wait = WebDriverWait(browser, 5)
    assert (wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[3]/div/label"))).text
            == "Sort By:")


def test_presence_of_limit_dropdown(browser, url):
    browser.get(url + "/tablet")
    wait = WebDriverWait(browser, 5)
    assert (wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div[4]/div/label"))).text
            == "Show:")
