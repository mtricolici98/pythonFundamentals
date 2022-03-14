import requests

response = requests.get('http://google.com/')  # Sending a GET Request to google.com

print(response.content)  # Will print out the HTML code of the requested website
print(response.status_code)  # Will print out the HTTP Status of the response

for header, value in response.headers.items():  # Will print out the headers for the response
    print(header, value)
for cookie, value in response.cookies.items():  # Will print out the response cookies
    print(cookie, value)
with open('google.html', 'wb') as file:  # Opening file to write bytes
    file.write(response.content)

python_logo = requests.get('https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
with open('python_logo.png', 'wb') as file:  # Opening file to write bytes
    print(python_logo.headers.get('Content-type'))
    # image/png
    file.write(python_logo.content)
