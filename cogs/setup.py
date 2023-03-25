import discord
import discord.ext


class Setup(discord.ext.commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.ext.commands.Cog.listener()
    async def on_ready(self):
        for guild in self.client.guilds:
            print(self.client.guilds)
    

    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        print(member)



def setup(client):
    client.add_cog(Setup(client))