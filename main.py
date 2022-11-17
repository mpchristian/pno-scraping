import requests
from parsel import Selector


# Functions
def fetch(url):
    """It recieves an URL;
    Requests with HTTP GET to this URL;
    Well secceded: returns with status 200 the text content
    If response has other status, returns None;
    If 3 secons Timeout, returns None.
    """

    try:
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; ' +
          'rv:55.0 Gecko/20100101 Firefox/55.0',
        }
        response = requests.get(
            url, headers=headers, timeout=3
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


def scrape_articles(html_content, css_selector):
    """It recieves a string with the HTML content and CSS selector;
    Scrapes the recieved contentand returns a list of the articles URLs;
    If no one article is found, returns ampty list
    """
    selector = Selector(text=html_content)
    urls = selector.css(css_selector).getall()
    return urls


# Execute
url = 'https://perguntarnaoofende.com/?s=roteiro'
text_content = fetch(url)
urls = scrape_articles(text_content, ".entry-title.h2 a::attr(href)")


print(urls)
