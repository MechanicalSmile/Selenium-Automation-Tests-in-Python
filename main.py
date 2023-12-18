import requests
import time
import concurrent.futures
import pyautogui
from webscraper import WebScraper
from memory_profiler import profile


@profile
def sign_up_for_newsletter():
    with WebScraper(driver_path='Original Python Projects\Learning_Selenium_With_Python\chromedriver.exe') as scraper:
        scraper.navigate_to('https://www.fakemailgenerator.com/')
        scraper.maximize_window()

        scraper.locator.xpath.find_element('/html/body/div[1]/div[1]/div[1]/div[3]/div', True)

        scraper.navigate_to('https://mashable.com/')

        scraper.locator.xpath.find_element('/html/body/div[10]/div[2]/div/div/div[2]/div/div/button', True)
        scraper.locator.xpath.paste_text_to_element('/html/body/div[7]/div[1]/div[2]/form/input[1]')
        scraper.locator.xpath.find_element('/html/body/div[7]/div[1]/div[2]/form/button', True)

        successful_registration_element = scraper.locator.xpath.find_element('/html/body/div[7]/div[3]/div', False)
        registration_text = successful_registration_element.get_attribute('textContent')
        expected_text = 'Thanks for signing up. See you at your inbox!'

        assert expected_text in registration_text, f"Expected text not found. Expected: '{expected_text}', Actual: '{registration_text}'"
    return True  # Indicate success

@profile
def test2():
    with WebScraper(driver_path='Original Python Projects\Learning_Selenium_With_Python\chromedriver.exe') as scraper:
        scraper.navigate_to('https://the-internet.herokuapp.com/')

        scraper.locator.xpath.find_element('//*[@id="content"]/ul/li[2]/a', True)

        while True:
            delete_element = scraper.locator.xpath.find_element('//*[@id="elements"]/button', False)
            if delete_element:
                scraper.locator.xpath.find_element('//*[@id="elements"]/button', True)
                break
            else:
                add_element = scraper.locator.xpath.find_element('//*[@id="content"]/div/button', False)
                if add_element:
                    scraper.locator.xpath.find_element('//*[@id="content"]/div/button', True)
    return True  # Indicate success

@profile
def test3():
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

@profile
def test4():
    with WebScraper(driver_path='Original Python Projects\Learning_Selenium_With_Python\chromedriver.exe') as scraper:
        scraper.navigate_to('https://the-internet.herokuapp.com/')

        scraper.locator.xpath.find_element('//*[@id="content"]/ul/li[4]/a', True)
        images = scraper.locator.tag_name.find_elements('img', False)
        broken_images = []
        for image in images:
            response = requests.get(image.get_attribute('src'))
            if response.status_code != 200:
                broken_images.append(f"Broken image: {image.get_attribute('outerHTML')}")
        if broken_images:
            return broken_images
        else:
            return True


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(sign_up_for_newsletter), executor.submit(test2), executor.submit(test3), executor.submit(test4)]

        # Wait for both scripts to finish
        concurrent.futures.wait(futures)

        # Check the results and print success messages
        for future, test_name in zip(futures, ["Test1", "Test2", "Test3", "Test4"]):
            try:
                result = future.result()
                assert result is True
                print(f"{test_name} is successful with no errors")
            except AssertionError as e:
                if str(e):
                    print(f"{test_name} failed. Error Details: {str(e)}")
                else:
                    print(f"{test_name} failed: {result}")