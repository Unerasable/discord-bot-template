import discord
from discord.ext import commands
import time


class servericonCog(commands.Cog, name="servericon command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "servericon",
					usage="",
					aliases=["Servericon", "ServerIcon","serverico"],
					description = "")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def servericon(self, ctx):
		#create embed
		embed = discord.Embed(title="Server Icon", color=0x00ff00)
		embed.add_field(name="Server Name", value=ctx.guild.name)
		embed.add_field(name="Server Owner", value=ctx.guild.owner)
		embed.set_image(url=ctx.guild.icon_url)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(servericonCog(bot))