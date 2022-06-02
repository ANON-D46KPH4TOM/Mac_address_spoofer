from os import system
system('pip install randmac')
system('pip install colorama')
from time import sleep
from randmac import RandMac
from colorama import Fore
system('clear')
banner = ('''

 ███╗   ███╗ █████╗  ██████╗    ███████╗██████╗  ██████╗  ██████╗ ███████╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗
██╔████╔██║███████║██║         ███████╗██████╔╝██║   ██║██║   ██║█████╗  █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║         ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║╚██████╗    ███████║██║     ╚██████╔╝╚██████╔╝██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝ 
            
                                           CODED BY ANON_DARKPHANTOM

[1] - Custom mac address
[2] - Random mac address

''').splitlines()
for i in banner:
    print(i)
    sleep(0.1)
mac_sample = '00:00:00:00:00:00'
Mode = input('\nPlease Select an Option : ')
if Mode == '1':
    mac_address = input(f'{Fore.RED}[!]{Fore.WHITE} Please Enter Your Mac Address : ')
    system('ifconfig  eth0  down')
    system('ifconfig  eth0  hw ether ' + mac_address)
    system('ifconfig  eth0  up')
    print(f'{Fore.GREEN}[+]{Fore.WHITE} Mac Address Changed & U Can Check It With ifconfig command :)')
elif Mode == '2':
    change_time = input(f'{Fore.RED}[!]{Fore.WHITE} Please enter Mac Address Changing Time :')
    while True:
        generated_mac = str(RandMac(mac_sample))
        sleep(int(change_time))
        system('ifconfig eth0 down')
        system(f'ifconfig eth0 hw ether {generated_mac}')
        system('ifconfig eth0 up')
        print(f'{Fore.GREEN}[+]{Fore.WHITE} Mac Address Changed , Your New Mac Address Is : {generated_mac}')
else:
    print(f'\n{Fore.RED}[!]{Fore.WHITE}Please Enter a Valid Option !')
    sleep(0.5)
    print(f'{Fore.RED}[!]{Fore.WHITE}program will close in 3 seconds')
    sleep(3)
    exit()
