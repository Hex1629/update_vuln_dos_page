from colorama import Fore,Back,init
import sys,os,threading,time,requests,random,platform,urllib3,ctypes
from GUI import *
from ETC.prefix_find import *
from command import *
from ETC.update.check_update import *

download_file("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/ver_of_dos.txt","ETC\\update\\ver_github_of_dos.txt")

read_as_update = open("ETC\\update\\ver_github_of_dos.txt","r")
data_update = read_as_update.read()
read_as_update.close()

up_file = get_update("get now . . .")
update_patch = find_update(data_update)
if True == update_patch:
    print("FOUND NEW UPDATE . . .")
    print(f"VERSION OF DOS YOU:{up_file}")
    print(F"VERSION OF DOS NOW:{data_update}")
else:
    print("NOT UPDATE . . .")

time.sleep(2)

prefix = find_prefix("GET PREFIX NOW . . .")
banner()

while True:
    command = input(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}{Fore.WHITE}>_{Fore.RESET}{Fore.LIGHTGREEN_EX}]{Fore.RESET} ")
    command_attack(command)