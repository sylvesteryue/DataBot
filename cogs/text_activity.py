import discord
from discord.ext import commands

class TextActivity(commands.Cog):
    def __init__(self, client):
        self.client = client

    
        @commands.Cog.listener()
        async def on_message(self, message):
            #keep track of messages here
            print(str(message.author) + " sent a message")


def setup(client):
    client.add_cog(TextActivity(client))