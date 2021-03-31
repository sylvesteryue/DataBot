import discord
from discord.ext import commands
import utils.db

class TextActivity(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        #keep track of messages here
        print(str(message.author) + " sent a message")
        utils.db.add_member_text_activity(message.guild.id, message.author.id, message.channel.id)

def setup(client):
    client.add_cog(TextActivity(client))