import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

fetlife = myclient["fetlife"]

print(myclient.list_database_names())

databaseList = myclient.list_database_names()

if "fetlife" in databaseList:
  print("The database exists.")
else:
    print('database does not exist yet')


fetLifeStats = fetlife["stats"]

mystats = [
  { "category": "followers", "amount": 341},
  { "category": "friends", "amount": 658},
  { "category": "following", "amount": 3414},
]

#x = fetLifeStats.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

#for stat in fetLifeStats.find():
# print(stat)

for stat  in fetLifeStats.find({},{ "category": 0 }):
    print(stat)
