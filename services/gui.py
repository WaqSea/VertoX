import random
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(f"""
{Fore.BLUE}
 ██▒   █▓▓█████  ██▀███  ▄▄▄█████▓ ▒█████  ▒██   ██▒
▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░
 ▓██  █▒░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒██░  ██▒░░  █   ░
  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ 
   ▒▀█░  ░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒
   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
   ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░      ░ ▒ ▒░ ░░   ░▒ ░
     ░░     ░     ░░   ░   ░      ░ ░ ░ ▒   ░    ░  
      ░     ░  ░   ░                  ░ ░   ░    ░  
     ░                                              
{Fore.YELLOW}            Welcome to VertoX Multi Tool
{Fore.RED}            This Tool is made by WaqSea
{Style.RESET_ALL}

{Fore.CYAN} ┌───────────────────────────────┐
 │        MAIN MENU OPTIONS      │
 └───────────────────────────────┘
{Fore.GREEN} [1]{Style.RESET_ALL} Token Validator
{Fore.GREEN} [2]{Style.RESET_ALL} Webhook Sender
{Fore.GREEN} [3]{Style.RESET_ALL} Discord Bot Tester
{Fore.GREEN} [4]{Style.RESET_ALL} QR Code Generator
{Fore.GREEN} [5]{Style.RESET_ALL} System Info Viewer
{Fore.GREEN} [6]{Style.RESET_ALL} Save/Load .env Config
{Fore.GREEN} [7]{Style.RESET_ALL} Discord Keylogger
{Fore.GREEN} [8]{Style.RESET_ALL} Exit

""")

def SETUP_BANNER():
    print(f"""

 ██▒   █▓▓█████  ██▀███  ▄▄▄█████▓ ▒█████  ▒██   ██▒
▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▒██▒  ██▒▒▒ █ █ ▒░
 ▓██  █▒░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒██░  ██▒░░  █   ░
  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒██   ██░ ░ █ █ ▒ 
   ▒▀█░  ░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░ ████▓▒░▒██▒ ▒██▒
   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
   ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░      ░ ▒ ▒░ ░░   ░▒ ░
     ░░     ░     ░░   ░   ░      ░ ░ ░ ▒   ░    ░  
      ░     ░  ░   ░                  ░ ░   ░    ░  
     ░                                              
                                                                                                                 

    {Fore.YELLOW}Welcome to VertoX Setup! {Style.RESET_ALL}
    {Fore.YELLOW}This script will help you set up your Discord bot with the necessary configurations.{Style.RESET_ALL}

                                                {Fore.RED}This Tool is made by WaqSea{Style.RESET_ALL}
    """)