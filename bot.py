import os
import discord
import r6sapi
import asyncio
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

bot = discord.Bot()



bot.run(token)

