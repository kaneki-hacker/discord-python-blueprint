# This file contains the functions that are used to fetch different type of data from the discord bot.

# Importing the necessary libraries
import discord
from discord.ext import commands

async def sync_commands(bot: commands.Bot):
    # This functions is responsible of syncing all the bot's slash commands and needs to be implimented so the discord bot works
    try:
        synced = await bot.tree.sync()
        print(f"Synced successfully {len(synced)} commands!")
    except Exception as e:
        print(f"An error has occured while syncing the commands: {e}")
        
