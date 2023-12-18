from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

class Locator:
    def __init__(self, driver):
        self.driver = driver

    def set_locators(self, ClassNameLocator, CSSLocator, IDLocator, LinkTextLocator, PartialLinkTextLocator, NameLocator, TagNameLocator, XPathLocator):
        self.class_name = ClassNameLocator
        self.css = CSSLocator
        self.id = IDLocator
        self.link_text = LinkTextLocator
        self.partial_link = PartialLinkTextLocator
        self.name = NameLocator
        self.tag_name = TagNameLocator
        self.xpath = XPathLocator
        
    def find_element(self, strategy, value, should_click):
        """
        Find an element based on strategy with should_click to click.

        Args:
            strategy: the locator strategy that should be used.
            Strategies include: By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT , By.PARTIAL_LINK_TEXT, By.NAME, By.TAG_NAME, By.XPATH
            value: the xpath of the element you wish to find
            should_click: True or False to determine if element should be clicked

        Returns:
            element
        """
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((strategy, value))
            )
            if should_click is True:
                if element:
                    element.click()
                    return element
            else:
                return element
        except TimeoutException:
            print(f"Element does not exist.")
        except Exception as e:
            print(f"An error occurred while finding element: {e}")
            return None
        
    def find_elements(self, strategy, value, should_click):
        """
        Find an element based on strategy with should_click to click.

        Args:
            strategy: the locator strategy that should be used.
            Strategies include: By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT , By.PARTIAL_LINK_TEXT, By.NAME, By.TAG_NAME, By.XPATH
            value: the xpath of the element you wish to find
            should_click: True or False to determine if element should be clicked

        Returns:
            element
        """
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_all_elements_located((strategy, value))
            )
            if should_click is True:
                if element:
                    element.click()
                    return element
            else:
                return element
        except TimeoutException:
            print(f"Element does not exist.")
        except Exception as e:
            print(f"An error occurred while finding element: {e}")
            return None

    def send_keys_to_element(self, strategy, value, keys):
        element = self.find_element(strategy, value, True)
        if element:
            try:
                element.send_keys(keys)
            except Exception as e:
                print(f"An error occurred while sending keys to element: {e}")

    def paste_text_to_element(self, strategy, value):
        """
        Paste text into an input element.

        Args:
            strategy: the locator strategy that should be used.
            value: the xpath of the element you wish to find
            text: the text to paste into the element
        """
        clipboard_text = pyperclip.paste()
        try:
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((strategy, value))
            )
            element.clear()  # Clear the existing text in the element
            element.send_keys(clipboard_text)
        except Exception as e:
            print(f"An error occurred while pasting text to element: {e}")
