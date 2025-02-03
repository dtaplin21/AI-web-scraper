from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
import time

def scrape_website(website):
    print("Launching Chrome Browser...")


    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)

        print('waiting for capcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
           'cmmd': 'Captcha.waitForSolve',
           'params': {'detectTimeout': 10000},
        })
        print('Capcha solve status:', solve_res['value'['status']])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html


AUTH = 'brd-customer-hl_97f6e034-zone-ai_scraper:76q03ch4g3jf'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


if __name__ == '__main__':
  main()

# click buttons and interact with the page 
# control web broweser
# interact with text widgets