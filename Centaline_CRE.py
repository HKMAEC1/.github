from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, time as dt_time
import time as sys_time

#set webdriver
chrome_options = webdriver.chrome.options.Options()

prefs = {
'download.extensions_to_open': 'xml',
'safebrowsing.enabled': True
}
## Uncomment the below to let the program to run in background
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
options.add_argument("start-maximized")
options.add_argument("--headless")
# options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def scrape_data():
    # Retail
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/lease/retail/'
    driver.get(url)
    retail_lease = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/sale/retail/'
    driver.get(url)
    retail_sales = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    # Office
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/lease/office/'
    driver.get(url)
    office_lease = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/sale/office/'
    driver.get(url)
    office_sales = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    # Factory
    # Lease
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/lease/industrial/'
    driver.get(url)
    factory_lease = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    # Sales
    driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
    url = 'https://oir.centanet.com/sale/industrial/'
    driver.get(url)
    factory_sales = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[4]/div/div/div[1]/h1/span').text
    
    d = datetime.now()
    
    driver.quit()  # Quit the webdriver to release resources
    
    return [d, retail_sales, retail_lease, office_sales, office_lease, factory_sales, factory_lease]

# Scrape data
data = scrape_data()

# Load existing data from file
try:
    df = pd.read_excel("CRE.xlsx")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Retail Sales", "Retail lease", "Office Sales", "Office lease", "Industrial Sales", "Industrial lease"])

# Append new data to the dataframe
df = df.append(pd.Series(data, index=df.columns), ignore_index=True)

# Save dataframe to file
df.to_excel("CRE.xlsx", sheet_name="sheet1", index=False)

print("Data appended successfully.")
