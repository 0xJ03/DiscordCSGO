import discord
import asyncio
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

class MyClient(Discord.client):
    async def on_ready(self):
        print("Logged on as:", self.user)
    
@bot.command()
async def test(ctx, arg):
if arg == "prisma":
    await ctx.send("Opening", arg, "case!")
    time.sleep(2)
    
    
    
bot.run(token)
        
        
