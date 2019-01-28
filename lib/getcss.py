# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from termcolor import colored
from tld import get_tld
import requests
import os
from urllib.request import urlretrieve


forbidden_prefixes = ['#', 'tel:', 'mailto:']


def save_output(name, links):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    if not os.path.exists("outputs/" + name):
        os.makedirs("outputs/" + name)

    if not os.path.exists("outputs/" + name + "/css/"):
        os.makedirs("outputs/" + name + "/css/")

    for link in range(len(links)):
        filename = links[link].rsplit('/', 1)[1]

        try:
            filename = filename.split("?")[0]
        except:
            pass

        path = "outputs/" + name + "/css/" + filename

        try:
            urlretrieve(links[link], path)
        except:
            print(colored("\nCSS file is unavailable", "red"))
        else:
            print(colored("File saved to outputs/" + name + "/css/" + filename, "green"))


def get_css(url):
    links = []

    parse_host = get_tld(url, as_object=True)
    name = parse_host.domain

    request = requests.get(url)

    soup = BeautifulSoup(request.content, 'lxml')

    for tag_link in soup.find_all('link'):

        if tag_link['rel'][0] == "stylesheet":
            links.append(tag_link['href'])

    save_output(name, links)
