import requests
from parsel import Selector


def fetch(url):
    """Recebe uma URL;
    Faz uma requisição HTTP GET para esta URL;
    Caso requisição bem sucedida: retorna com status 200 o conteúdo de texto;
    Caso resposta com status diferente de 200: retorna None;
    Caso Timeout de 3 segundos: retorna None.
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


# Requisição do tipo GET
url = 'https://perguntarnaoofende.com/?s=roteiro'
text_content = fetch(url)


selector = Selector(text=text_content)


# Pegar artigos da primeira pagina
first_page = selector.css(".entry-title.h2 a::attr(href)").getall()
print(first_page)
