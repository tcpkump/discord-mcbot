#!/usr/bin/env python

import discord
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))
#DISCORD_GUILD_ID = str(os.environ.get("DISCORD_GUILD_ID"))

bot = discord.Bot()

# create Slash Command group with bot.create_group
minecraft= bot.create_group("minecraft", "Manage Minecraft Server(s)")

@minecraft.command()
async def status(ctx):
    """Get the Minecraft Server Status"""
    await ctx.respond(f"{ctx.author}, the mc server is doing great.")

@minecraft.command()
async def start(ctx):
    """Start the Minecraft Server"""
    await ctx.respond(f"{ctx.author}, the mc server has been started.")

@minecraft.command()
async def stop(ctx):
    """Stop the Minecraft Server"""
    await ctx.respond(f"{ctx.author}, the mc server has been stopped.")

bot.run(DISCORD_TOKEN)

