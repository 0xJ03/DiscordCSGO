import discord
import asyncio
import time
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

async def main():
    conn = await asyncpg.connect('postgresql://postgres@localhost/test')
    await conn.execute('''
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')

@bot.event
async def on_ready():
    print('\nLogged in as')
    print("Bot Name: " + bot.user.name)
    print("Bot User ID: " + bot.user.id)

@bot.command()
async def help(ctx):
    await ctx.send("Use .case to open a case!")

@client.command() # add more of the same item to make it more common
@commands.cooldown(1, 4, commands.BucketType.user)
async def case(ctx):
    items = [
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "You get R8 Revolver - Bone Forged", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "MP5-SD - Desert Strike", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "AWP - Capillary", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "SG 553 - Darkwing", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "Glock-18 - Bullet Queen", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "Glock-18 - Bullet Queen", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "Glock-18 - Bullet Queen", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "Glock-18 - Bullet Queen", color = ctx.author.color),
    discord.Embed(title = "Item recieved", description = "Glock-18 - Bullet Queen", color = ctx.author.color),
    discord.Embed(title = "Item recieved!", description = "You get 5 :star: Skyward Atlas <:SkywardAtlas:857281156763746364> (Catalyst Weapon).", color = FFD700)]
    randomitem = random.choice(items)
    await ctx.send(embed=randomitem)

bot.run(token)
