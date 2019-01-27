from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tld import get_tld
from termcolor import colored
import requests
import os
import lxml


forbidden_prefixes = ['#', 'tel:', 'mailto:']

def save_output(url, links):
    parse_host = get_tld(url, as_object=True)
    name = parse_host.domain

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    if not os.path.exists("outputs/" + name):
        os.makedirs("outputs/" + name)

    with open("outputs/" + name + "/" + name + "_links.txt", "w") as f:
        for link in links:
            f.write(link + "\n")

    print("File saved to outputs/" + name)


def add_link(url, maxdepth=1):
    
    links = []
    domain = url.split("//")[1]

    try:
        request = requests.get(url)
    except:
        print(colored("Host is unreachable!"))
    else:
        soup = BeautifulSoup(request.content, 'lxml')

        for tag_a in soup.find_all('a'):

            try:
                link = tag_a['href']
            except:
                print(colored("\nURLs not found", "red"))
                break

            if all(not link.startswith(prefix) for prefix in forbidden_prefixes):
                if link.startswith('/') and not link.startswith('//'):
                    link = url + link

                if urlparse(link).netloc == domain and link not in links:
                    links.append(link)

    if len(links) > 10:

        while True:
            ans = input("There are more than 10 links.\nSave to file(1) or show all(2)? [1/2] ")

            if ans == '1':
                save_output(url,links)
                break
            elif ans == '2':
                for link in links:
                    print(link)
                break
            else:
                print("Unknown variant\n")
