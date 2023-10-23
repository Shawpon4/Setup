## SETUP -2024 ##

## CREAT BY SHAWPON ##

## import module ##

import os,sys,time,json,random,re,string,platform,base64,uuid

from time import sleep
from rich import print as SP
from rich.panel import Panel
from rich.text import Text as tekz
from time import sleep
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.text import Text as tekz
Shawponx = input(f'\x1b[38;5;46m╰─> \x1b[1;95mSetup-Storage -Give Y/N > \033[93m')
os.system(f"termux-setup-storage -{Shawponx}")

## Color code ##

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
reset_color = "\033[0m"
black_color = "\033[0;30m"
red_color = "\033[0;31m"
green_color = "\033[0;32m"
yellow_color = "\033[0;33m"
blue_color = "\033[0;34m"
purple_color = "\033[0;35m"
cyan_color = "\033[0;36m"
white_color = "\033[0;37m"
bold_black_color = "\033[1;30m"
bold_red_color = "\033[1;31m"
bold_green_color = "\033[1;32m"
bold_yellow_color = "\033[1;33m"
bold_blue_color = "\033[1;34m"
bold_purple_color = "\033[1;35m"
bold_cyan_color = "\033[1;36m"
bold_white_color = "\033[1;37m"

sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
ORANGE = '\033[1;35m'
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_RECORD = '\033[1;91m'

spbd_W = '\033[1;97m'

SP_BDGROUP = '\033[1;32m' 

SP_BD_YT = '\033[1;33m'

SPBD_BLUG = '\033[1;34m'
P = '\x1b[1;97m' # PUTIH
faff = 'x1b[38;5;46m'
M = '\x1b[1;91m' # MERAH
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU
SPBD_ID = '\033[1;35m'
facebook = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD,O,A,K])
OK_ID = random.choice([SPBD_ID,SP_BD_YT,SPBD_RECORD])

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 
RED = '\033[1;91m'

WHITE = '\033[1;97m'
SPBD_ID = '\033[1;35m'
SPBD = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU
## TIME-DATE-YEAR ##

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import pretty

from rich.text import Text as tekz
cokbrut=[]

princp=[]
## Logo ##

def print(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.010)

def banner():
	
	wel='# WELCOME TO TERMUX SETUP TOOL'
	
	cik2=mark(wel ,style='green')

	sol().print(cik2)
	
	time.sleep(0.15)

	ban=f'''
  _____ _____        ____  _____ 
  / ____|  __ \      |  _ \|  __ \ 
  | (___ | |__) |_____| |_) | |  | |
   \___ \|  ___/______|  _ <| |  | |
   ____) | |          | |_) | |__| |
 |_____/|_|          |____/|_____/
BANGLADESHI TEAM'''

	oi = nel(tekz(ban,justify='center',style='bold'), style='cyan')

	cetak(nel(oi, title='[bold cyan] • DEVELOVER INFORMATION • [/bold cyan]'))

print(f"\n\033[0;92m\33[0;41m NEW ADDED PIP AND PKG{x}")
print(f'\n{bold_cyan_color} pkg update pkg upgrade') 
print(f'\n install python') 
print(f'\n install php') 
print(f'\n install pip') 
print(f'\n install rsa') 
print(f'\n install pyaes') 
print(f'\n install asyncio') 
print(f'\n install async_generator') 
print(f'\n install bs4') 
print(f'\n install telethon') 
print(f'\n install requests') 
print(f'\n install colorama') 
print(f'\n install beautifulsoup4') 
print(f'\n install chardet')
print(f'\n install certifi') 
print(f'\n install idna') 
print(f'\n install python2') 
print(f'\n install git') 
print(f'\n install python3') 
print(f'\n install sqlite') 
print(f'\n install curl') 
print(f'\n install wget') 
print(f'\n install requests mechanize bs4') 
print(f'\n install paperkey') 
print(f'\n install play-audio') 
print(f'\n install pacman') 
print(f'\n install pypy3') 
print(f'\n install open-adventure')
print(f"\n install more package and pip{x}")

class __main__:

    def __init__(self):
    	user=[]
    
    banner()
    cetak(panel(f"{K2}[{H2}01{K2}] {K2}SETUP ONLY CRACKER PACKAGE(BASIC) \n{K2}[{H2}02{K2}] {K2}ADVANCE SETUP\n{K2}[{H2}03{K2}] {K2}ADMIN ID\n{K2}[{H2}04{K2}] {K2}EXIT\n",width=101,title=f"{K2}SETUP-MENU ",subtitle_align='center',padding=(0,2),style=f"green"))
    
    Shawpon = input(f'\x1b[38;5;46m╰─> \x1b[1;95mSELECT MENU ─> \033[93m')
    if Shawpon in ["01","1","A","a"]:
    	os.system("pkg update -y && pkg upgrade -y && pkg install git -y && pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests && pip install mechanize && pip install bs4 && pip install colorama && apt update -y")
    if Shawpon in ["02","2","B","b"]:
    	os.system("pkg update -y && pkg upgrade -y && termux-setup-storage -y && pkg install python -y && pkg install python2 -y && pkg install python2-dev -y && pkg install python3 -y && pkg install java -y && pkg install fish -y && pkg install ruby -y && pkg install help -y && pkg install git -y && pkg install host -y && pkg install php -y && pkg install perl -y && pkg install nmap -y && pkg install bash -y && pkg install clang -y && pkg install nano -y && pkg install w3m -y && pkg install havij -y && pkg install hydra -y && pkg install figlet -y && pkg install cowsay -y && pkg install curl -y && pkg install tar -y && pkg install zip -y && pkg install unzip -y && pkg install tor -y && pkg install google -y && pkg install sudo -y && pkg install wget -y && pkg install wireshark -y && pkg install wgetrc -y && pkg install wcalc -y && pkg install bmon -y && pkg install vpn -y && pkg install unrar -y && pkg install toilet -y && pkg install proot -y && pkg install net-tools -y && pkg install golang -y && pkg install chroot -y macchanger-y &&pkg install openssl -y && pkg install cmatrix -y && pkg install openssh -y && pkg install wireshark -y && pkg install macchanger -y && pkg install espeak -y && pkg install robot -y && pkg install nmap -y && pkg install coreutils -y && pkg install sl -y && pkg install dnsutils -y && pkg install fortune -y && pkg install libcaca -y && pip install --robota && pip install async_generator && pip install pyaes && pip install rsa && pip install colourama && pip install telethon && pip install asyncio && pip install wheel && pip install espeak && pip install mpv && pip install --upgrade pip && pip install requirements && pip install requests && pip2 install requests && pip install mechanize && pip2 install mechanize && pip install lolcat && pip install bs4 && pip2 install bs4 && pip2 install requests bs4 && pip install futures && pip2 install futures && pip install rich && pip install wordlist")
    if Shawpon in ["03","3","C"]:
    	os.system("xdg-open https://www.facebook.com/original.Typeboss.ur.father")
    if Shawpon in ["04","4","X","x","0","00"]:
    	exit()
    else:
    	exit()
__main__()