# Multi-Site Web Scraper

This Python project scrapes multiple websites concurrently to extract all links and images using Selenium and BeautifulSoup.

## Features
- Headless browser scraping using Selenium
- Parses HTML for all <a> and <img> tags
- Saves detailed data and summary counts to Excel files
- Multi-threaded scraping for speed

## Setup

### Requirements
Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using:

```bash
python scraper.py
```

## Output
- `scraped_data.xlsx` – contains all links and images from the sites
- `summary_counts.xlsx` – shows count of links and images per site

## Dataset
Websites used for scraping (you can modify in `scraper.py`):

```txt
https://www.britannica.com/place/Andhra-Pradesh
https://www.flipkart.com/search?q=mobile+phones+under+10000
```
