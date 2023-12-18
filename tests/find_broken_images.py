from webscraper import WebScraper
from memory_profiler import profile
import requests

@profile
def find_broken_images():
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