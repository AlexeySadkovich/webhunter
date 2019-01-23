import socket
import requests
from lxml import html


def get_title(url):
    response = requests.get(url)
    parsed = html.fromstring(response.text)
    title = parsed.xpath('//title/text()')

    return title[0]


def get_info(host_name, url):
    ip_adress = socket.gethostbyname(host_name)
    title = get_title(url)

    print("[IP] : " + str(ip_adress))
    print("[TITLE] : " + str(title))
