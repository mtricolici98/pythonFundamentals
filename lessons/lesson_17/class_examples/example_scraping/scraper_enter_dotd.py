from bs4 import BeautifulSoup
import requests
import pandas

data = requests.get('https://enter.online/')
soup = BeautifulSoup(data.content)

deals_of_the_day = soup.find('div', {"class": "deal-of-the-day-slider"})
deals_list = deals_of_the_day.find('ul', {"class": "uk-slider-items"}).find_all('li')
deals = []
for deal in deals_list:
    data = dict(
        product=deal.find('span', {"class": 'product-title'}).text.strip(),
        new_price=deal.find('span', {"class": 'price-new'}).text.strip(),
        old_price=deal.find('span', {"class": 'price-old'}).text.strip(),
        discount=deal.find('span', {"class": 'discount'}).text.strip(),
    )
    data_clean = dict(
        product=data['product'],
        new_price=data['new_price'].replace(' ', ''),
        old_price=data['old_price'].replace(' ', ''),
        discount=data['discount'].replace(' ', ''),
    )
    deals.append(data_clean)
deals_df = pandas.DataFrame(deals)
print(deals_df)
