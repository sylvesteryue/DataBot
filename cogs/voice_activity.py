import discord
from discord.ext import commands
from discord.ext import tasks
import datetime
import utils.db

class VoiceActivity(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.update_voice_activity.start()


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #keep track of voice channel activity here
        if before.channel is None and after.channel is not None:
            print(str(member) + " in " + member.guild.name + " joined " + str(after.channel) + " " + str(datetime.datetime.utcnow()))
            # utils.db.member_voice_activity(datetime.datetime.utcnow(), member.guild.id, member.id, "join")

        if before.channel is not None and after.channel is None:
            print(str(member) + " in " + member.guild.name + " left " + str(after.channel) + " " + str(datetime.datetime.utcnow()))
            # utils.db.member_voice_activity(datetime.datetime.utcnow(), member.guild.id, member.id, "leave")


    def cog_unload(self):
        self.update_voice_activity.cancel()


    @tasks.loop(seconds=30.0)
    async def update_voice_activity(self):
        print("hi")
        for guild in self.client.guilds:
            channels = [channel for channel in guild.channels if channel.type == discord.ChannelType.voice]
            members = [member for channel in channels for member in channel.voice_states.keys()]
            #members = [guild.get_member(member) for channel in channels for member in channel.voice_states.keys()]
            # utils.db.add_guild_voice_activity(datetime.datetime.utcnow(), guild.id, members)
            entry = {"timestamp" : datetime.datetime.utcnow(), "guild_id" : guild.id, "members_id" : members}
            print(entry)

    @commands.command()
    async def check_numbers(self, ctx):
        for guild in self.client.guilds:
            channels = [channel for channel in guild.channels if channel.type == discord.ChannelType.voice]
            members = [member for channel in channels for member in channel.members]
            await ctx.send(len(members))
            



def setup(client):
    client.add_cog(VoiceActivity(client))