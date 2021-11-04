import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

class MyClient(Discord.client):
    async def on_ready(self):
        print("Logged on as:", self.user)
        


bot.run(token)
        
        
