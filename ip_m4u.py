#coded by M4U.YT 
#
import argparse
import requests, json
import sys
from sys import argv
import os
print (u'''
\u001b[48;5;16m
╭─━─≪✠≫─━─━─≪✠≫─━──━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─╮
|   \u001b[38;5;196m888b     d888 \u001b[38;5;202m    d8888 \u001b[38;5;220m 888     888     \u001b[38;5;201mY88b   d88P\u001b[38;5;198m 88888888888\u001b[0m       |
|   \u001b[38;5;196m8888b   d8888 \u001b[38;5;202m   d8P888 \u001b[38;5;220m 888     888     \u001b[38;5;201m Y88b d88P     \u001b[38;5;198m 888    \u001b[0m       |
|   \u001b[38;5;196m88888b.d88888 \u001b[38;5;202m  d8P 888  \u001b[38;5;220m888     888      \u001b[38;5;201m Y88o88P    \u001b[38;5;198m   888    \u001b[0m       |
|   \u001b[38;5;196m888Y88888P888 \u001b[38;5;202m d8P  888  \u001b[38;5;220m888     888      \u001b[38;5;201m  Y888P      \u001b[38;5;198m  888   \u001b[0m        |
|   \u001b[38;5;196m888 Y888P 888 \u001b[38;5;202md88   888  \u001b[38;5;220m888     888      \u001b[38;5;201m   888      \u001b[38;5;198m   888    \u001b[0m       |
|   \u001b[38;5;196m888  Y8P  888 \u001b[38;5;202m8888888888 \u001b[38;5;220m888     888        \u001b[38;5;201m 888      \u001b[38;5;198m   888   \u001b[0m        |  
|   \u001b[38;5;196m888   "   888  \u001b[38;5;202m     888  \u001b[38;5;220mY88b. .d88P  \u001b[38;5;111md8b   \u001b[38;5;201m 888     \u001b[38;5;198m    888   \u001b[0m        |
|   \u001b[38;5;196m888       888  \u001b[38;5;202m     888  \u001b[38;5;220m "Y88888P"   \u001b[38;5;111mY8P    \u001b[38;5;201m888        \u001b[38;5;198m 888  \u001b[0m         | 
╰─━─≪✠≫─━─━─≪✠≫─━──━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─━─≪✠≫─━─╯
''')
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
print ("\u001b[38;5;198mEmail: mahendrakumargahelot@gmail.com\n"+clear)



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
