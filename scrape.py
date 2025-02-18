import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By


def scrape_website(website):
   print("Launching chrome browser...")
   
   chrome_driver_path = "./chromedriver"
   options = webdriver.ChromeOptions() #if you want to ignore images or anything like that
   driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
   
   try:
      driver.get(website)
      print("Page loaded...")
      html = driver.page_source
      time.sleep(10)

      return html
   finally:
      driver.quit()










AUTH = 'brd-customer-hl_97f6e034-zone-ai_scraper:76q03ch4g3jf'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'
def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get('https://example.com')

        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
           'cmd': 'Captcha.waitForSolve',
           'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        
        
        html = driver.page_source
        print(html)
if __name__ == '__main__':
  main()