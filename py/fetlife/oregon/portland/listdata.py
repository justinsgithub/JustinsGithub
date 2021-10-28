import pymongo

database = pymongo.MongoClient("mongodb://localhost:27017/")
databaseList = database.list_database_names()
fetlifeDatabase = database["fetlife"]



portlandUsers= fetlifeDatabase["portlandUsers"]
userList = []

#for user in seattleUsers.find({},{ "_id":0, "userName":1, "lovedPictures":1 }):
for user in portlandUsers.find():
    lovedPictures = user["lovedPictures"]
    followedByLemon = user["followedByLemon"]
    userName = user["userName"]
    #if followedByLemon == True:
    if lovedPictures == True:
    #print(user)
        userList.append(userName)
        print(userName)

#for user in userList:
        #print(user["lovedPictures"])
    #    print(user["userName"])
#        followedByLemon = user["followedByLemon"]
 #       if followedByLemon == True:
  #          print(user)

#for user in seattleUsers.find():
#    print(user)
