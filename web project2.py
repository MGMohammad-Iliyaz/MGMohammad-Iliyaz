import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Function to fetch the HTML content of a webpage
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        raise Exception(f"Page not found: {url}")
    elif response.status_code == 403:
        raise Exception(f"Access forbidden: {url}")
    else:
        raise Exception(f"Failed to fetch the webpage (status code {response.status_code}): {url}")

# Function to parse the HTML and extract data
def parse_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        data = []
        
        # Example: Extract all links and images from the webpage
        for link in soup.find_all('a'):
            href = link.get('href')
            text = link.text.strip()
            data.append({'type': 'link', 'href': href, 'text': text})
        
        for img in soup.find_all('img'):
            src = img.get('src')
            alt = img.get('alt', '').strip()
            data.append({'type': 'image', 'src': src, 'alt': alt})
        
        return data
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return None

# Function to scrape a single website
def scrape_website(url):
    try:
        html = fetch_html(url)
        data = parse_html(html)
        return data
    except Exception as e:
        print(e)
        return None

# Main function to scrape multiple websites concurrently
def scrape_multiple_websites(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(scrape_website, urls)
    all_data = []
    for result in results:
        if result:
            all_data.extend(result)
    # Print the collected data instead of saving it
    for item in all_data:
        print(item)

if __name__ == "__main__":
    urls = ['https://www.britannica.com/place/Andhra-Pradesh', 'https://www.britannica.com/summary/Mahatma-Gandhi'] 
    data = scrape_multiple_websites(urls)
    
    # Print the collected data
    if data:
        for item in data:
            print(item)
    print("Scraping process completed.")