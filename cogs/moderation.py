import discord
from discord.ext import commands
from manageCases import ManageCases
import json

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):
        id = ctx.message.guild.id
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
        elif reason is None:
            reason = "No reason specified"

        banCase, kickCase, warnCase, lockdownCase = caseManger.getCases(caseType="ban", serverID= id)
        caseManger.updateCases(banCase, kickCase, warnCase, lockdownCase)
        caseManger.logCases(serverID=id, member=member, caseType="ban", reason = reason, banCase=banCase, kickCase= kickCase, warnCase=warnCase, lockdownCase=lockdownCase)


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
    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        id = ctx.message.guild.id
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
            return
        elif reason is None:
            reason = "No reason specified"
        
        banCase, kickCase, warnCase, lockdownCase = caseManger.getCases(caseType="kick", serverID=id)
        caseManger.updateCases(banCase, kickCase, warnCase, lockdownCase, serverID=id)
        caseManger.logCases(serverID=id, member=member, caseType="kick", reason = reason, banCase=banCase, kickCase= kickCase, warnCase=warnCase, lockdownCase=lockdownCase)
            
        kickEmbed = discord.Embed(
        title = f"Kick case #{kickCase}",
        color=discord.Color.orange()
        )
        kickEmbed.add_field(name=f"{member} has kicked.", value=" ", inline=False)
        kickEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        kickEmbed.add_field(name=f"Kicked by:", value=ctx.author, inline=True)
        await ctx.send(embed = kickEmbed)
        await member.kick(reason=reason)
    
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member = None, *, reason = None):
        id = ctx.message.guild.id
        userID = member.id
        caseManager = ManageCases()
        if member is None:
            await ctx.send("No member specified")
            return
        elif reason is None:
            reason = "No reason specified"

        banCase, kickCase, warnCase, lockdownCase = caseManager.getCases(caseType="warn", serverID=id)
        caseManager.updateCases(banCase, kickCase, warnCase, lockdownCase, serverID=id)
        caseManager.logCases(serverID=id, member=member, caseType="warn", reason=reason, banCase=banCase, kickCase=kickCase, warnCase=warnCase, lockdownCase=lockdownCase)

        warnEmbed = discord.Embed(
        title = f"Warn case #{warnCase}",
        color=discord.Color.orange()
        )
        warnEmbed.add_field(name=f"{member} has been warned.", value=" ", inline=False)
        warnEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        warnEmbed.add_field(name=f"Warned by:", value=ctx.author, inline=True)
        await ctx.send(embed = warnEmbed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def getcase(self, ctx, search):
        id = ctx.guild.id
        result = None

        try:
            with open(f'data/{id}_Cases.json', 'r') as cases:
                data = json.load(cases)
                for case in data:
                    if "Case" in case and case["Case"] == search or "Member" in case and case["Member"] == search:
                        result = case
        except FileNotFoundError:
            await ctx.send("No logs found for this server.")
            return

        if result is not None:
            caseEmbed = discord.Embed(
                title=f"{result['Member']}'s {result['Case'][:-1]} case",
                color = discord.Color.blue()
            )
            caseEmbed.add_field(name="Case", value=result["Case"], inline=True)
            caseEmbed.add_field(name="Reason", value=result["Reason"], inline=True)
            caseEmbed.add_field(name="Date", value=result["Date"], inline=False)
            caseEmbed.add_field(name="Time", value=result["Time"], inline=False)
            await ctx.send(embed=caseEmbed)
        else:
            await ctx.send("Case not found")

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
        id = ctx.message.guild.id
        caseManager = ManageCases()
        if reason is None:
            reason = "No reason specified"

        banCase, kickCase, warnCase, lockdownCase = caseManager.getCases(caseType="warn", serverID=id)
        caseManager.updateCases(banCase, kickCase, warnCase, lockdownCase, serverID=id)
        caseManager.logCases(serverID=id, member=member, caseType="warn", reason=reason, banCase=banCase, kickCase=kickCase, warnCase=warnCase, lockdownCase=lockdownCase)
        
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