#!/usr/bin/env python

import logging
import discord
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))
DISCORD_GUILD_ID = str(os.environ.get("DISCORD_GUILD_ID"))

# This example requires the 'message_content' intent.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name = "minecraft", description = "Manage Minecraft Server(s)", guild=discord.Object(id=DISCORD_GUILD_ID))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=DISCORD_GUILD_ID))
    print("Ready!")


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(DISCORD_TOKEN, log_handler=handler)

