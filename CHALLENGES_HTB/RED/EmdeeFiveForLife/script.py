import requests
import hashlib
from requests_html import HTMLSession

url = 'http://docker.hackthebox.eu:30698'
data = {
        'hash' : 'hash=4791b54ac8247e0bfa13ba94685b305f'
}

try:
    session = HTMLSession()
    response = session.post(url, data=data)
    element = response.html.xpath('/html/body/h3')
    text = element[0].text
    hash_object = hashlib.md5(text.encode())
    cifrado = hash_object.hexdigest()
    data = {
            'hash':cifrado
        }
    response = session.post(url, data=data)
    print(response.text)

except requests.exceptions.RequestException as e:
    print(e)
