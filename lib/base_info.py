import socket
import requests
from termcolor import colored
from lxml import html


def get_title(url):
	response = requests.get(url)
	parsed = html.fromstring(response.text)
	title = parsed.xpath('//title/text()')

	return title[0]


def get_info(host_name, url):
	ip_adress = ""
	title = ""

	try:
		ip_adress = socket.gethostbyname(host_name)
		title = get_title(url)
	except:
		print(colored("Host is unreachable!", "red"))

	print(colored("\n      RESULT", "white"))
	print("[IP]    : " + ip_adress)
	print("[TITLE] : " + title)
