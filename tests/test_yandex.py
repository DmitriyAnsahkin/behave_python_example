import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.yandex_page import MainYandexPage, SearchPage, Pictures


def test_yandex():

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(
        executable_path='/Users/dmitrijanaskin/PycharmProjects/SeleniumTasks/webdrivers/chromedriver',
        chrome_options=chrome_options
    )


    driver.get('https://yandex.ru')

    # Заполнить поле поиска
    page = MainYandexPage(driver=driver)                         # 1
    page.fill_input(xpath=page.INPUT_SEARCH, value='Cessna')

    # Кликнуть кнопку найти
    page.click_button_by_name(button_name='Найти')

    page = SearchPage(driver=driver)                                         # 3

    page.click_button_by_name(button_name='Картинки')

    page = Pictures(driver=driver)

    page.click_button_by_name(button_name='Видео')

    print()
