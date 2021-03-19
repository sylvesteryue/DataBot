from pymongo import MongoClient
import config

cluster  = MongoClient(config.MONGO_URL)
mongo = cluster["HackBot"]