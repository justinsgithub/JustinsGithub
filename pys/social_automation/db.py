#!/bin/python3

import pymongo

uri = "mongodb+srv://justinaawd:YhsGDjkfojaq0fC5@online-presence-cluster.rdnj4.mongodb.net/site1?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(uri)

test_db = cluster["test"]
test_collection = test_db["test"]

db = cluster["site1"]
location_collection = db["locations"]
user_collection = db["users"]

tc = test_collection
# post1 = {"name": "eric", "score": 5}
# post2 = {"name": "tyler", "score": 15}
# post3 = {"name": "angeles", "score": 20}


def delete_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("deleting all data")
        deleted = collection.delete_many({thiskey: thisvalue})
        print(deleted)

    if not isMany:
        print("deleting single data")
        deleted = collection.delete_one({thiskey: thisvalue})
        print(deleted)


def insert_data(collection, data, isMany: bool):
    if isMany:
        print("inserting all data")
        collection.insert_many(data)
        print(data)

    if not isMany:
        print("inserting single data")
        collection.insert_one(data)
        print(data)


def all_data(collection):
    print("printing all data in collection")
    search = collection.find({})
    for x in search:
        print(x)


def query_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("printing all data in search")
        search = collection.find({thiskey: thisvalue})
        print(search)
        for x in search:
            print(x)

    if not isMany:
        print("printing first data in search")
        search = collection.find_one({thiskey: thisvalue})
        print(search)


def update_data(collection, thiskey, thisvalue, newkey, newvalue,
                isMany: bool):
    if isMany:
        print("printing all data in search")
        update = collection.update_many({thiskey: thisvalue},
                                        {"$set": {
                                            newkey: newvalue
                                        }})
        print(update)

    if not isMany:
        print("printing first data in search")
        update = collection.update_one({thiskey: thisvalue},
                                       {"$set": {
                                           newkey: newvalue
                                       }})
        print(update)


def count_data(collection):
    data_count = collection.count_documents({})
    print(data_count)
    return data_count

def increment_data(collection, querykey, queryvalue, incrementkey,
                   incrementvalue: int, isMany: bool):
    if isMany:
        print("incrementing data in query")
        update = collection.update_many(
            {querykey: queryvalue}, {"$inc": {
                incrementkey: incrementvalue
            }})
        print(update)

    if not isMany:
        print("incrementing data in query")
        update = collection.update_one(
            {querykey: queryvalue}, {"$inc": {
                incrementkey: incrementvalue
            }})
        print(update)


#print(insert_data(tc, post1, False))
#print_data(tc, "name", "justin", False)
#all_data(tc)
#delete_data(tc, "name", "justin", True)
#update_data(tc, "name", "tyler", "name", "justin-tyler", True)
#update_data(tc, "name", "angeles", "name", "justin tyler angeles", True)
#update_data(tc, "name", "justin tyler angeles", "name", "jewell lemon", False)
#all_data(tc)
#count_data(tc)
#query_data(tc, "name", "justin tyler angeles", False)
#increment_data(tc, "name", "justin tyler angeles", "score", 5, False)
#query_data(tc, "name", "justin tyler angeles", False)
#count_data(tc)
