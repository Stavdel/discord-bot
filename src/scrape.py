import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text

def normalize_url(url):
    parsed_url = urlparse(url)
    # Standardizing to a single scheme (https) and removing 'www.'
    scheme = 'https'
    netloc = parsed_url.netloc.replace('www.', '')
    path = parsed_url.path.rstrip('/')
    return f"{scheme}://{netloc}{path}"

def scrape(url, depth=1, current_depth=0, visited=None):
    if visited is None:
        visited = set()
    
    normalized_url = normalize_url(url)
    if normalized_url in visited or current_depth > depth:
        return ""
    
    visited.add(normalized_url)
    print(f"Scraping {normalized_url}...")

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        if response.status_code != 200:
            print(f"Failed to fetch {normalized_url}")
            return ""
    except requests.RequestException as e:
        print(f"Error fetching {normalized_url}: {e}")
        return ""

    # Convert the HTML to Markdown
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = False
    markdown_content = text_maker.handle(response.text)

    # Only proceed to scrape further if we are not at the maximum depth
    if current_depth < depth:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links[:5]:  # Limit the number of links processed to avoid too much recursion
            full_url = urljoin(url, link['href'])
            markdown_content += scrape(full_url, depth, current_depth + 1, visited)

    return markdown_content
