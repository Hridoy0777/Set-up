###__IMPORT__###

import os , time
from time import sleep

###__COLOURS__###

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

logo = ('''
 \x1b[38;5;46m╔═════════════════[\033[1;32m 𝘼𝘿𝙈𝙄𝙉 𝙄𝙉-𝙁𝙍𝙊 \033[1;32m]══════════════╗
 \x1b[38;5;46m║     \033[1;96m[🍁] CREATED BY\33[0;m   : \033[1;96m 𝑯𝑹𝑰𝑫𝑶𝒀 𝑯𝑶𝑺𝑺𝑨𝑰𝑵       \033[1;32m║
 \x1b[38;5;46m║     \033[1;32m[🍁] FACEBOK      : \033[1;34m 𝑹𝑶𝑫𝑵𝑬𝒀  𝑪𝒀𝑷𝑹𝑰𝑨𝑵     \033[1;32m ║
 \x1b[38;5;46m║     \033[1;35m[🍁] GITHUB       :  \033[1;35m𝑯𝒓𝒊𝒅𝒐𝒚0777          \033[1;32m ║
 \x1b[38;5;46m║     \033[1;36m[🍁] TOOL STATUS  : \033[1;36m SET-UP TERMUX BASIC \033[1;32m ║
 \x1b[38;5;46m║     \033[1;35m[🍁] TEAM         :  \033[1;35 CEMPAR SPAMMING TEAM \033[1;32m ║
 \x1b[38;5;46m║     \033[1;36m[🍁] TOOL VIRSION :  \033[1;36m0.0                 \033[1;32m ║
 \x1b[38;5;46m║᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱⊰᯽⊱┈─╌❊❊╌──┈⊰᯽⊱ \033[1;32m║
 \x1b[38;5;46m║  [\033[1;97m🌺\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....                \033[1;32m  ║
 \x1b[38;5;46m║  [\033[1;97m🌺\033[1;91m]\033[1;32m 𝐑𝐈𝐃𝐃𝐔 TERMUX COMMEND ZONE....          \033[1;32m ║
 \x1b[38;5;46m╚═════════════════[\x1b[38;5;46m 𝑹𝑰𝑫𝑫𝑼 - 𝑵𝑶𝑶𝑩 \033[1;32m]══════════════╝''')
 
menu = ('''
[1] Basic Setup
[2] Contact Admin 
[3] Contact Owner 
[4] Exit
''')
 
def setup ():
	os.system("pkg update -y && pkg upgrade -y && pkg install git -y &&pkg install python -y && pkg install python2 -y && pkg install python3 -y && pkg install curl -y && pkg install wget -y && pip install requests  mechanize bs4")
	
def join (): 
	os.system ("xdg-open https://facebook.com/Riddu999")
	
def main():
	os.system('clear')
	print(logo)
	print('')
	print(menu)
	option = input(f'{YELLOW}Choose Option : ')
	if option == '1':
		setup()
		main()
	elif option == '2':
		join()
		main()
	elif option == '3':
		os.system("xdg-open https://wa.me/+88001906312645")
		main()
	elif option =='4':
		exit()
	else:
		print('\n')
		print(f'Choose Carefully')
		time.sleep(3)
		main()

main()