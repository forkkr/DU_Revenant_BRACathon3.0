from pymongo import MongoClient
from threading import Lock


# Singleton Class
class Database:
    db = None
    instance = None
    lock = Lock()

    def __init__(self, online):
        if online:
            MONGODB_URI = "mongodb://csclassroomfeed:mlab123@ds231643.mlab.com:31643/upgbrac"

            client = MongoClient(MONGODB_URI, connectTimeoutMS=30000, retryWrites=False)
            self.db = client.get_database("upgbrac")
        else:
            client = MongoClient('localhost', 27017)
            self.db = client.upgbrac

    @staticmethod
    def get_instance(online):
        Database.lock.acquire()
        if Database.instance is None:
            Database.instance = Database(online)
        Database.lock.release()
        return Database.instance


# Database Connection Online
db = Database.get_instance(online=True).db


# Database Connection Offline
'''
db = Database.get_instance(online=False).db
'''