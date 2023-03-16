import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
page = requests.get('https://www.google.com/search?q=dolar+hoje&rlz=1C1SQJL_pt-BRBR998BR998&oq=dola&aqs=chrome.1.69i57j0i271l3.3519j0j4&sourceid=chrome&ie=UTF-8&dlnr=1&sei=ykoSZKGROs6H5OUPg5KBoAk', headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
valor_dolar = soup.find_all('span', class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])