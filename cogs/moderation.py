import discord
from discord.ext import commands
import json
import os


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.bot_has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = " "):
        if reason == " ":
            reason = "No reason given"
        elif not member:
            await ctx.send("No user given!")
        
        os.chdir(r'C:\Users\mario\Python Projects\bot\cogs\data')
        with open('caseCounts.json', 'r') as caseCounts:
            cases = json.load(caseCounts)
        banCase = int(cases['bans'])
        banCase+=1
        
        with open('caseCounts.json', 'w') as updateCases:
            json.dump(updateCases, banCase=updateCases['bans'])

        banEmbed = discord.Embed(
            title = f"Ban case #{banCase}",
            description=f"{member} was banned with reason '{reason}' by {ctx.author}."
        )
        await ctx.send(emebd = banEmbed)
        await member.ban(reason=reason)



async def setup(client):
    await client.add_cog(Moderation(client))       
