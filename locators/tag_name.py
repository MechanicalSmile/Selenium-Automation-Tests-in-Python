from selenium.webdriver.common.by import By
from locators import *

class TagNameLocator(Locator):
    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, value, should_click):
        """
        Find an element based on Tag Name.

        Args:
            value: the tag name of the element you wish to find
            should_click: True or False to determine if element should be clicked

        Returns:
            a call to the super function with parameters
        """
        return super().find_element(By.TAG_NAME, value, should_click)
    
    def find_elements(self, value, should_click):
        return super().find_elements(By.TAG_NAME, value, should_click)
    
    def paste_text_to_element(self, value):
        return super().paste_text_to_element(By.TAG_NAME, value)