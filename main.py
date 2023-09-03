#!/usr/bin/env python

import discord
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))
#DISCORD_GUILD_ID = str(os.environ.get("DISCORD_GUILD_ID"))

bot = discord.Bot()

# create Slash Command group with bot.create_group
greetings = bot.create_group("greetings", "Greet people")

@greetings.command()
async def hello(ctx):
  await ctx.respond(f"Hello, {ctx.author}!")

@greetings.command()
async def bye(ctx):
  await ctx.respond(f"Bye, {ctx.author}!")

bot.run(DISCORD_TOKEN)

