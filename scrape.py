import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import service

def scrape_website(website):
    print("Launching Chrome Browser...")


    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service(chrome_driver_path), options=options)


    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source

        return html
    finally:
        driver.quit()

# click buttons and interact with the page 
# control web broweser
# interact with text widgets