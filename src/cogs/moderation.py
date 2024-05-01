import discord
from discord.ext import commands
from datetime import datetime
from src.ManageDatabase import ManageDatabase

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.databaseManager = ManageDatabase()

    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):
        userID = member.id
        modID = ctx.author.id
        serverID = ctx.message.guild.id
        self.databaseManager.createDb(serverID)

        if reason is None:
            reason = "No reason specified"
        
        caseInfo = {
            "userID": userID,
            "responsibleModerator": modID,
            "caseType": "bans",
            "reason": reason,
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%H:%M:%S")
        }

        try:
            banCaseNumber = self.databaseManager.getCases(serverID, caseInfo["caseType"])
            self.databaseManager.updateCases(caseInfo, serverID)
        except Exception as e:
            print(f"Error accessing database:\n{e}")
            await ctx.send(f"Error accessing database. Ban has still been processed.")

        banEmbed = discord.Embed(
            title = f"Ban case #{banCaseNumber}",
            color=discord.Color.orange()
        )
        banEmbed.add_field(name=f"{member} has been banned.", value=" ", inline=False)
        banEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        banEmbed.add_field(name=f"Banned by:", value=ctx.author, inline=True)
        await ctx.send(embed = banEmbed)
        await member.ban(reason=reason)


    @commands.command()
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        userID = member.id
        modID = ctx.author.id
        serverID = ctx.message.guild.id
        self.databaseManager.createDb(serverID)

        if reason is None:
            reason = "No reason specified"
        
        caseInfo = {
            "userID": userID,
            "responsibleModerator": modID,
            "caseType": "kicks",
            "reason": reason,
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%H:%M:%S")
        }

        try:
            kickCaseNumber = self.databaseManager.getCases(serverID, caseInfo["caseType"])
            self.databaseManager.updateCases(caseInfo, serverID)
        except Exception as e:
            print(f"Error accessing database:\n{e}")
            await ctx.send(f"Error accessing database. Kick has still been processed.")

        kickEmbed = discord.Embed(
            title = f"Kick case #{kickCaseNumber}",
            color=discord.Color.orange()
        )
        kickEmbed.add_field(name=f"{member} has been kicked.", value=" ", inline=False)
        kickEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        kickEmbed.add_field(name=f"Kicked by:", value=ctx.author, inline=True)
        await ctx.send(embed = kickEmbed)
        await member.kick(reason=reason)
    
    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def purge(self, ctx, amount = 25, *, reason= None):
        if reason is None:
            reason = "No reason specified"
        await ctx.channel.purge(limit = amount)
        purgeEmbed = discord.Embed(
            title = f"Purged {amount} messages",
            color = discord.Color.orange()
        )
        purgeEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        purgeEmbed.add_field(name=f"Purged by:", value = ctx.author, inline=True)
        await ctx.send(embed=purgeEmbed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def lockdown(self, ctx, *, reason= None):
        userID = ''
        modID = ctx.author.id
        serverID = ctx.message.guild.id
        self.databaseManager.createDb(serverID)

        if reason is None:
            reason = "No reason specified"
        
        caseInfo = {
            "userID": userID,
            "responsibleModerator": modID,
            "caseType": "bans",
            "reason": reason,
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%H:%M:%S")
        }

        try:
            lockdownCaseNumber = self.databaseManager.getCases(serverID, caseInfo["caseType"])
            self.databaseManager.updateCases(caseInfo, serverID)
        except Exception as e:
            print(f"Error accessing database:\n{e}")
            await ctx.send(f"Error accessing database. Lockdown has still been processed.")

        lockdownEmbed = discord.Embed(
            title = f"{ctx.channel.mention} has been locked!",
            color = discord.Color.orange()
        )
        lockdownEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        lockdownEmbed.add_field(name=f"Locked by:", value = ctx.author, inline=True)
        await ctx.send(embed=lockdownEmbed)
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)


    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def unlock(self, ctx, *, reason= None):
        if reason is None:
            reason = "No reason specified"
        lockdownEmbed = discord.Embed(
            title = f"{ctx.channel.mention} has been unlocked!",
            color = discord.Color.orange()
        )
        lockdownEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        lockdownEmbed.add_field(name=f"Unlocked by:", value = ctx.author, inline=True)
        await ctx.send(embed=lockdownEmbed)
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)

async def setup(client):
    await client.add_cog(Moderation(client))