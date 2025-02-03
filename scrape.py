import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching Chrome Browser...")


    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get('https://example.com')
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'brd-customer-hl_97f6e034-zone-ai_scraper:76q03ch4g3jf'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


if __name__ == '__main__':
  main()

# click buttons and interact with the page 
# control web broweser
# interact with text widgets