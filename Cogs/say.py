import discord
from discord.ext import commands
import time


class sayCog(commands.Cog, name="say command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "say",
					usage="<msg type> <message>",
					aliases=["Say"],
					description = "Say something using the bot!")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def say(self, ctx, msg_type, *, message):
		if msg_type == "embed":
			embed = discord.Embed(title="Say", color=0x00ff00)
			embed.add_field(name="Message", value=message)
			await ctx.send(embed=embed)
		elif msg_type == "text":
			await ctx.send(message)
		else:
			await ctx.send("Invalid message type. Available types: `embed`, `text`")
def setup(bot:commands.Bot):
	bot.add_cog(sayCog(bot))