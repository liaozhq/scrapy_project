import pymongo

class XiciMongoClient:
        def __init__(self):
                self.client = pymongo.MongoClient(host='192.168.1.160', port=27017)

        def insertXici(self, obj):
                db = self.client.test
                collection = db.xici
                collection.insert(obj)
               

