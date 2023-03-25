import discord
import os
import time

from discord.ext import commands

client = commands.Bot(command_prefix=".")


if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')