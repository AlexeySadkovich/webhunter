# -*- coding: utf-8 -*-

import socket
import requests
from termcolor import colored
from urllib.request import urlopen
from lxml import html


def check_robots(url):
	protocol = url.split("//")[0]
	domain = url.split("//")[1]

	if domain.find("www.") == -1:
		url = protocol + "//www." + domain

	path = url + "/robots.txt"

	try:
		urlopen(path)
		status = "There is Robots.txt"
	except:
		status = "Robot.txt not found"
	finally:
		return status



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
		print(colored("\nHost is unreachable!", "red"))
	else:
		print(colored("\n      RESULT", "white"))
		print("[IP]    : " + ip_adress)
		print("[TITLE] : " + title)
		print("[ROBOTS]: " + check_robots(url))
