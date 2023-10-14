import discord
from discord.ext import commands
import config
import os

token = config.token
intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="?", description="I just got so emo I fell apart.")

async def loadCogs():
    for fileName in os.listdir("./cogs"):
        if fileName.endswith(".py") and fileName != "manageCases.py":
            await client.load_extension(f'cogs.{fileName[:-3]}')
            print(f"{fileName[:-3]} cog loaded!")

@client.event
async def on_ready():
    print("Client is running!")
    await loadCogs()

client.run(token)