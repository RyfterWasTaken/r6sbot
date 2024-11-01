import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
guild_ids = os.getenv("GUILD_IDS")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=guild_ids)
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(token)

