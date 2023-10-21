import discord
from discord.ext import commands
from manageCases import ManageCases
import json

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = " "):
        id = ctx.message.guild.id
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
        elif reason == " ":
            reason = "No reason specified"

        banCase, kickCase, warnCase = caseManger.getCases(caseType="ban", serverID= id)
        caseManger.updateCases(banCase, kickCase)
        caseManger.logCases(serverID=id, member=member, caseType="ban", reason = reason, banCase=banCase, kickCase= kickCase, warnCase=warnCase)


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
        id = ctx.message.guild.id
        caseManger = ManageCases()
        if member is None:
            await ctx.send("No member specified")
            return
        elif reason == " ":
            reason = "No reason specified"
        
        banCase, kickCase, warnCase, lockdownCase = caseManger.getCases(caseType="kick", serverID=id)
        caseManger.updateCases(banCase, kickCase, warnCase, lockdownCase, serverID=id)
        caseManger.logCases(serverID=id, member=member, caseType="kick", reason = reason, banCase=banCase, kickCase= kickCase, warnCase=warnCase)
            
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
    async def warn(self, ctx, member: discord.Member = None, *, reason= " "):
        id = ctx.message.guild.id
        userID = ctx.message.member.id
        caseManager = ManageCases()
        if member is None:
            await ctx.send("No member specified")
            return
        elif reason == " ":
            reason = "No reason specified"

        banCase, kickCase, warnCase = caseManager.getCases(caseType="warn", serverID=id)
        caseManager.updateCases(banCase, kickCase, warnCase, serverID=id)
        caseManager.logCases(serverID=id, member=member, caseType="warn", reason=reason, banCase=banCase, kickCase=kickCase, warnCase=warnCase)
        caseManager.logUserWarns(userID=userID, serverID=id, member = member, reason = reason, userWarnCase='0')

        warnEmbed = discord.Embed(
        title = f"Warn case #{warnCase}",
        color=discord.Color.orange()
        )
        warnEmbed.add_field(name=f"{member} has been warned.", value=" ", inline=False)
        warnEmbed.add_field(name=f"Reason:", value = reason, inline=True)
        warnEmbed.add_field(name=f"Warned by:", value=ctx.author, inline=True)
        await ctx.send(embed = warnEmbed)

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def lockdown(self, ctx, *,reason = " "):
        caseManager = ManageCases()
        member = ctx.author
        if reason == " ":
            reason = "No reason specified."
        role = discord.Guild.default_role
        await role.edit(permissions=discord.permissions(send_messages = "False"))
        banCase, kickCase, warnCase, lockdownCase = caseManager.getCases(caseType = "lockdown", serverID = id)
        caseManager.updateCases(banCase, kickCase, warnCase, lockdownCase, serverID = id)
        caseManager.logCases(serverID=id, member=member, caseType="lockdown", reason = reason, banCase=banCase, kickCase= kickCase, warnCase=warnCase)
        lockdownEmbed=discord.Embed(
            title= f"Lockdown Case #{lockdownCase}",
            color = discord.Colour.red()
        )
        lockdownEmbed.add_field(name = f"{ctx.channel} has been locked down.", value = " ", inline =- False)
        lockdownEmbed.add_field(name = "Reason:,", value=reason, inline=True)
        lockdownEmbed.add_field(name = "Warned by:,", value=ctx.author, inline=True)
        

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def getcase(self, ctx, search):
        id = ctx.guild.id
        result = None

        with open(f'data/{id}_Cases.json', 'r') as cases:
            data = json.load(cases)
            for case in data:
                if "Case" in case and case["Case"] == search or "Member" in case and case["Member"] == search:
                    result = case

        if result is not None:
            caseEmbed = discord.Embed(
                title=f"{result['Member']}'s {result['Case'][:-2]} case",
                color = discord.Color.blue()
            )
            caseEmbed.add_field(name="Case:", value=result["Case"])
            caseEmbed.add_field(name="Reason:", value=result["Reason"])
            await ctx.send(embed=caseEmbed)
        else:
            await ctx.send("Case not found")
      
async def setup(client):
    await client.add_cog(Moderation(client))