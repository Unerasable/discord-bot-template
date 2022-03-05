from ast import alias
import discord
from discord.ext import commands
import time


class StatsCog(commands.Cog, name="Stats command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "stats",
					usage="",
					aliases=["stats"],
					description = "Display the bot's Stats.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def Stats(self, ctx):
		embed = discord.Embed(title="Stats", color=0x00ff00)
		embed.add_field(name="Servers", value=len(self.bot.guilds))
		embed.add_field(name="Users", value=len(self.bot.users))
		embed.add_field(name="Channels", value=len(self.bot.channels))
		embed.add_field(name="Users Online", value=len(self.bot.users))
		embed.add_field(name="Memory Usage", value=str(self.bot.process.memory_full_info().rss/1000000)+"MB")
		embed.add_field(name="CPU Usage", value=str(self.bot.process.cpu_percent())+"%")
		embed.add_field(name="Uptime", value=str(self.bot.uptime))
		embed.add_field(name="Latency", value=str(self.bot.latency))
		embed.add_field(name="Version", value=discord.__version__)
		embed.add_field(name="Python Version", value=discord.__version__)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(StatsCog(bot))