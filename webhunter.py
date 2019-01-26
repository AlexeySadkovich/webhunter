# -*- coding: utf-8 -*-

from lib.base_info import get_info
from lib.startflooder import set_options
from lib.gethtml import gethtml
from termcolor import colored
from lib.parseurls import add_link
import os
import platform
import sys
import urllib

#http://ns.licei40.sampo.ru

platform = platform.system()

if platform.lower() == 'windows':
	clear = "cls"
else:
	clear = "clear"


def update_screen():
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
		protocol = input("HTTP or HTTPS [1/2]? : ")

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

		print("\n [1] Information about host")
		print(" [2] Get links")
		print(" [3] Get html file")
		print(" [4] Start HTTP flood")
		print(" [5] Another target")
		print(colored(" [q] Quit\n", "yellow"))

		try:
			ans = input(" [>] ")
		except:
			print("Answer is incorrect!")

		if ans == '1':
			get_info(name, url)
			update_screen()
		elif ans == '2':
			add_link(url)
			update_screen()
		elif ans == '3':
			gethtml(url)
			update_screen()
		elif ans == '4':
			set_options(name, url)
			update_screen()
		elif ans == '5':
			refresh_screen()
			get_target()
		elif ans == 'q':
			print("Bye!")
			sys.exit(0)
		else:
			refresh_screen()


if __name__ == "__main__":
	refresh_screen()
	get_target()

