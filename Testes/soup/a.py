import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
page = requests.get('https://www.google.com/search?q=dolar+hoje&rlz=1C1SQJL_pt-BRBR998BR998&oq=dola&aqs=chrome.1.69i57j0i271l3.3519j0j4&sourceid=chrome&ie=UTF-8&dlnr=1&sei=ykoSZKGROs6H5OUPg5KBoAk', headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
valor_dolar = soup.find_all('span', class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])

page2 = requests.get('https://www.google.com/search?q=hora&oq=hora&aqs=chrome..69i57j0i433i512j0i131i433i457i512j0i402i512j0i512j0i131i433i512j0i512j0i131i433i512j0i512l2.1378j0j1&sourceid=chrome&ie=UTF-8', headers = headers)
soup2 = BeautifulSoup(page2.content, 'html.parser')
Hora_agora = soup2.find_all('div', class_="gsrt vk_bk FzvWSb YwPhnf")[0]
print(Hora_agora.text)

#usando beautifulsoupe para buscar o valor do bitcoin para reais e printar no terminal

page3 = requests.get('https://www.google.com/search?q=bitcoin+reais&rlz=1C1SQJL_pt-BRBR998BR998&oq=bitcoin+reais&aqs=chrome..69i57j0i433i512j0i131i433i457i512j0i402i512j0i512j0i131i433i512j0i512j0i131i433i512j0i512j0i131i433i512j0i512l2.1378j0j1&sourceid=chrome&ie=UTF-8', headers = headers)
soup3 = BeautifulSoup(page3.content, 'html.parser')
valor_bitcoin = soup3.find_all('span', class_="pclqee")[0]
print(f'1 bitcoin vale {valor_bitcoin.text} reais.\n')

#buscar a data atual no google

page4 = requests.get('https://www.google.com/search?q=data&rlz=1C1SQJL_pt-BRBR998BR998&sxsrf=APwXEdcupV6LQAigM1YJ-8DRy9SGmmyOjw%3A1680127416747&ei=uLUkZO6JLYPM1sQP_teriAo&ved=0ahUKEwjuxeiukoL-AhUDppUCHf7rCqEQ4dUDCBA&uact=5&oq=data&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIHCAAQigUQQzIOCC4QgAQQsQMQxwEQ0QMyDQgAEIoFELEDEIMBEEMyBwgAEIoFEEMyBQgAEIAEMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIoFELEDEIMBOgoIABBHENYEELADOgoIABCKBRCwAxBDSgQIQRgAUMsFWMoNYPsSaAFwAXgAgAGDAYgBvwWSAQMwLjaYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp', headers = headers)
soup4 = BeautifulSoup(page4.content, 'html.parser')
data_atual = soup4.find_all('div', class_="vk_bk dDoNo FzvWSb")[0]
print(data_atual.text)

with open('bitcoin.txt', 'a') as arquivo:
    arquivo.write(f'\n _______________________________\n 1 bitcoin vale {valor_bitcoin.text} reais.\n')
    arquivo.write(data_atual.text)
    arquivo.write(f'\n {Hora_agora.text}')

##usando beautifulsoupe para buscar o valor do euro para reais e printar no terminal 

page5 = requests.get('https://www.google.com/search?q=valor+do+euro&rlz=1C1SQJL_pt-BRBR998BR998&sxsrf=APwXEdcupV6LQAigM1YJ-8DRy9SGmmyOjw%3A1680127416747&ei=uLUkZO6JLYPM1sQP_teriAo&ved=0ahUKEwjuxeiukoL-AhUDppUCHf7rCqEQ4dUDCBA&uact=5&oq=valor+do+euro&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIECCMQJzIHCAAQigUQQzIOCC4QgAQQsQMQxwEQ0QMyDQgAEIoFELEDEIMBEEMyBwgAEIoFEEMyBQgAEIAEMgsIABCABBCxAxCDATIgQIQRgAUMsFWMoNYPsSaAFwAXgAgAGDAYgBvwWSAQMwLjaYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp', headers = headers) 
soup5 = BeautifulSoup(page5.content, 'html.parser')
data_atual = soup5.find_all('div', class_="dDoNo ikb4Bb gsrt")[0]
print(data_atual.text)












