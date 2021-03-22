from pymongo import MongoClient
import config
import datetime

db  = MongoClient(config.MONGO_URL).test



def add_guild_voice_activity(time, guild_id, members_id):
    col = db["guild_voice_activity"]
    entry = {"timestamp" : datetime.datetime.utcnow(), "guild_id" : guild_id, "members_id" : members_id}
    x = col.insert_one(entry)
    print(x)



def add_channel_voice_activity(time, guild_id, channel_id, members_id):
    pass

def add_text_activity(time, guild_id, author_id, channel_id):
    pass