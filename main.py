#!/usr/bin/env python3.12

# This is the main file that will connect the discord bot with everything else
# in the project from events to functions to commands.

# Importing the necessary libraries
import discord
from discord.ext import commands
import time
import os

# Importing the bots libraries and functions
from Events.ready import *
from Events.guild import *
from Events.member import *
from Commands.ping import ping_command
from .config import token

# Initialising the bot intents
intents = discord.Intents.all()

# Creating the bot
bot = commands.Bot(command_prefix="?", intents=intents)

# Connecting the events in the "Events" folder to the bot client
@bot.event
async def on_ready():
    pass

@bot.event
async def on_guild_join(guild: discord.Guild):
    pass

@bot.event
async def on_guild_remove(guild: discord.Guild):
    pass

# Connecting the commands in the "Commands" folder to the bot client





# Running the bot instence
bot.run(token=token)

