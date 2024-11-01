import os
import discord
import asyncio
from siegeapi import Auth
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
bot = discord.Bot()

def format_xp(number):
  if number >= 1000:
    return f"{number/1000:.1f}k"
  else:
    return str(number)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

stats = discord.SlashCommandGroup("stats", "Rechercher les stats")

@bot.command(name="joueur")
async def player(ctx,
                 name: discord.Option(str, name="identifiant") = "CNDRD"):
    
    sentMsg = await ctx.respond("Loading")
    auth = Auth("8abdulhhanyj@gmail.com", "VNnyH8(NA-e@bB3")
    player = await auth.get_player(name=name)
    print(f"Name: {player.name}")
    print(f"Profile pic URL: {player.profile_pic_url}")

    await player.load_persona()
    print(f"Streamer nickname: {player.persona.nickname}")
    print(f"Nickname enabled: {player.persona.enabled}")

    await player.load_playtime()
    print(f"Total Time Played: {player.total_time_played:,} seconds / {player.total_time_played_hours:,} hours")
    print(f"Level: {player.level}")

    await player.load_ranked_v2()
    print(f"Ranked Points: {player.ranked_profile.rank_points}")
    print(f"Rank: {player.ranked_profile.rank}")
    print(f"Max Rank Points: {player.ranked_profile.max_rank_points}")
    print(f"Max Rank: {player.ranked_profile.max_rank}")

    await player.load_progress()
    print(f"XP: {player.xp:,}")
    print(f"Total XP: {player.total_xp:,}")
    print(f"XP to level up: {player.xp_to_level_up:,}")

    embed = discord.Embed(
        title=f"Statistiques de {player.name}",
        thumbnail=player.profile_pic_url,
        fields=[
            discord.EmbedField("Niveau",
                          f"> {player.level} \n> `{player.xp}`/{format_xp(player.xp + player.xp_to_level_up)} XP"
                          ,True),
            discord.EmbedField("Rang",
                          f"> Act: `{player.ranked_profile.rank}`(`{player.ranked_profile.rank_points}`pts)\n> Max: `{player.ranked_profile.max_rank}`(`{player.ranked_profile.max_rank_points}`pts)",
                          True)
        ]
    )
    await sentMsg.edit(content="", embed=embed)
    await auth.close()

bot.run(token)

