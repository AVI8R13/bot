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

    @commands.command()
    async def created(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        
        created = member.created_at
        
        createdEmbed = discord.Embed(
            title = f"{member}'s account creation date!",
            description = f"{member} joined discord on {created.strftime('%x')}"
        )
        await ctx.send(embed=createdEmbed)

    # @commands.command()
    # async def joined(self, ctx, member: discord.Member = None):
    #     if not member:
    #         member = ctx.author

    #     joined = member.joined_at
    #     guildName = discord.Guild.name()

    #     joinEmbed = discord.Embed(
    #         title = f"{member}'s join date!",
    #         description= f"{member} joined {member.uild.name} on {joined.strftime('%x')}",
    #         color= discord.Color.dark_blue()
    #     )
    #     await ctx.send(embed=joinEmbed)





async def setup(client):
    await client.add_cog(UserInfo(client))
