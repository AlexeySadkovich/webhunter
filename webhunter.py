# -*- coding: utf-8 -*-

from lib.baseinfo import get_info
from lib.startflooder import set_options
from lib.gethtml import get_html
from termcolor import colored
from lib.parseurls import add_links
from lib.getcss import get_css
import os
import platform
import sys
import socket


platform = platform.system()

if platform.lower() == 'windows':
	clear = "cls"
else:
	clear = "clear"


def wait_screen():
	input("\nPress <ENTER>")
	refresh_screen()


def refresh_screen():
	os.system(clear)
	banner()


def banner():
	with open("./lib/banner.txt") as b:
		print(colored(b.read(), "yellow"))
	print(colored("/////////", "yellow", attrs=['reverse']) + colored("CAN BE ILLEGAL", "red", "on_yellow") + colored("/////////\n", "yellow", attrs=['reverse']))


def get_target():

	while True:
		target = input("Target : ")

		if len(target.split(".")) > 1:
			break
		else:
			print(colored("Invalid URL!", "red"))

	while True:
		protocol = input("HTTP or HTTPS? [1/2] : ")

		if protocol == "1":
			url = "http://" + target
			break
		elif protocol == "2":
			url = "https://" + target
			break
		else:
			print("Invalid Protocol!")

	refresh_screen()
	get_action(target, url)


def get_action(name, url):
	ans = 0

	while ans != '99':
		print(colored("	Website: ", "blue") + url)

		print("\n [1] Basic information")
		print(" [2] Nmap scan" + colored("(Nmap required)", "white"))
		print(" [3] Get links")
		print(" [4] Get html file")
		print(" [5] Get CSS file")
		print(" [6] Start HTTP flood")
		print(" [7] Another target")
		print(colored(" [q] Quit\n", "yellow"))

		try:
			ans = input(" [>] ")
		except:
			print("Answer is incorrect!")

		if ans == '1':
			get_info(name, url)
			wait_screen()
		elif ans == "2":
			ip_adress = socket.gethostbyname(name)
			os.system("nmap -F " + ip_adress)
			wait_screen()
		elif ans == '3':
			add_links(url)
			wait_screen()
		elif ans == '4':
			get_html(url)
			wait_screen()
		elif ans == '5':
			get_css(url)
			wait_screen()
		elif ans == '6':
			set_options(name, url)
			wait_screen()
		elif ans == '7':
			refresh_screen()
			get_target()
		elif ans == 'q':
			print(colored("\n	Bye!", "green"))
			sys.exit(0)
		else:
			refresh_screen()


if __name__ == "__main__":
	refresh_screen()
	get_target()

