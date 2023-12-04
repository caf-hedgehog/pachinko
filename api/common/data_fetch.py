import requests
from bs4 import BeautifulSoup
import re
from common.definitions import USERAGENT


@staticmethod
def data_fetch(url):
    headers = {"User-Agent": USERAGENT}
    html = requests.get(url, headers=headers)

    bs = BeautifulSoup(html.content, "html.parser")
    print(bs)
    return bs
