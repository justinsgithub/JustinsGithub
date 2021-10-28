import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
fetlife = myclient["fetlife"]
databaseList = myclient.list_database_names()

fetlifeStates = fetlife["states"]


stateList = []

for state in fetlifeStates.find({},{"_id":0, "name":1}):
    stateList.append(state)

for state in stateList:
    print(state["name"])

