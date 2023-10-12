import discord
from discord.ext import commands
import json
import os
import datetime


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.bot_has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = " "):
        if reason == " ":
            reason = "No reason given"
        elif not member:
            await ctx.send("No user specified!")
            return

        os.chdir(r'C:\Users\mario\Python Projects\bot\cogs\data')
        with open('caseCounts.json', 'r') as caseCounts:
            cases = json.load(caseCounts)
        banCase = int(cases['bans'])
        kickCase= int(cases['kicks'])
        banCase+=1
            
        with open('caseCounts.json', 'w') as updateCases:
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "lockdowns": 0
            }
            json.dump(cases, updateCases)

        banEmbed = discord.Embed(
            title = f"Ban case #{banCase}",
            color=discord.Color.orange()
        )
        
        banEmbed.add_field(name=f"{member} has been banned.", value=" ", inline=False)
        banEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        banEmbed.add_field(name=f"Banned by:", value=ctx.author, inline=True)
        await ctx.send(embed = banEmbed)
        await member.ban(reason=reason)
        
    @commands.command()
    @commands.bot_has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = " "):
        if reason == " ":
            reason = "No reason given."
        elif not member:
            await ctx.send("No user specified.")
            return
        
        os.chdir(r'C:\Users\mario\Python Projects\bot\cogs\data')
        with open('caseCounts.json', 'r') as caseCounts:
            cases = json.load(caseCounts)

        kickCase = int(cases['kicks'])
        banCase = int(cases['bans'])
        kickCase+=1
        
        with open('caseCounts.json', 'w') as updateCases:
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "lockdowns": 0
            }
            json.dump(cases, updateCases)

            kickEmbed = discord.Embed(
            title = f"Kick case #{kickCase}",
            color=discord.Color.orange()
        )
        
        kickEmbed.add_field(name=f"{member} has kicked.", value=" ", inline=False)
        kickEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        kickEmbed.add_field(name=f"Kicked by:", value=ctx.author, inline=True)
        await ctx.send(embed = kickEmbed)
        await member.kick(reason=reason)
               
async def setup(client):
    await client.add_cog(Moderation(client))

print("test")
print('ets2')
