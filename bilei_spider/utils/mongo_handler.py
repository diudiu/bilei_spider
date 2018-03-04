from pymongo import MongoClient
from datetime import datetime
from scrapy.conf import settings


def singleton(cls):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


class MongoBase(object):
    def __init__(self, collection):
        self.collection_name = collection
        host = settings["MONGO_HOST"]
        port = int(settings["MONGO_PORT"])
        db = settings["MONGO_DB"]
        username = settings["MONGO_USER"]
        password = settings["MONGO_PSW"]
        self.connection = MongoClient(host=host, port=port)
        self.db = self.connection[db]
        if username and password:
            self.db.authenticate(username, password)
        self.collection = self.db[self.collection_name]

    def __del__(self):
        self.connection.close()

    def insert(self, data):
        data.update({
            'create_time': datetime.now(),
            'update_time': datetime.now(),
        })
        return self.collection.insert_one(data)

