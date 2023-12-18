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