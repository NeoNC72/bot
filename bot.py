import discord
from discord.ext import commands
import random
import argparse
import numpy as np
import time
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print('------')


@client.command()
async def ping(ctx):
    await ctx.send(f"Latency is {round(client.latency * 1000)} ms")


@client.command()
async def racism(ctx):
    await ctx.send("@nice#2618")


@client.command(aliases=["?"])
async def ask(ctx, *, question):
    responses=["Yes", "No"]
    await ctx.send(f"{question}\nAnswer is {random.choice(responses)}")


@client.command()
async def idk(ctx):
    embed = discord.Embed(title="ok", url="http://www.pornhub.com", description="ok", color=0xff0000)
    embed.set_author(name="neon")
    embed.add_field(name="ok", value="nigger", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@client.command()
async def rng(ctx, stop: int, amount=1):
    for i in range(amount):
        await ctx.send(random.randrange(stop))


@client.command()
async def test(ctx, maxx: int, step: int, startt: int):
    await ctx.send("working")
    a = []
    avgg=[]

    def sortbench(x):
        for i in range(x):
            a.append(i)
        print(x)
        print("shuffling....")
        start = time.time()
        np.random.shuffle(a)
        end=time.time()
        timeend=str(end-start)
        print(f"done in {timeend} s")
        print("sorting....")
        start=0
        end=0
        start = time.time()
        sort=sorted(a)
        end=time.time()
        timeend=str(end-start)
        print(f"done in {timeend} s")
        return float(timeend)
        return(x)
    for i in np.arange(startt, maxx, step):
        avgg.append(sortbench(i))
    print("fastest was:")
    print(min(avgg))
    print("slowest was:")
    print(max(avgg))
    idk2=max(avgg)
    idk1=min(avgg)
    await ctx.send(f'{idk1}s was lowest time and {idk2}s was slowest time')
client.run("NzY5NTM3ODkwNjI3MzU0NjY1.X5QeAg.fTAbdNbcYAacw30sjkwbulDYhL0")





