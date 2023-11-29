import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):  # parser - встроенная фикстура pytest
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", help="base application url")


@pytest.fixture()  # Эта фикстура обеспечивает передачу url в терминале: pytest --url http://192.168.1.96:8081
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):  # request - встроенная фикстура pytest

    # Пишем опции выбора браузера
    headless = request.config.getoption("--headless")

    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "yandex":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = Service(
            executable_path=os.path.expanduser("~/Downloads/drivers/yandexdriver"))  # Чтобы не писать длинный путь
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "safari":
        driver = webdriver.Safari()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(f"The browser {browser_name} not supported!")

    if request.config.getoption("--maximize"):
        driver.maximize_window()

    yield driver

    driver.quit()
