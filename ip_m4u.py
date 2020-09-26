# -*- coding: utf-8 -*-
#coded by M4U.YT 
import argparse
import requests, json
import sys
from sys import argv
import os
print(u'''\u001b[48;5;16m
                     \u001b[38;5;12m    •\u001b[38;5;196m•\u001b[38;5;208m•\u001b[0m
     \u001b[38;5;226m    •×\ Created By: @ M 4 U . Y T /×•\u001b[0m
  \u001b[38;5;117m  ╭─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫──━─╮\u001b[0m
   \u001b[38;5;117m•┃\u001b[0m   \u001b[38;5;208m ᚓ \u001b[0m 𝙴 𝚃 𝙷 𝙸 𝙲 𝙰 𝙻 \u001b[38;5;208m|\u001b[0m \u001b[38;5;196m𝙷 𝙰 𝙲 𝙺 𝙴 𝚁 \u001b[38;5;208mᚓ  \u001b[0m    \u001b[38;5;117m┃•\u001b[0m
\u001b[38;5;117m╭─━─≪✠≫─━─━─≪✠≫─━──━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─╮\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m╭━╮╭━╮ \u001b[38;5;196m╭╮ ╭╮ \u001b[38;5;208m╭╮ ╭╮  \u001b[38;5;39m╭╮  ╭╮ \u001b[38;5;48m╭━━━━╮ \u001b[38;5;196m\\\ \u001b[38;5;200m   °••°    \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m┃┃╰╯┃┃ \u001b[38;5;196m┃┃ ┃┃ \u001b[38;5;208m┃┃ ┃┃  \u001b[38;5;39m┃╰╮╭╯┃ \u001b[38;5;48m┃╭╮╭╮┃  \u001b[38;5;196m\\\  \u001b[38;5;208m╭\━━/╮   \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m┃╭╮╭╮┃ \u001b[38;5;196m┃╰━╯┃ \u001b[38;5;208m┃┃ ┃┃  \u001b[38;5;39m╰╮╰╯╭╯ \u001b[38;5;48m╰╯┃┃╰╯   \u001b[38;5;196m\\\ \u001b[38;5;208m┃ \u001b[38;5;116moo\u001b[38;5;208m ┃   \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m┃┃┃┃┃┃ \u001b[38;5;196m╰━━╮┃ \u001b[38;5;208m┃┃ ┃┃   \u001b[38;5;39m╰╮╭╯    \u001b[38;5;48m┃┃     \u001b[38;5;196m// \u001b[38;5;208m┃ \u001b[38;5;116m==\u001b[38;5;208m ┃   \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m┃┃┃┃┃┃    \u001b[38;5;196m┃┃ \u001b[38;5;208m┃╰━╯┃ ╭╮ \u001b[38;5;39m┃┃     \u001b[38;5;48m┃┃    \u001b[38;5;196m//  \u001b[38;5;208m╰━||━╯   \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m|\u001b[0m  \u001b[38;5;12m╰╯╰╯╰╯    \u001b[38;5;196m╰╯ \u001b[38;5;208m╰━━━╯ ╰╯ \u001b[38;5;39m╰╯     \u001b[38;5;48m╰╯   \u001b[38;5;196m//   \u001b[38;5;200m •°°•    \u001b[38;5;117m|\u001b[0m
\u001b[38;5;117m╰─━─≪✠≫─━─━─≪✠≫─━──━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─╯\u001b[0m
     GitHub -> \u001b[38;5;197mhttps://github.com/mahendraplus\u001b[0m
                    \u001b[38;5;12m    •\u001b[38;5;196m•\u001b[38;5;208m•\u001b[0m                     ''')

print('''\u001b[38;5;81mUSE:
python ip_m4u.py -v [Ip Address]''')


parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()
#-----------------
red = '\u001b[38;5;81m'
yellow = '\u001b[38;5;81m'
lgreen = '\u001b[38;5;46m'
clear = '\u001b[38;5;46m'
bold = '\u001b[38;5;46m'
cyan = '\u001b[38;5;46'
#------------------- M Y  C O L O R -------
#m4u banner

print (red+bold+"𝙲 𝚛 𝚎 𝚊 𝚝 𝚎 𝚍   𝙱 𝚢 :    @ 𝙼 𝟺 𝚄 . 𝚈 𝚃 \n"+clear)
print ("\u001b[38;5;198mM4U.YT\n"+clear)



ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"⬤"
        b = cyan+bold+"⬤"
        print (a, "[ 🤵 Victim]:", data['query'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (b, "[ 📶 ISP]:", data['isp'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (a, "[ 👁️‍🗨️ Organisation]:", data['org'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (b, "[ 🗺️ City]:", data['city'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (a, "[ 🏷️ Region]:", data['region'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (b, "[ 📡 Longitude]:", data['lon'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (a, "[ 📡 Latitude]:", data['lat'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (b, "[ 🕙 Time zone]:", data['timezone'])
        print(red+"─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─"+red)
        print (a, "[ 🔢 Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('M4U.YT, Ram Ram Ji'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+"CHECK YOUR INTERNETn!"+clear)
sys.exit(1)
