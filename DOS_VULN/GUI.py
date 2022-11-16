from colorama import Fore,Back,init
from ETC.prefix_find import *
import string
prefix = find_prefix("GET PREFIX NOW . . .")
def banner():
    print(f"""{Fore.CYAN}&----------------------------------------------------------&
| 8888b.   dP"Yb  .dP"Y8    Yb    dP 88   88 88     88b 88 |
|  8I  Yb dP   Yb `Ybo."     Yb  dP  88   88 88     88Yb88 |
{Fore.BLUE}|  8I  dY Yb   dP o.`Y8b      YbdP   Y8   8P 88  .o 88 Y88 |
| 8888Y"   YbodP  8bodP'       YP    `YbodP' 88ood8 88  Y8 |
&----------------------------------------------------------&

{Fore.CYAN}
#--------------------------------------------------------#
|                                                        |
         {prefix}method use for see list method dos . . .       
         {prefix}cls,clear use for clear print . . .
         {Fore.BLUE}{prefix}back use for back to home
         {prefix}exit for use exit . . .
|                                                        |
*--------------------------------------------------------*
{Fore.RESET}""")

def method():
    print(f"""{Fore.GREEN}
#----------------------------- method  VNLN ---------------------------#
| [+] {prefix}nov-5-2022 <url> <time> <mod> <type>
#----------------------------------------------------------------------#

# TOOL OTHER ----------------------------------------------------------#
| [+] {prefix}ping <url> <get,post,put,patch,head,option,delete> <time>
#----------------------------------------------------------------------#
{Fore.YELLOW}
@- MODE AND TYPE VULN --------------------------------------------
| [>_] LIST . . . .
|  |
|  |_ [MOD]: re_user_spf user_spf re_ssl_user_spf user_normal
|  |
|  |__ [TYPE]: random all get post head delete option patch put  
|
@----------------------------------------------------------------{Fore.RESET}""")

def note_log(url,time_loop,mod,type):
    print(f"""{Fore.LIGHTGREEN_EX}--------------------
{Fore.LIGHTYELLOW_EX}LOG.DOS     
{Fore.LIGHTCYAN_EX}####################
{Fore.LIGHTRED_EX} |_[URL] {url}
 |__[TIME] {time_loop}
 |___[MOD] {mod}
 |____[TYPE] {type}
 {Fore.RESET}""")

def end_log():
    print(f"""{Fore.LIGHTMAGENTA_EX}
~-------------~
  ! DOS DONE ! {Fore.RESET}
~-------------~
{Fore.RED}Please wait and check down. but not down because vulnerability is block!{Fore.RESET}
{Fore.YELLOW}YOU CAN'T SEE WEBSITE DOWN BUT OTHER SEE!{Fore.RESET}
""")

def message_flood(method,code,i,data_buff):
    if str(200) in str(code):
        print(f"{Fore.LIGHTGREEN_EX}{method.upper()} {i} SUCCESS TO CONNECT ID-{data_buff} . . .{Fore.RESET}")
    else:
        print(F"{Fore.YELLOW}{method.upper()} {i} CODE-{code} FAIL TO CONNECT ID-{data_buff} . . .{Fore.RESET}")
