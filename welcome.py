import random
import time
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def intro1():
    print()
    print(f'{Fore.LIGHTRED_EX}⠀⠀⠀⠀⠀⣀⠤⠖⠋⠉⠉⠉⠉⠉⠑⠢⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀')    
    print(f'{Fore.LIGHTRED_EX}⠀⠀⠀⡴⠋⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀              ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⣯⠀⠀⡤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠈⣇⠀⠀             {Fore.WHITE} ██ ▄█▀▓█████▄▄▄█████▓ ▄▄▄       ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⣟⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⡄⠀⠀⠀⡇⠀             {Fore.WHITE} ██▄█▒ ▓█   ▀▓  ██▒ ▓▒▒████▄    ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀    ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⣿⢧⣄⠀⣟⣿⠇⠀⠀⠀⠀⠀⠘⠿⠿⠿⣇⠀⠀⠀⡇⠀             {Fore.WHITE}▓███▄░ ▒███  ▒ ▓██░ ▒░▒██  ▀█▄  ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███     ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⣿⡬⣿⡆⢹⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣷⠀⠀⡏⠀             {Fore.WHITE}▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄  ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⢿⣷⡌⣇⢸⣆⡀⠀⢀⣀⣤⣴⡯⣿⡿⠈⣿⠀⡼⠀              {Fore.WHITE}▒██▒ █▄░▒████▒ ▒██▒ ░  ▓█   ▓██▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒ ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⠀⢏⢻⣟⣯⡇⠉⠻⣿⣯⣭⣿⢟⡟⠁⠀⢹⠀⣼⠀ ')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⠀⠀⠱⡿⣏⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢯⠀⠀⠀ ')
    print(f'{Fore.LIGHTRED_EX} ⠀⠀⠀⠀⠀⡴⠷⣽⣿⣏⣧⣄⣀⣀⡤⠤⠖⣾⣭⡿⣿⣿⣗⣒⣦                  {Fore.CYAN}Repo: https://github.com/IlyaKosloF/ketamine')
    print(f'{Fore.LIGHTRED_EX}⠀⠀⠀⠀⣲⣞⣻⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠭⠯⠯⠿⠯⠭⠭⠤                  {Fore.CYAN}Instagram: ilya.koslof') 
    print(f'{Fore.LIGHTRED_EX}⠤⠶⠿⠿⠷⠞⠭⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print(f'{Fore.LIGHTRED_EX} ')
    print(f'{Fore.LIGHTRED_EX}                                            {Fore.CYAN}love')
    print(f'{Fore.LIGHTRED_EX}       ')
    print(f'{Fore.LIGHTRED_EX}         ')
    print(f'{Fore.LIGHTRED_EX}           ')
    print(f'{Fore.LIGHTRED_EX}              ')
    print(f'{Fore.LIGHTRED_EX}               ')
    print(f'{Fore.LIGHTRED_EX}                 ')

def welcome():
    introList = [intro1]
    subprocess.call(['clear'])
    random.choice(introList)()
    time.sleep(5.0)
    subprocess.call(['clear'])
