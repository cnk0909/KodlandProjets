import discord
from discord.ext import commands
import random
from bot_token import TOKEN
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def plastik(ctx):
    await ctx.send("geri dönüşüme atabilirsin        , saksi olarak kullanabilirsin          , bişey yaparken kullanabilirsin")

@bot.command()
async def metal(ctx):
    await ctx.send("geri dönüşüme atabilirsin        , saksi olarak kullanabilirsin          , bişey yaparken kullanabilirsin")

@bot.command()
async def cam(ctx):
    await ctx.send("geri dönüşüme atabilirsin        , kavanoz yabilirsin         , bişey yaparken kullanabilirsin")

@bot.command()
async def pil(ctx):
    await ctx.send("geri dönüşüme atabilirsin          , bişey yaparken kullanabilirsin")




bot.run(TOKEN)