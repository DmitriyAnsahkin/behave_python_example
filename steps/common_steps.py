import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.yandex_page import MainYandexPage


@given('Открыть сайт "{url}"')
def step(context, url):

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(
        executable_path='/Users/dmitrijanaskin/PycharmProjects/SeleniumTasks/webdrivers/chromedriver',
        chrome_options=chrome_options
    )
    context.driver.get(url)

    context.page = MainYandexPage(driver=context.driver)
    time.sleep(2)


