from lib.base_info import get_info
import os

#http://ns.licei40.sampo.ru

def refresh_screen(target_url):
	os.system("clear")
	print("Site: " + target_url)

def banner():
	with open("./lib/banner.txt") as b:
		print("\n\033[94m" + b.read() + "\033[m")


def get_target():

	while True:
		target = input("Target : ")

		if len(target.split(".")) > 1:
			break
		else:
			print("Invalid URL!")

	while True:
		protocol = input("HTTP or HTTPS [1/2] : ")

		if protocol == "1":
			url = "http://" + target
			break
		elif protocol == "2":
			url = "https://" + target
			break
		else:
			print("Invalid Protocol!")

	get_action(target, url)
	refresh_screen(url)


def get_action(name, url):
	ans = 0

	while ans != '99':
		print("\n===================")
		print("[1] Information about host")
		print("[2] Get html file")
		print("[3] Get links")
		print("[4] Another target")
		print("[99]Quit")
		print("===================")

		try:
			ans = input("> ")
		except:
			print("Answer is incorrect!")

		if ans == '1':
			get_info(name, url)
		elif ans == '2':
			get_html()
		elif ans == '4':
			os.system("clear")
			get_target()
		elif ans == '99':
			print("Bye!")
			break
		else:
			print("Choose from list")

		refresh_screen(url)


if __name__ == "__main__":
	banner()
	get_target()

