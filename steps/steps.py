from behave import *

from pages.yandex_page import Pictures, SearchPage


@step('Нажать кнопку {button_name}')
def click_by_name(context, button_name):
    page = context.page
    page.click_button_by_name(button_name=button_name)


@step('Заполнить поле поиска текстом {text_value}')
def fill_field(context, text_value):
    page = context.page
    page.fill_input(xpath=page.INPUT_SEARCH, value=text_value)
