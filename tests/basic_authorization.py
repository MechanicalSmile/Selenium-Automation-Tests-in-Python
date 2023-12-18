from webscraper import WebScraper
from memory_profiler import profile
import time
import pyautogui

@profile
def basic_authorization():
    time.sleep(1)
    with WebScraper(driver_path='Original Python Projects\Learning_Selenium_With_Python\chromedriver.exe') as scraper:
        scraper.navigate_to('https://the-internet.herokuapp.com/')

        scraper.locator.xpath.find_element('//*[@id="content"]/ul/li[3]/a', True)
        
        username = "admin"
        password = "admin"
        pyautogui.write(username)
        pyautogui.press('tab')  # Move to the password field if needed
        pyautogui.write(password)
        pyautogui.press('enter')  # Submit the form
        success = scraper.locator.xpath.find_element('//*[@id="content"]/div/p', False)
        success_text = success.text
        expected_text = "Congratulations! You must have the proper credentials."
        assert expected_text in success_text, f"Expected text not found. Expected: '{expected_text}', Actual: '{success_text}'"
    return True  # Indicate success