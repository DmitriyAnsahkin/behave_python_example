from pages.base_page import BasePage


class MainYandexPage(BasePage):
    BUTTON_BY_NAME = '//*[text()="{button_name}"]/ancestor::button'

    INPUT_SEARCH = '//input[@class="input__control input__input"]'
    CLEAR_SEARCH = '//input[@class="input__control"]'
    PIC_PUSH = '//span[text()="Видео"]' # тест

    # первая картинка по запросы
    FIRST_PICTURE = '(//a[contains(@href, ".jpg")])[1]'


class SearchPage(MainYandexPage):
    BUTTON_BY_NAME = '//*[text()="{button_name}"]'


class Pictures(MainYandexPage):
    BUTTON_BY_NAME = '//*[text()="{button_name}"]'


