#!/usr/bin/env python3.12

# This is the main file that will connect the discord bot with everything else
# in the project from events to functions to commands.

# Importing the necessary libraries
import discord
from discord.ext import commands
from discord import app_commands
import time
import os

# Importing the bots libraries and functions
from Events.ready import ready
from Events.guild import *
from Events.member import *
from Commands.ping import ping_command
from Commands.help import help_command

from Functions.fetch import sync_commands
from .config import token

# Initialising the bot intents
intents = discord.Intents.all()

# Creating the bot
bot = commands.Bot(command_prefix="?", intents=intents)

# Connecting the events in the "Events" folder to the bot client
@bot.event
async def on_ready():
    await sync_commands(bot)
    await ready(bot)

@bot.event
async def on_guild_join(guild: discord.Guild):
    pass

@bot.event
async def on_guild_remove(guild: discord.Guild):
    pass

# Connecting the commands in the "Commands" folder to the bot client

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await help_command(bot, interaction)

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await ping_command(bot, interaction)

# Running the bot instence
bot.run(token=token)

