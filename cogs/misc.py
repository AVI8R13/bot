import discord
from discord.ext import commands
import random
import datetime

class Misc:
    def __init__(self, client):
        self.client = client
    
    @commands.command
    async def ping(self, ctx):
        pingEmbed = discord.Embed(
            header = "Pong!",
            description = f"Responded in {round(self.latency*1000)} ms!"
        )
        pingEmbed.set_footer(datetime.datetime.now())

