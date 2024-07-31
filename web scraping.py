import requests
from bs4 import BeautifulSoup
# Function to fetch the HTML content of a webpage
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the webpage: {url}")

# Function to parse the HTML and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    # Example: Extract all links from the webpage
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text
        data.append({'href': href, 'text': text})
    return data

# Main function to scrape a website
def scrape_website(url):
    try:
        html = fetch_html(url)
        data = parse_html(html)
        return data
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    url = 'https://www.britannica.com/biography/Mahatma-Gandhi'  # Replace with the target website
    scraped_data = scrape_website(url)
    if scraped_data:
        for item in scraped_data:
            print(f"Text: {item['text']}, Link: {item['href']}")

