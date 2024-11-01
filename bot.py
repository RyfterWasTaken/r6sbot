import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

bot = discord.Bot()

greetings = bot.create_group("greetings", "Greet people")

@greetings.command()
async def hello(ctx):
  await ctx.respond(f"Hello, {ctx.author}!")

@greetings.command()
async def bye(ctx):
  await ctx.respond(f"Bye, {ctx.author}!")

bot.run(token)

