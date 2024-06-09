# This file contains the functions used to connect the bot to the discord servers and make it available.

# Importing necessary libraries
import discord
from discord.ext import commands

# Create the ready function for the "on_ready" event
async def ready(bot: commands.Bot):
    # This function can be modified to say whatever you choose when the discord bot connects
    # or to do something when the bot connects to the discord servers.
    # For example the following print statments is used to notify that the bot is ready for use.
    print(f"<WRITE WHAT YOU WANT THE BOT TO SAY WHEN IT STARTS>")


