import discord
from discord.ext import commands
import random
from datetime import datetime

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        pingEmbed = discord.Embed(
            title = "Pong!  :ping_pong:",
            description = f"Responded in {round(self.client.latency*1000)} ms!",
            color=discord.Color.blue()
        )
        await ctx.send(embed = pingEmbed)

    @commands.command()
    async def roll(self, ctx, sides = 6):
        if sides == 0:
            await ctx.send("Please enter a valid number of sides.")
        elif sides == None:
            sides = 6
        else:
            sides == sides
        roll = random.randint(1, sides)
        rollEmbed = discord.Embed(
            title = "Your roll: ",
            description = roll,
            color = discord.Color.og_blurple()
        )
        await ctx.send(embed=rollEmbed)
    
    @commands.command()
    async def coinflip(self, ctx):
        result = random.randint(1,10000)
        if result%2 == 0:
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

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
    await client.add_cog(Misc(client))
