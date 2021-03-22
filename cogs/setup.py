import discord
from discord.ext import commands


class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.create_text_channel("annoucements")




def setup(client):
    client.add_cog(Setup(client))