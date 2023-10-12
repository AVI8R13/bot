import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def pfp(self, ctx,*, member: discord.Member = None):
        if not member:
            member = ctx.author

        pfpEmbed = discord.Embed(
            title = f"{member}'s profile picture!",
            color= discord.Color.dark_blue()
        )
        pfpEmbed.set_image(url=member.avatar)
        await ctx.send(embed=pfpEmbed)

async def setup(client):
    await client.add_cog(UserInfo(client))
