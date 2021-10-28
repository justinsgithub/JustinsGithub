import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
fetlife = myclient["fetlife"]
#databaseList = myclient.list_database_names()



#fetlifeStates = fetlife["states"]
#stateList = []
#for state in fetlifeStates.find({},{"_id":0, "name":1}):
#    stateList.append(state)
#for state in stateList:
#    print(state["name"])


seattleUsers = fetlife["seattleUsers"]

userList = []

#for user in seattleUsers.find():
#   userList.append(user)

with open('./followedusers') as file:
    for followeduser in file:
        followeduser = followeduser.strip() #preprocess line
        userQuery = {"userName": followeduser}
        newValue = { "$set": { "followedByLemon": True } }
        seattleUsers.update_one(userQuery, newValue)


#for user in userList:
#    userQuery = {"userName": user["userName"]}
    #newValue = { "$set": { "lovedPictures": False } }
#    newValue = { "$set": { "followedByLemon": False } }
#    seattleUsers.update_one(userQuery, newValue)
