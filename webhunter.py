from lib.base_info import get_info
from termcolor import colored
import os

#http://ns.licei40.sampo.ru

def update_screen():
	wait = input("\nPress <ENTER>")
	refresh_screen()

def refresh_screen():
	os.system("clear")
	banner()

def banner():
	with open("./lib/banner.txt") as b:
		print(colored(b.read(), "blue"))


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
		print("Site: " + url)
		print("===================")
		print("[1] Information about host")
		print("[2] Get html file")
		print("[3] Get links")
		print("[4] Another target")
		print("[99]Quit")
		print("===================")

		try:
			ans = input("[>] ")
		except:
			print("Answer is incorrect!")

		if ans == '1':
			get_info(name, url)
			update_screen()
		elif ans == '2':
			get_html()
			update_screen()
		elif ans == '4':
			os.system("clear")
			get_target()
		elif ans == '99':
			print("Bye!")
			break
		else:
			refresh_screen()


if __name__ == "__main__":
	refresh_screen()
	get_target()

