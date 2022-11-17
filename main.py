import requests
from parsel import Selector


# Requisição do tipo GET
url = 'https://perguntarnaoofende.com/?s=roteiro'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0 ' +
    'Gecko/20100101 Firefox/55.0',
}
response = requests.get(url, headers=headers)
selector = Selector(text=response.text)


# Pegar artigos da primeira pagina
first_page = selector.css(".entry-title.h2 a::attr(href)").getall()
print(first_page)
