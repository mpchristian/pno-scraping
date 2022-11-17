import requests


# Requisição do tipo GET
url = 'https://perguntarnaoofende.com/?s=roteiro'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text)