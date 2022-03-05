import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents, owner_id = owner_id)

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")
			with open("README.md", "r+") as log:
				filenameSyn = filename[:-3].upper().replace(".py", "")
				contents=log.read()
				if filenameSyn not in contents:
					if filenameSyn == "ONCOMMANDERROR":
						print("[WARNING] The cog 'OnCommandError' is not recommended to be used in production. It is only for debugging purposes.")
					log.write(f"`{filenameSyn}`\n")
					log.close()
					print(f"[INFO] Added {filenameSyn} to the README.md file.")
				else:
					print(f"[INFO] {filenameSyn} is already in the README.md file.")
		else:
			with open("log.txt", "a") as log:
				log.write(f"{filename} is not a .py file\n")
				log.close()

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)