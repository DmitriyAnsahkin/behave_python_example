from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, xpath: str):
        """Метод получения вэб элемента по xpath

        Args:
            xpath: xpath

        Returns:
            element: вэб-элемент
        """
        try:
            element = WebDriverWait(driver=self.driver, timeout=20).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            element = self.driver.find_element(By.XPATH, xpath)
        return element

    def wait_clickable_element(self, xpath: str):
        """

        """
        element = WebDriverWait(driver=self.driver, timeout=20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

        return element

    def click(self, xpath):
        element = self.get_element(xpath=xpath)
        element.click()

    def fill_input(self, xpath, value):
        """Метод заполняет поле

        Args:
            xpath: xpath
            value: значение которым заполняется

        Returns:

        """
        element = self.get_element(xpath=xpath)
        element.send_keys(value)

    def clear_input(self, xpath):

        element = self.get_element(xpath=xpath)
        element.clear()

    def element_hover(self, xpath):

        element = self.wait_clickable_element(xpath=xpath)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).click().perform()

    def click_button_by_name(self, button_name):
        xpath = self.BUTTON_BY_NAME.format(button_name=button_name)
        self.get_element(xpath=xpath)
        self.click(xpath=xpath)
