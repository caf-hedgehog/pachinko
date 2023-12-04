import requests
from bs4 import BeautifulSoup
import re
from common.definitions import USERAGENT
import bs4


@staticmethod
def get_html_data(url) -> bs4.BeautifulSoup:
    headers = {"User-Agent": USERAGENT}
    html = requests.get(url, headers=headers)

    bs = BeautifulSoup(html.content, "html.parser")
    return bs
