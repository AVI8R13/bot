import discord
from discord.ext import commands
import json
import os
import datetime
from manageCases import ManageCases

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = " "):
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
        elif reason == " ":
            reason = "No reason specified"

        banCase, kickCase= caseManger.getCases(caseType="ban")
        caseManger.updateCases(banCase, kickCase)

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
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = " "):
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
            return
        elif reason == " ":
            reason = "No reason specified"
        
        banCase, kickCase = caseManger.getCases(caseType="kick")
        caseManger.updateCases(banCase, kickCase)
            
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