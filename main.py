#!/usr/bin/env python

import discord
import os

from dotenv import load_dotenv

# Load configuration from environment variables/.env file
load_dotenv()
DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))
DEFAULT_SERVER = str(os.environ.get("DEFAULT_SERVER"))

# prepare bot
bot = discord.Bot()
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# create commands/command group
minecraft = discord.SlashCommandGroup("minecraft", "Manage Minecraft server(s).")
server_desc = "Server to target."

@minecraft.command()
async def list(ctx):
    """
    Get the list of Minecraft servers available to manage.
    """
    await ctx.respond(f"{ctx.author}, the mc server is doing great.")

@minecraft.command()
async def status(ctx, server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER)):
    """
    Get Minecraft server status.
    """
    await ctx.respond(f"{ctx.author}, the mc server {server} is doing great.")

@minecraft.command()
async def start(ctx, server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER)):
    """
    Start the Minecraft server
    """
    await ctx.respond(f"{ctx.author}, the mc server {server} has been started.")

@minecraft.command()
async def stop(ctx, server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER)):
    """
    Stop the Minecraft server
    """
    await ctx.respond(f"{ctx.author}, the mc server {server} has been stopped.")


# main
bot.add_application_command(minecraft)
bot.run(DISCORD_TOKEN)

