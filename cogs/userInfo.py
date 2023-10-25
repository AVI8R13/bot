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
            description = f"{member} joined discord on {created.strftime('%x')}",
            color = discord.Color.dark_blue()
        )
        await ctx.send(embed=createdEmbed)

    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        roles = [r.name for r in member.roles if r != ctx.guild.default_role]
        if len(roles) >= 30:
            roles = str("Too many to show.")
        else:
            roles = [r.mention for r in member.roles if r != ctx.guild.default_role]
        whoisEmbed = discord.Embed(
            title = member,
            color = discord.Color.blurple()
        )
        whoisEmbed.set_thumbnail(url = member.avatar)
        whoisEmbed.add_field(name = "Joined: ", value = member.joined_at.strftime('%Y-%m-%d'), inline=True)
        whoisEmbed.add_field(name = "Registered", value = member.created_at.strftime('%Y-%m-%d'), inline=True)
        whoisEmbed.add_field(name = f"Roles [{len(roles)}]", value = roles, inline = False)
        await ctx.send(embed=whoisEmbed)


async def setup(client):
    await client.add_cog(UserInfo(client))
