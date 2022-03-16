from bs4 import BeautifulSoup

file = open('example.html', 'r')

soup = BeautifulSoup(file)

welcome_message = soup.find('h1', {'id': 'welcome-message'})
print(welcome_message)
print(welcome_message.text)

main_info_bloc = soup.find('div', {'class': 'main-info'})
print(main_info_bloc)

paragraphs = main_info_bloc.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)

my_image = main_info_bloc.find('img').get('src')
import requests

img_file = requests.get(my_image)

with open('cat.jpg', 'wb') as f:
    f.write(img_file.content)
