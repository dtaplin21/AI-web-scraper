from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching chrome browser...")

    # Fixing syntax issue by placing AUTH and SBR_WEBDRIVER on separate lines
    AUTH = 'brd-customer-hl_97f6e034-zone-ai_scraper:76q03ch4g3jf'
    SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')

    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)

        print('Waiting for captcha to be solved...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')

        html = driver.page_source
        return html  # Correct indentation inside the function

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_contetn(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]): 
        script_or_style.extract()  #look inside parsed content run a script or style and remove them

        cleaned_content = soup.get_text(separator="\n")
        cleaned_content = "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
        
        return cleaned_content
    

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length) #after you get the first 6000 char then it will go to the next 6000
    ]