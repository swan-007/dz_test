import requests
from settings import TOKEN
Token = TOKEN

base_host = 'https://cloud-api.yandex.net/'

headers = {'Content-Type': 'application/json',
           'Authorization': f'OAuth {Token}'}

def put_path(base_host, headers):
    uri = 'v1/disk/resources?'
    path = "path=new"
    request_url = base_host + uri + path
    response = requests.put(request_url, headers=headers)
    return str(response)


def check_path(base_host, headers):
    uri = 'v1/disk/resources?'
    path = "path=788"
    request_url = base_host + uri + path
    response = ((requests.get(request_url, headers= headers)))
    return str(response)


