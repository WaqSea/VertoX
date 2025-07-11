import discord
import asyncio

def validate_token():
    token = input("Enter your Discord Bot Token: ").strip()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    async def check():
        try:
            await client.login(token)
            await client.close()
            return True
        except discord.LoginFailure:
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    valid = asyncio.run(check())

    if valid:
        print("✅ Token is valid!")
    else:
        print("❌ Invalid token or login failed.")

    return token, valid