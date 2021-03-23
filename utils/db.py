from pymongo import MongoClient
import config
import datetime

cluster  = MongoClient(config.MONGO_URL)
db = cluster["hackbot_analytics"]



def add_guild_voice_activity(time, guild_id, members_id):
    col = db["guild_voice_activity"]
    entry = {"timestamp" : datetime.datetime.utcnow(), "guild_id" : guild_id, "members_id" : members_id}
    x = col.insert_one(entry)
    print(x)



def add_channel_voice_activity(time, guild_id, channel_id, members_id):
    col = db["channel_voice_activity"]

def add_text_activity(time, guild_id, author_id, channel_id):
    col = db["text_voice_activity"]