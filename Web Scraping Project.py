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

# Function to setup Selenium WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Function to fetch the HTML content of a webpage using Selenium
def fetch_html(driver, url):
    driver.get(url)
    time.sleep(2)  # Wait for the page to load (can be adjusted)
    return driver.page_source

# Function to parse HTML and extract links and images
def parse_html(html, url):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        data = []

        # Extract links
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            text = link.text.strip()
            data.append({'url': url, 'type': 'link', 'href': href, 'text': text})
        
        # Extract images
        images = soup.find_all('img')
        for img in images:
            src = img.get('src')
            alt = img.get('alt', '').strip()
            data.append({'url': url, 'type': 'image', 'src': src, 'alt': alt})
        
        # Summary of total links and images
        counts = {
            'url': url,
            'total_links': len(links),
            'total_images': len(images),
        }
        return data, counts
    except Exception as e:
        print(f"Error parsing HTML for {url}: {e}")
        return None, None

# Function to scrape a single website
def scrape_website(url):
    try:
        driver = setup_driver()  # Setup WebDriver
        html = fetch_html(driver, url)  # Fetch HTML
        data, counts = parse_html(html, url)
        driver.quit()  # Close WebDriver
        return data, counts
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, None

# Function to scrape multiple websites concurrently
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

# Main Execution
if __name__ == "__main__":
    urls = [
        'https://www.britannica.com/place/Andhra-Pradesh',
        'https://www.flipkart.com/search?q=mobile+phones+under+10000'
    ]

    # Scrape data
    data, counts = scrape_multiple_websites(urls)

    # Define file paths
    scraped_data_file = os.path.abspath('scraped_data.xlsx')
    summary_counts_file = os.path.abspath('summary_counts.xlsx')

    # Save detailed data to an Excel file
    if data:
        data_df = pd.DataFrame(data)
        data_df.to_excel(scraped_data_file, index=False)

    # Save summary counts to an Excel file
    if counts:
        counts_df = pd.DataFrame(counts)
        counts_df.to_excel(summary_counts_file, index=False)

    print(f"Scraping process completed. Data saved to:\n 1️⃣ {scraped_data_file}\n 2️⃣ {summary_counts_file}")

    # Open the Excel file automatically
    webbrowser.open(scraped_data_file)
