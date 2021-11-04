import discord
import asyncio
import time
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
    discord.Embed(title = "Wish Successfull", description = "You get 3 :star: Ebony Bow <:EbonyBow:857220938571317248> (Bow Weapon).", color = ctx.author.color), 
    discord.Embed(title = "Wish Successfull", description = "You get 3 :star: Raven Bow <:RavenBow:857221178338574357> (Bow Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 3 :star: Recurve Bow <:RecurveBow:857221810932547594> (Bow Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 4 :star: Alley Hunter <:AlleyHunter:857262273805287434> (Bow Weapon).", color = ctx.author.color), 
    discord.Embed(title = "Wish Successfull", description = "You get 4 :star: Blackcliff Warbow <:BlackcliffWarbow:857262272656441345> (Bow Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 4 :star: Compound Bow <:CompoundBow:857262272622493736> (Bow Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 5 :star: Lost Prayer to the Sacred Winds <:LostPrayertotheSacredWinds:857281184492552213> (Catalyst Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 5 :star: Memory of Dust <:MemoryofDust:857281131413635122> (Catalyst Weapon).", color = ctx.author.color),
    discord.Embed(title = "Wish Successfull", description = "You get 5 :star: Skyward Atlas <:SkywardAtlas:857281156763746364> (Catalyst Weapon).", color = ctx.author.color)]
    randomitem = random.choice(items)
    await ctx.send(embed=randomitem)

    
    
    
bot.run(token)
        
        
