import data_diplom
import urls_diplom
import requests


def created_order(body):
    head = data_diplom.headers_api.copy()
    return requests.post(urls_diplom.URL_USER+urls_diplom.URL_API_CREATE_ORDER, headers=head, json=body)


def get_order(track):
    track = str(track)
    return requests.get(urls_diplom.URL_USER+urls_diplom.URL_API_GET_ORDER, params={'t': track})


