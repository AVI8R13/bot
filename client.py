import discord
from discord.ext import commands
import config
import os
from manageCasesNew import ManageDatabase

token = config.discordToken 
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="?", description="I just got so emo I fell apart.")

def config():
    if os.path.exists("data/") == False:
        os.mkdir("data")
        
config()

async def loadCogs():
    for fileName in os.listdir("./cogs"):
        if fileName.endswith(".py") and fileName != "manageCases.py":
            await client.load_extension(f'cogs.{fileName[:-3]}')
            print(f"{fileName[:-3]} cog loaded!")

@client.event
async def on_ready():
    print("Client is running!")
    await loadCogs()

@client.command()
async def load(ctx, extension):
    if extension == "all":
        for fileName in os.listdir("./cogs"):
            if fileName.endswith(".py") and fileName!= "manageCases.py":
                await client.load_extension(f'cogs.{fileName[:-3]}')
        await ctx.send(f'Cogs loaded.')
    else:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} loaded.')


@client.command()
async def unload(ctx, extension):
    if extension == "all":
        for fileName in os.listdir("./cogs"):
            if fileName.endswith(".py") and fileName!= "manageCases.py":
                await client.unload_extension(f'cogs.{fileName[:-3]}')
        await ctx.send(f'Cogs unloaded.')
    else:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog {extension} unloaded.')

try:
    client.run(token)
except:
    print("Plase paste your tokens and api keys in the tokens.json file")

#i use arch btw