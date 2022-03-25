import requests


def get_locaiton():
    url = 'https://ip-location5.p.rapidapi.com/get_geo_info'
    headers = {
        "X-RapidAPI-Host": "ip-location5.p.rapidapi.com",
        'X-RapidAPI-Key': '9fc02c456bmsh6626cffb86bc4a3p13dc03jsn476488b50c4e'
    }
    data = requests.get(url, headers=headers)
    print(data.json())


get_locaiton()
