from colorama import Fore,Back,init
import sys,os,threading,time,requests,random,platform,urllib3,ctypes
from GUI import *
from command import *
from ETC.update.check_update import *
def download_file2(url, local_file_path,type):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "w" in type:
                with open(local_file_path, 'w') as local_file:
                     local_file.write(response.text)
                     print(f"{url} TO {local_file_path} WRITING FILES WITH W MODE . . .")
                     time.sleep(1)
            else:
                with open(local_file_path, 'wb') as local_file:
                     local_file.write(response.text)
                     print(f"{url} TO {local_file_path} WRITING FILES WITH WB MODE . . .")
                     time.sleep(1)
    except requests.exceptions:
        print("error . . .")
download_file("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/ver_of_dos.txt","ETC\\update\\ver_github_of_dos.txt")
read_as_update = open("ETC\\update\\ver_github_of_dos.txt","r")
data_update = read_as_update.read()
read_as_update.close()
up_file = get_update("get now . . .")
update_patch = find_update(data_update)
def loader_update():
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/NOTE_UPDATE.txt","NOTE_PATCH.txt","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/setup.py","setup.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/ETC/update/check_update.py","ETC\\update\\check_update.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/command.py","command.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/DOS_VULN.py","DOS_VULN.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/ETC/prefix_find.py","ETC\\prefix_find.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/DOS_VULN/GUI.py","GUI.py","w")
    download_file2("https://raw.githubusercontent.com/Hex1629/update_vuln_dos_page/main/ver_of_dos.txt","ETC\\update\\ver_of_dos.txt","w")
    print("DONE UPDATE NEW!! AND OPEN AGAIN!!")
    time.sleep(2)
    start_app("NOTE_PATCH.txt")
    time.sleep(2)
    exit()

update_auto_file = open("ETC\\update\\check_update.txt","r")
UAF = update_auto_file.read()
update_auto_file.close()

if "True" in UAF:
    if False == update_patch:
        print("FOUND NEW UPDATE . . .")
        print(f"VERSION OF DOS YOU:{up_file}")
        print(F"VERSION OF DOS NOW:{data_update}")
        if up_file == data_update:
            if data_update == up_file:
                print("DONE PATCH . . .")
            else:
                loader_update()
        else:
            loader_update()
            
if "Windows" in platform.system():
            os.system("cls")
else:
            os.system("clear")
            
banner()
while True:
    command = input(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}{Fore.WHITE}>_{Fore.RESET}{Fore.LIGHTGREEN_EX}]{Fore.RESET} ")
    command_attack(command)
