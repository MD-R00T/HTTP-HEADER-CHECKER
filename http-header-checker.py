import requests
import os
from colorama import Fore, Back, Style
import pyfiglet
ascii_banner = pyfiglet.figlet_format("ARIZONA !!")
print(ascii_banner)

os.system("cls")
print("")
first = input(Fore.GREEN + "[+] " + Fore.BLUE + "Give Me A Site : ")
check = requests.get(first)
http_security_headers = ['X-Frame-Options', 'Host', 'X-XSS-Protection', 'Cache-Control', 'Pragma', 'Content-Type',
                         'Content-Encoding', 'Accept-Encoding', 'X-UA-Compatible', 'IE', 'Date', 'Set-Cooki',
                         'Dnn_IsMobile', 'HttpOnly', 'Referer', 'Expires', 'User-Agent', 'Content-Length',
                         'X-Content-Type-Options', 'Content-Type', 'Connection', 'Authorization', 'Accept', 'A-IM',
                         'Accept-Charset', 'Accept-Datetime', 'Accept-Language', 'Expect', 'Origin', 'Forwarded',
                         'From', 'If-Match', 'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since',
                         'Max-Forwards', 'Proxy-Authorization', 'Range', 'TE', 'Upgrade', 'Via', 'Warning',
                         'Non-Standard-Headers', 'Dnt', 'X-Requested-With', 'X-CSRF-Token', 'ETag', 'Last-Modified', 'Accept-Ranges']
header_dict = {}
for item in http_security_headers:
    if item in check.headers.keys():
        header_dict.update({item: 'FOUND'})
        print(f'{Fore.GREEN}{item}:{header_dict[item]}')
    else:
        header_dict.update({item: 'NOT-FOUND'})
        print(f'{Fore.RED}{item}:{header_dict[item]}')
print(Fore.YELLOW + "Header Checking Finished Successfully\n")




