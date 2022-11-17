import requests
from parsel import Selector
import os


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
    """It recieves a string with the HTML content of an article;
    get the infos as a dict with attributes:
      * title - title of article.
      * url - link of the article.
      * pdf_url - link of the pdf.
    """
    selector = Selector(text=html_content)
    title = selector.css(".entry-title::text").get().rstrip().rstrip()
    url = selector.css("head link[rel='canonical']::attr(href)").get()
    pdf_url = selector.css(".wp-block-button__link::attr(href)").get()

    data = {}
    data["title"] = title
    data["url"] = url
    data["pdf_url"] = pdf_url
    return data


def get_name_of_article(article, path):
    """It recieves an article dict;
    Returns the name of the file to be saved by
    converting the title from "Roteiro para culto doméstico – Salmo 140"
    to "roteiro_salmo_140.pdf"
    """
    splited_name = article["title"].lower().split("– ")
    name = splited_name[1].replace(" ", "_")
    file_name = path + "/roteiro_" + name + ".pdf"
    return file_name


def download(url, path):
    """It recieves the url of the pdf and the file_name to be saved;
    Downloads the file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; ' +
      'rv:55.0 Gecko/20100101 Firefox/55.0',
    }
    with open(
      path,
      "wb"
      ) as file:
        response = requests.get(url, headers=headers)
        file.write(response.content)
