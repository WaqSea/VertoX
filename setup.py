import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from services.gui import *
from colorama import Fore, Style, init
import time

init(autoreset=True)

if not os.path.exists(".env"): 
with open(".env", "w") as f: 
f.write("")

SETUP_BANNER()

def delete_self(): 
path = os.path.abspath(__file__) 
time.sleep(2) # Let the code finish completely, then delete it 
try: 
os.remove(path) 
print(f"{Fore.GREEN}setup.py deleted successfully.") 
except Exception as e: 
print(f"{Fore.RED}setup.py could not be deleted: {e}")

TOKEN = input(Fore.CYAN + "Enter your Discord Bot Token: " + Style.RESET_ALL).strip()
CHANNEL_ID = input(Fore.CYAN + "Enter your Discord Channel ID: " + Style.RESET_ALL).strip()
ADMIN_ID = input(Fore.CYAN + "Enter your Discord Admin User ID: " + Style.RESET_ALL).strip()

with open(".env", "w") as f: 
f.write(f"TOKEN={TOKEN}\n") 
f.write(f"CHANNEL_ID={CHANNEL_ID}\n") 
f.write(f"ADMIN_ID={ADMIN_ID}\n")

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def delete_setup_bat(): 
bat_path = os.path.abspath("setup.bat") 
time.sleep(2) 
if os.path.exists(bat_path): 
try: 
os.remove(bat_path) 
time.sleep(1) # Wait for a second before deleting 
delete_self() 
print(Fore.YELLOW + f"{bat_path} deleted successfully.") 
except Exception as e: 
print(Fore.RED + f"Failed to delete {bat_path}: {e}") 
else: 
print(Fore.RED + f"{bat_path} not found.")

@bot.event
async def on_ready(): 
await bot.tree.sync() 
print(Fore.GREEN + f"Bot logged in as: {bot.user}") 

try: 
user_id = int(os.getenv("ADMIN_ID")) 
user = await bot.fetch_user(user_id) 
await user.send("✅ The bot has been successfully set up! You can now use its commands.") 
print(Fore.BLUE + "Message sent to admin successfully.") 
delete_setup_bat() 
except ValueError: 
print(Fore.RED + "ADMIN_ID is not a valid number.") 
except discord.NotFound: 
print(Fore.RED + "User not found. Check if the Admin ID is correct.") 
except discord. Forbidden: 
print(Fore.RED + "Cannot send DM. The user has DMs disabled or blocked the bot.") 
except Exception as e: 
print(Fore.RED + f"Unexpected error while sending message: {e}") 

await bot.close()

try: 
bot.run(os.getenv("TOKEN"))
except discord.LoginFailure: 
print(Fore.RED + "Invalid Discord Token. Please enter a valid bot token.") 
delete_setup_bat() 
exit(1)
except Exception as e: 
print(Fore.RED + f"Failed to start the bot: {e}") 
exit(1)
