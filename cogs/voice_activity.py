import discord
from discord.ext import commands
import time
import sqlite3


class VoiceActivity(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #keep track of voice channel activity here
        if before.channel is None and after.channel is not None:
            print(str(member) + " joined " + str(after.channel) + " " + str(time.localtime(time.time())))


def setup(client):
    client.add_cog(VoiceActivity(client))