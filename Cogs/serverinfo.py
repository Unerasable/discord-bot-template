import discord
from discord.ext import commands
import time


class serverinfoCog(commands.Cog, name="serverinfo command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "serverinfo",
					usage="",
					aliases=["Serverinfo", "ServerInfo","si"],
					description = "")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def serverinfo(self, ctx):
		embed = discord.Embed(title="Server Info", color=0x00ff00)
		embed.add_field(name="Server Name", value=ctx.guild.name)
		embed.add_field(name="Server ID", value=ctx.guild.id)
		embed.add_field(name="Server Owner", value=ctx.guild.owner)
		embed.add_field(name="Server Region", value=ctx.guild.region)
		embed.add_field(name="Server Created At", value=ctx.guild.created_at)
		embed.add_field(name="Server Members", value=ctx.guild.member_count)
		embed.add_field(name="Server Channels", value=len(ctx.guild.channels))
		embed.add_field(name="Server Roles", value=len(ctx.guild.roles))
		embed.add_field(name="Server Embeds", value=ctx.guild.embed_enabled)
		embed.add_field(name="Server Version", value=ctx.guild.version)
		embed.add_field(name="Server AFK Timeout", value=ctx.guild.afk_timeout)
		embed.add_field(name="Server AFK Channel", value=ctx.guild.afk_channel)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		try:
			#try to set the server banner as the image
			embed.set_image(url=ctx.guild.banner_url)
		except:
			#if the server banner is not set, set the default image
			pass
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(serverinfoCog(bot))