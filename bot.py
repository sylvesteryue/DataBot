import discord
import config
import os
import time

from discord.ext import commands

client  = commands.Bot(command_prefix=".")


if __name__ == "__main__":
	# for extension in config.STARTUP_COGS:
	# 	try:
	# 		client.load_extension(extension)
	# 		#extension = extension.replace("cogs.", "")
	# 		print(f"Loaded extension '{extension}'")
	# 	except Exception as e:
	# 		exception = f"{type(e).__name__}: {e}"
	# 		extension = extension.replace("cogs.", "")
	# 		print(f"Failed to load extension {extension}\n{exception}")
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			client.load_extension(f'cogs.{filename[:-3]}')

    
client.run(config.bot_token)