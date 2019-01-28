# -*- coding: utf-8 -*-

import requests
from termcolor import colored
from tld import get_tld
import os


def save_output(doc, name, encoding):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    if not os.path.exists("outputs/" + name):
        os.makedirs("outputs/" + name)

    with open("outputs/" + name + "/" + name + "_html.html", "w", encoding=encoding) as f:
        f.write(doc)

        print(colored("\nFile saved to outputs/" + name, "green"))


def get_html(host):
    parse_host = get_tld(host, as_object=True)
    name = parse_host.domain

    try:
        response = requests.get(host)
    except:
        print(colored("Host is unreachable!", "red"))

    try:
        doc = response.content.decode("utf-8", errors="ignore")
        encoding = "utf-8"
    except:
        doc = response.content.decode("cp1251", errors="ignore")
        encoding = "cp1251"
    finally:
        save_output(doc, name, encoding)
