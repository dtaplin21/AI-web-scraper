import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching Chrome Browser...")


    chrome_driver_path = "./chromedriver"         #allows to control chrome
    options = webdriver.ChromeOptions()   #how the chrome will oporate
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options) #setup driver


    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

# click buttons and interact with the page 
# control web broweser
# interact with text widgets