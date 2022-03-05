import discord
from discord.ext import commands
import time
import json

class inviteCog(commands.Cog, name="invite command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "invite", 
					usage="", 
					aliases=["Invite"], 
					description = "Invite the bot!")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def invite(self, ctx):
		# open config.json and get the bot's invite link
		with open("configuration.json", "r") as f:
			config = json.load(f)
			invite_link = config["invite_link"]
		await ctx.send(invite_link)

def setup(bot:commands.Bot):
	bot.add_cog(inviteCog(bot))