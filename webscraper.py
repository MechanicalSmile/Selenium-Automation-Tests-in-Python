from selenium import webdriver
from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from locators import Locator, ClassNameLocator, CSSLocator, IDLocator, LinkTextLocator, PartialLinkTextLocator, NameLocator, TagNameLocator, XPathLocator

class WebScraper:
    def __init__(self, driver_path):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=self.options)
        self.locator = Locator(self.driver)
        self.locator.set_locators(ClassNameLocator(self.driver), CSSLocator(self.driver), IDLocator(self.driver), LinkTextLocator(self.driver), PartialLinkTextLocator(self.driver), NameLocator(self.driver), TagNameLocator(self.driver), XPathLocator(self.driver))
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()

    def navigate_to(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def extract_text(self, element):
        try:
            # Try getting text directly
            text_content = element.text
            if text_content:
                return text_content
        except Exception as e:
            print(f"Error with text: {e}")

        try:
            # Try getting innerText
            inner_text = element.get_attribute("innerText")
            if inner_text:
                return inner_text
        except Exception as e:
            print(f"Error with innerText: {e}")

        try:
            # Try getting textContent
            text_content = element.get_attribute("textContent")
            if text_content:
                return text_content
        except Exception as e:
            print(f"Error with textContent: {e}")

        try:
            # Try getting innerHTML
            inner_html = element.get_attribute("innerHTML")
            if inner_html:
                return inner_html
        except Exception as e:
            print(f"Error with innerHTML: {e}")

        # If all else fails, return an empty string or handle accordingly
        return ""

    def quit(self):
        self.driver.quit()