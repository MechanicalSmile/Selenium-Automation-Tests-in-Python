from webscraper import WebScraper
from memory_profiler import profile


@profile
def add_remove_elements():
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