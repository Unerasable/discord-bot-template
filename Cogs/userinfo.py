import time

import discord
from discord.ext import commands


class userinfoCog(commands.Cog, name="userinfo command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "userinfo",
					usage="<user>",
					aliases=["UserInfo","Userinfo","ui"],
					description = "")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def userinfo(self, ctx, *, user:discord.Member=None):
		if user is None:
			user = ctx.author
		#create embed
		embed = discord.Embed(title="User Info", color=0x00ff00)
		embed.add_field(name="User Name", value=user.name)
		embed.add_field(name="User ID", value=user.id)
		embed.add_field(name="User Discriminator", value=user.discriminator)
		embed.add_field(name="User Status", value=user.status)
		embed.add_field(name="User Activity", value=user.activity)
		embed.add_field(name="User Created At", value=user.created_at)
		embed.add_field(name="User Joined At", value=user.joined_at)
		embed.add_field(name="User Top Role", value=user.top_role)
		embed.add_field(name="User Bot", value=user.bot)
		embed.add_field(name="User Avatar URL", value=user.avatar_url)

def setup(bot:commands.Bot):
	bot.add_cog(userinfoCog(bot))
