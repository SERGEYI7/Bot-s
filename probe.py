import urllib3
import requests

if requests.get('https://www.instagram.com/p/BbUPUwKn4dK/').text.rfind('src'):
    print(requests.get('https://www.instagram.com/p/BbUPUwKn4dK/').text)

# print(requests.get('http://vk.com').text.)