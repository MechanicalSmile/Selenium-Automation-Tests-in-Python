from selenium.webdriver.common.by import By
from locators import *

class XPathLocator(Locator):
    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, value, should_click):
        """
        Find an element based on Xpath.

        Args:
            value: the xpath of the element you wish to find
            should_click: True or False to determine if element should be clicked

        Returns:
            a call to the super function with parameters
        """
        return super().find_element(By.XPATH, value, should_click)
    
    def click_element(self, value):
        return super().click_element(By.XPATH, value)

    def paste_text_to_element(self, value):
        return super().paste_text_to_element(By.XPATH, value)