#!/usr/bin/env python

import json
import logging
import os

import discord
import requests
from dotenv import load_dotenv

# Load configuration from environment variables/.env file
load_dotenv()
DISCORD_TOKEN = str(os.environ.get("DISCORD_TOKEN"))
API_SERVER = str(os.environ.get("API_SERVER"))
DEFAULT_SERVER = str(os.environ.get("DEFAULT_SERVER"))

logging.basicConfig(level=logging.INFO)

# prepare bot
bot = discord.Bot()


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")


# create commands/command group
minecraft = discord.SlashCommandGroup("minecraft", "Manage Minecraft server(s).")
server_desc = "Server to target."


@minecraft.command()
async def list(ctx):
    """
    Get the list of Minecraft servers available to manage.
    """
    logging.info(f"{ctx.author} issued command: list")

    response = requests.get(API_SERVER + "/list")
    json_data = json.loads(response.text)
    server_list = json_data["message"]

    output = "Available servers:"
    for server in server_list:
        if server == DEFAULT_SERVER:
            output += f"\n- {server['name']} (default)"
        else:
            output += f"\n- {server['name']}"
        output += f"\n  version: {server['data']['version']}"

    logging.info(output)
    await ctx.respond(output)


@minecraft.command()
async def start(
    ctx,
    server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER),
):
    """
    Start the Minecraft server
    """
    logging.info(f"{ctx.author} issued command: start")
    logging.info(f"(arg) server: {server}")

    response = requests.get(API_SERVER + "/list")
    json_data = json.loads(response.text)
    server_list = json_data["message"]

    if not any(i["name"] == server for i in server_list):
        logging.warn(f"Server ({server}) not in list of servers.")
        await ctx.respond(f"Server ({server}) not in list of servers.")
        return

    post_body = {"server": server}
    response = requests.post(API_SERVER + "/start", json=post_body)
    json_data = json.loads(response.text)
    message = json_data["message"]
    logging.info(message)
    await ctx.respond(message)


@minecraft.command()
async def stop(
    ctx,
    server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER),
):
    """
    Stop the Minecraft server
    """
    logging.info(f"{ctx.author} issued command: stop")
    logging.info(f"(arg) server: {server}")

    response = requests.get(API_SERVER + "/list")
    json_data = json.loads(response.text)
    server_list = json_data["message"]

    if not any(i["name"] == server for i in server_list):
        logging.warn(f"Server ({server}) not in list of servers.")
        await ctx.respond(f"Server ({server}) not in list of servers.")
        return

    post_body = {"server": server}
    response = requests.post(API_SERVER + "/stop", json=post_body)
    json_data = json.loads(response.text)
    message = json_data["message"]
    logging.info(message)
    await ctx.respond(message)


@minecraft.command()
async def extendtime(
    ctx,
    server: discord.Option(str, server_desc, required=False, default=DEFAULT_SERVER),
    days: discord.Option(
        int, "How many days to keep the server running.", required=False, default=1
    ),
):
    """
    Extend how long the Minecraft server stays running
    """
    logging.info(f"{ctx.author} issued command: extendtime")
    logging.info(f"(arg) server: {server}")
    logging.info(f"(arg) days: {days}")

    response = requests.get(API_SERVER + "/list")
    json_data = json.loads(response.text)
    server_list = json_data["message"]

    if not any(i["name"] == server for i in server_list):
        logging.warn(f"Server ({server}) not in list of servers.")
        await ctx.respond(f"Server ({server}) not in list of servers.")
        return

    if days < 1 or days > 30:
        logging.info(f"Days ({days}) outside of accepted range 1-30.")
        await ctx.respond(f"Days ({days}) outside of accepted range 1-30.")
        return

    post_body = {"server": server, "days": days}
    response = requests.post(API_SERVER + "/extendtime", json=post_body)
    json_data = json.loads(response.text)
    message = json_data["message"]
    logging.info(message)
    await ctx.respond(message)


# main
bot.add_application_command(minecraft)
bot.run(DISCORD_TOKEN)
