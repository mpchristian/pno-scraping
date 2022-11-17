# pno-scraping
Web scraping of www.perguntarnaoofende.com

## Cria e ativa ambiente virtual
python3 -m venv .venv && source .venv/bin/activate

## Instala biblioteca para fazer requisições
python3 -m pip install requests

## Instala lint
pip install flake8

## Instala biblioteca parsel para extrair dados de requisição
python3 -m pip install parsel

## instala dotenv
pip install python-dotenv

## Executar localmente
Em .env_example, defina o caminho dos arquivos a serem baixados em PATH_FILE e a quantidade dos arquivos em AMOUNT
Depois renomeie o arquivo para .env
Execute localmente com:

python3 main.py