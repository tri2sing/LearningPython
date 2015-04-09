import datetime
import pymongo
import sys

today = datetime.datetime.utcnow()
today = today.replace (hour=0, minute=0, second=0, microsecond=0)

# The MongoDB should not be set to use a usename and password for access
MONGO_URL = 'mongodb://mongodb-us-sw-in.icloud.intel.com'

try:
    conn = pymongo.Connection (MONGO_URL, safe=True)
except pymongo.errors.ConnectionFailure as e:
    print 'Error: check your MongoDB connectivity'
    print 'Error:', e
    sys.exit()

# Set the mongo database to the one for inventory information
db = conn.collectd

# Set the Mongo collection to the one for flavor information
# coll = db.disk
coll = db.cpu

# query = {'timestamp':datetime.datetime (2013, 7, 8)}
query = {'timestamp':today}
selector = {'_id': 0}

try:
#     docs = coll.find ({ "host" : "prd1intfm1occn03.cps.intel.com", 
#                         "time" : { "$gte" : datetime.datetime(2013,11,18), "$lte" : datetime.datetime(2013,11,19) } },
#                       { "values" : 1, "time": 1, "_id" : 0 }).sort("time", pymongo.DESCENDING).limit(5)

    docs = coll.find ({ "host" : "prd1intfm1occn03.cps.intel.com", 
                        "time" : { "$gte" : datetime.datetime(2013,11,18), "$lte" : datetime.datetime(2013,11,19) } },
                      ).sort("time", pymongo.DESCENDING).limit(5)

except pymongo.errors.PyMongoError as e:
    print 'Error: unable to query for instance info'
    print 'Error:', e

for doc in docs:
   # print doc['host']
   # print doc['host'], doc['time']
  # print doc['time'], ', ', doc['host']
    print doc['time'], ',', doc['host'], ',', doc['type'], ',', doc['dsnames'][0], ',', doc['values'][0]
#     print doc['time'], ',', doc['host'], ',', doc['dsnames'][0], ',', doc['values'][0], ',', doc['dsnames'][1], ',', doc['values'][1]






