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


def member_voice_activity(time, guild_id, member_id, join_type):
    col = db["member_voice_activity"]
    filter = {'guild_id': guild_id, 'member_id': member_id}
    doc = col.find(filter)
    new_value = {"guild_id": guild_id, "member_id": member_id}
    x = col.update(filter, {"$set": new_value, "$push": {"actions" : {"timestamp" : datetime.datetime.utcnow(), "join_type": join_type}}}, upsert=True)
    print(x)


def add_channel_voice_activity(time, guild_id, channel_id, members_id):
    col = db["channel_voice_activity"]


def add_member_text_activity(guild_id, author_id, channel_id):
    col = db["member_text_activity"]

    filter = {'guild_id': guild_id, 'author_id': author_id}
    doc = col.find(filter)
    new_value = {"guild_id": guild_id, "author_id": author_id}
    x = col.update(filter, {"$set": new_value, "$inc": {"num_messages" : 1}}, upsert=True)
    print(x)


def add_channel_text_activity(guild_id, author_id, channel_id):
    col = db["channel_text_activity"]

    filter = {'guild_id': guild_id, 'channel_id': channel_id}
    doc = col.find(filter)
    new_value = {"guild_id": guild_id, "channel_id": channel_id}
    x = col.update(filter, {"$set": new_value, "$inc": {"num_messages" : 1}}, upsert=True)
    print(x)