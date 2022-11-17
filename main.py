import requests
from parsel import Selector
# import urllib.request


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
    Scrapes the recieved content and returns a list of the articles URLs;
    If no one article is found, returns ampty list
    """
    selector = Selector(text=html_content)
    urls = selector.css(css_selector).getall()
    return urls


def scrape_next_page_link(html_content, css_selector):
    """It recieves a string with the HTML content and CSS selector;
    Scrapes the recieved content and returns the URL of the next page;
    If the link is not found, returns None
    """
    selector = Selector(text=html_content)
    url = selector.css(css_selector).get()
    return url


def scrape_article(html_content):
    """Recebe uma string contendo o conteúdo HTML da página de uma notícia;
    busca as informações das notícias e preenche um dicionário com os atributos
        * url - link para acesso da notícia.
    """
    selector = Selector(text=html_content)
    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().rstrip()
    pdf_url = selector.css(".wp-block-button__link::attr(href)").get()

    # ---------- comments_count
    comments_count = (
        selector.css(".pk-share-buttons-count.cs-font-primary::text").get()
        or "0"
    )
    comments_count = [int(s) for s in comments_count.split() if s.isdigit()]
    # -----------

    data = {}
    data["url"] = url
    data["title"] = title
    data["pdf_url"] = pdf_url
    return data


# Execute
url = 'https://perguntarnaoofende.com/?s=roteiro'
text_content = fetch(url)

urls = scrape_articles(
  text_content,
  ".entry-title.h2 a::attr(href)")

# next_page_link = scrape_next_page_link(
#   text_content,
#   "a.next.page-numbers::attr(href)")

article = scrape_article(fetch(urls[0]))
print(article)
