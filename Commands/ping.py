# This file is used to define the ping command for the disord bot.
# It's just a simple command used to determine if the bot is up and running.

# Importing the necessary libraries
import discord
from discord.ext import commands


# Defining the command with discord interaction api, commonly known as "slash commands"
# The function takes to arguments:
#   bot: a discord bot, it's used to avoid recusive importating
#   interaction: the interaction that user made with the discord bot in discord
async def ping_command(bot: commands.Bot, interaction: discord.Interaction):
    pass



