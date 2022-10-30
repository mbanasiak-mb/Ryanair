import json
import requests

from Consts import *


def get_json(url: str):
    r = requests.get(url)
    c = r.content
    j = json.loads(c)
    return j


def get_airports_org():
    URL = URL_ORG
    return get_json(URL)


def get_airports_dst(org: str):
    URL = URL_DST.replace(KW_ORG, org)
    return get_json(URL)


def get_dates(org: str, dst: str):
    URL = URL_DATE
    URL = URL.replace(KW_ORG, org)
    URL = URL.replace(KW_DST, dst)
    return get_json(URL)


def get_prices(org: str, dst: str, date: str):
    URL = URL_PRICE
    URL = URL.replace(KW_ORG, org)
    URL = URL.replace(KW_DST, dst)
    URL = URL.replace(KW_DATE, date)
    return get_json(URL)
