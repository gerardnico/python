import requests


def get_my_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']
