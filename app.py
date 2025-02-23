import os
import discord
import requests
import asyncio
import unittest
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv(".env")
TOKEN = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

API_URL = "https://v2.jokeapi.dev/joke/Any?lang={}"

def get_joke(language):
    response = requests.get(API_URL.format(language))
    joke_data = response.json()
    if joke_data["type"] == "single":
        return joke_data["joke"]
    else:
        return joke_data["setup"], joke_data["delivery"]

@bot.command()
async def chiste(ctx):
    joke = get_joke("es")
    if isinstance(joke, tuple):
        await ctx.send(f"{ctx.author.mention} {joke[0]}")
        await asyncio.sleep(2)
        await ctx.send(f"{ctx.author.mention} {joke[1]}")
    else:
        await ctx.send(f"{ctx.author.mention} {joke}")

@bot.command()
async def joke(ctx):
    joke = get_joke("en")
    if isinstance(joke, tuple):
        await ctx.send(f"{ctx.author.mention} {joke[0]}")
        await asyncio.sleep(2)
        await ctx.send(f"{ctx.author.mention} {joke[1]}")
    else:
        await ctx.send(f"{ctx.author.mention} {joke}")


bot.run(TOKEN)
