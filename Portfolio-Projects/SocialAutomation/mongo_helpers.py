#!/bin/python3

def delete_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("deleting all data")
        collection.delete_many({thiskey: thisvalue})
        print("succesfully deleted")

    if not isMany:
        print("deleting single data")
        collection.delete_one({thiskey: thisvalue})
        print("succesfully deleted")


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
    print("getting all data in collection")
    search = collection.find({})

    return search


def query_data(collection, thiskey, thisvalue, isMany: bool):
    if isMany:
        print("getting all data in search")
        search = collection.find({thiskey: thisvalue})

        return search

    if not isMany:
        print("getting first data matching query")
        search = collection.find_one({thiskey: thisvalue})
        print(search["_id"])

        return search


def update_data(collection, thiskey, thisvalue, newkey, newvalue,
                isMany: bool):
    if isMany:
        collection.update_many({thiskey: thisvalue},
                               {"$set": {
                                   newkey: newvalue
                               }})
        print("data updated")

    if not isMany:
        collection.update_one({thiskey: thisvalue},
                              {"$set": {
                                  newkey: newvalue
                              }})
        print("data updated")


def count_data(collection):
    data_count = collection.count_documents({})
    print(data_count)
    return data_count


def increment_data(collection, querykey, queryvalue, incrementkey,
                   incrementvalue: int, isMany: bool):
    if isMany:
        print("incrementing data in query")
        collection.update_many({querykey: queryvalue},
                               {"$inc": {
                                   incrementkey: incrementvalue
                               }})
        print("data updated")

    if not isMany:
        print("incrementing data in query")
        collection.update_one({querykey: queryvalue},
                              {"$inc": {
                                  incrementkey: incrementvalue
                              }})
        print("data updated")
