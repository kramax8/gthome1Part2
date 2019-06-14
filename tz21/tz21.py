import requests
from bs4 import BeautifulSoup
# import string
headers = {'accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/75.0.3770.80 Chrome/75.0.3770.80 Safari/537.36'}

def get_html(url):
   r = requests.get(url)
   return r.text

def get_all_links(html):
   soup = BeautifulSoup(html,'html.parser')
   divs = soup.find('div',class_='mr-3').find_all('article',class_='listing-item')
   titles = []
   links = []
  
   for div in divs:
       a = div.find('a').get('href')
       title = div.find('a').text
       price = div.find('p', class_='listing-item-title').text
       ph_link = div.find('img', class_='listing-item-photo').get('src')
      #  import string
      #  price = string.replace(price,"&nbsp;", "")
       link = '\n' + '----------------------------------------------' + '\n'
       link += 'PHOTO==> ' + ph_link + '\n' + 'NAME==> ' + title + '\n'
       link += 'PRICE==> ' + price[1:] + '\n' + 'HREF==> ' + 'https://lalafo.kg' + a
       link += '\n' + '----------------------------------------------' + '\n'

       links.append(link)
   return links


def main():
   url = "https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony"
   all_links = get_all_links(get_html(url))
   for i in all_links:
       print(i)

if __name__ == '__main__':
   main()



















































































# import requests
# from bs4 import BeautifulSoup as bs

# headers = {'accept': '*/*',
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/75.0.3770.80 Chrome/75.0.3770.80 Safari/537.36'}

# base_url = 'https://hh.ru/search/vacancy?text=python&area=1'

# def hh_parse(base_url, headers):
#     session = requests.Session()
#     requests = session.get(base_url, headers=headers)
#     if requests.status_code == 200:
#         # soup = bs(requests.content, 'html.parser')
#         # div = soup.find_all('div', attrs={})
#         print('ok')
#     else:
#         print('error')

# hh_parse(base_url, headers)