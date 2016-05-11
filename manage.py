import pymongo

MONGODB_URI = 'mongodb://ds:ds@ds059694.mongolab.com:59694/datastructure'
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()
# fitters = db['fitter-collection'] <- 본인에 생성한 collection 정보 입력!
# cursor = fitters.find()
# for fitter in cursor:
#     print ('fitter : %s' % (fitter['useremail'])) <- 본인에 생성한 collection의 필드 정보 입력!
# db.drop_collection('fitters');
client.close();
