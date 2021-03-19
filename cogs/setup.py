import discord
from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))


def setup(client):
    client.add_cog(Setup(client))