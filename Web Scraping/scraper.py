import os
import time
import pandas as pd
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

import chromedriver_autoinstaller

# Automatically install the right ChromeDriver version
chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(options=chrome_options)
def setup_driver():
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
return driver

def fetch_html(driver, url):
driver.get(url)
time.sleep(2)
return driver.page_source

def parse_html(html, url):
try:
soup = BeautifulSoup(html, 'html.parser')
data = []

links = soup.find_all('a')
for link in links:
href = link.get('href')
text = link.text.strip()
data.append({'url': url, 'type': 'link', 'href': href, 'text': text})

images = soup.find_all('img')
for img in images:
src = img.get('src')
alt = img.get('alt', '').strip()
data.append({'url': url, 'type': 'image', 'src': src, 'alt': alt})

counts = {
'url': url,
'total_links': len(links),
'total_images': len(images),
}
return data, counts
except Exception as e:
print(f"Error parsing HTML for {url}: {e}")
return None, None

def scrape_website(url):
try:
driver = setup_driver()
html = fetch_html(driver, url)
data, counts = parse_html(html, url)
driver.quit()
return data, counts
except Exception as e:
print(f"Error scraping {url}: {e}")
return None, None

def scrape_multiple_websites(urls):
all_data = []
all_counts = []
with ThreadPoolExecutor(max_workers=5) as executor:
results = executor.map(scrape_website, urls)
for data, counts in results:
if data:
all_data.extend(data)
if counts:
all_counts.append(counts)
return all_data, all_counts

if __name__ == "__main__":
urls = [
'https://www.britannica.com/place/Andhra-Pradesh',
'https://www.flipkart.com/search?q=mobile+phones+under+10000'
]

data, counts = scrape_multiple_websites(urls)

scraped_data_file = os.path.abspath('scraped_data.xlsx')
summary_counts_file = os.path.abspath('summary_counts.xlsx')

if data:
data_df = pd.DataFrame(data)
data_df.to_excel(scraped_data_file, index=False)

if counts:
counts_df = pd.DataFrame(counts)
counts_df.to_excel(summary_counts_file, index=False)

print(f"Scraping process completed. Data saved to:\n 1️⃣ {scraped_data_file}\n 2️⃣ {summary_counts_file}")
webbrowser.open(scraped_data_file)
