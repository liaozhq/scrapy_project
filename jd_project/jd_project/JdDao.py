import pymongo

class JdMongoClient:
        
        def __init__(self):
                self.client = pymongo.MongoClient(host='192.168.0.160', port=27017)

        def insertJD(self, obj):
                db = self.client.test
                collection = db.jd
                collection.insert(obj)