import os
from colorama import Fore,Back,init
print(f"""{Fore.GREEN}
SETUP CNC OR CONTROL PANEL . . .
1] PREFIX COMMAND SETUP
2] UPDATE CHECK AUTO {Fore.RESET}""")
prefix_get = input("prefix:")
pre_import = open("ETC\\prefix.txt",'w')
pre_import.write(str(prefix_get))
pre_import.close()

print(f"{Fore.RED}True or False")
auto_update = input("auto:")
import_file_write = open("ETC\\update\\check_update.txt","w")
import_file_write.write(str(auto_update))
import_file_write.close()

print(f"removeing setup.py{Fore.RESET}")
os.remove(__file__)