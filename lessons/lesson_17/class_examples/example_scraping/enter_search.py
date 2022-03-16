from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import pandas

base_url = 'https://enter.online/search?query={}'

search_term = input('Product to search')

search_url = base_url.format(parse.quote(search_term))  # Setting the search term in the url

data = requests.get(search_url)
soup = BeautifulSoup(data.content)

product_list = soup.find('div', {'class': "product-list"})
products = product_list.find_all('div', {"class": "grid-item"})
results = []
classes_to_look_up = ['product-title',
                      'product-descr',
                      'price',
                      'price-new',
                      'price-old',
                      'discount', ]
for deal in products:
    data = dict()
    for _class in classes_to_look_up:
        try:
            data[_class] = deal.find('span', {"class": _class}).text.strip()
        except:
            data[_class] = None
    results.append(data)
dataFrame = pandas.DataFrame(results)
print(dataFrame)
