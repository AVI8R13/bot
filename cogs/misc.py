import discord
from discord.ext import commands
import random
from datetime import datetime
import qrcode
import requests
import config
from ping3 import ping


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx, *, target = "Bot"):
        latency = None
        if target == "Bot":
            latency = self.client.latency
        else:
            latency = ping(target)

        if latency < 0:
            pingEmbed = discord.Embed(
                title = "Pong!  :ping_pong:",
                description = f"{target} responded in {round(latency*1000)} ms!",
                color=discord.Color.blue()
            )
            await ctx.send(embed = pingEmbed)
        else:
            await ctx.send(f"{target} is unreachable, or is not a valid url.")

    @commands.command()
    async def roll(self, ctx, sides = 6):
        responses = [
            ":game_die: ***Throws dice aggressively***",
            ":game_die: Keep rollin', rollin', rollin', rollin' (uh)",
            ":game_die: *Throws dice*",
            ":game_die: You rolled a:",
            ":game_die: Your roll:",
            ":game_die: :game_die: :game_die:",
            ":game_die: haha dice go brrr"
            ]
        if sides >= 0:
            await ctx.send("Please enter a valid number of sides.")
        elif sides == None:
            sides = 6
        roll = random.randint(1, sides)
        rollEmbed = discord.Embed(
            title = random.choice(responses),
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
    async def eightball(self, ctx, *,question):
        responses = ["It is certain", "Without a doubt", "You may rely on it", "Yes, definately", "It is decidedly so", "As I see it, yes",
                     "Most Likely", "Yes", "Outlook good", "Signs point to yes", "Reply hazy try again", "Better not tell you now",
                       "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and try again", "Don't count on it",
                       "Outlook not good", "My sources say no", "Very doubtful", "My reply is no"]
        response = random.randint(0, len(responses))
        eightballEmbed = discord.Embed(
            title = f"Eight ball :8ball:"
        )
        eightballEmbed.add_field(name=question, value = responses[response], inline = True)
        await ctx.send(embed=eightballEmbed)
    
    @commands.command()
    async def qrcode(self, ctx, *, url):
        img = qrcode.make(url)
        img.save("qrcode.png")
        await ctx.send(f"QR code to {url}", file=discord.File("qrcode.png"))

    @commands.command()
    async def catfact(self, ctx):
        url = "https://catfact.ninja/fact"
        response = requests.get(url)
        if response.status_code == 200:
            fact=response.json()
            response = fact["fact"]
        else:
            response = "Error getting cat fact :<"

        catEmbed = discord.Embed(
            title = "Cat Fact :cat:",
            description=response,
            color = discord.Color.yellow()
        )
        await ctx.send(embed=catEmbed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        url = f"https://api.giphy.com/v1/gifs/random?api_key={config.giphyApiKey}&tag=anime+hug"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            url = data["data"]["url"]
            await ctx.send(f"{ctx.author} hugs {member}! \n{url}")
        else:
            await ctx.send("Failed to fetch a hug gif.")

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        url = f"https://api.giphy.com/v1/gifs/random?api_key={config.giphyApiKey}&tag=anime+kiss"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            url = data["data"]["url"]
            await ctx.send(f"{ctx.author} kisses {member}!\n{url}")
        else:
            await ctx.send("Failed to fetch a kiss gif.")

    @commands.command()
    async def eval(self, ctx, *, statement):
        response = str(eval(statement))
        await ctx.send(response)
        
async def setup(client):
    await client.add_cog(Misc(client))
