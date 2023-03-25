import discord
import discord.ext
import utils.db

class TextActivity(discord.ext.commands.Cog):
    def init(self, client):
        self.client = client


    @discord.ext.commands.Cog.listener()
    async def on_message(self, message):
        #keep track of messages here
        print(str(message.author) + " sent a message")


def setup(client):
    client.add_cog(TextActivity(client))