import time

import pandas as pd

start = time.time()

currencies_old = pd.read_json('conversion_rates.json').transpose()
currencies_new = pd.read_json('http://www.floatrates.com/daily/mdl.json').transpose()

print(currencies_new)
print(currencies_old)

currencies_new = pd.concat([currencies_new] * 200)
currencies_old = pd.concat([currencies_old] * 200)

converion_diff = currencies_new['inverseRate'] - currencies_old['inverseRate']
print(converion_diff)

difference_from = currencies_old['date']
difference_to = currencies_new['date']

sorted = converion_diff.sort_values()

currencies_new['difference'] = converion_diff
currencies_new['difference_from'] = difference_from
currencies_new['difference_to'] = difference_to
print(currencies_new)
print(currencies_new)
currencies_new.to_excel('currencies_example.xlsx')
end = time.time()

print(end - start)
