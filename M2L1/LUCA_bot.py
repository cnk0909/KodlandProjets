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
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    "Chooses between multiple choices."
    await ctx.send(random.choice(choices))

@bot.command(name="Bana bır resım verır mısın?")
async def mem(ctx):
    with open('M2L1\images\Imagekatil.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    memes = os. listdir('M2L1/images')
    image_name = random.choice(memes)
    with open(f'M2L1/images/{image_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


@bot.command()
async def random_mem2(ctx):
    memes = os.listdir('M2L1/images2')
    image_name = random.choice(memes)
    with open(f'M2L1/images2/{image_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run(TOKEN)