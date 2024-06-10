# This file will be used to handle anything about the guilds that the discord bot has joined

# Importing necessary libraries
import discord
from discord.ext import commands

async def guild_join(bot: commands.Bot, guild: discord.Guild):
    pass

async def guild_left(bot: commands.Bot, guild:discord.Guild):
    pass

async def guild_channel_create(bot: commands.Bot, channel: discord.abc.GuildChannel):
    pass

async def guild_channel_delete(bot: commands.Bot, channel: discord.abc.GuildChannel):
    pass


