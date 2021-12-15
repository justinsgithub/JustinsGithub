#!/bin/python3


def update_data(collection, thiskey, thisvalue, newkey, newvalue, isMany: bool):
    if isMany:
        collection.update_many({thiskey: thisvalue}, {"$set": {newkey: newvalue}})
        print("data updated")

    if not isMany:
        collection.update_one({thiskey: thisvalue}, {"$set": {newkey: newvalue}})
        print("data updated")


def count_data(collection):
    data_count = collection.count_documents({})
    print(data_count)
    return data_count


def increment_data(
    collection, querykey, queryvalue, incrementkey, incrementvalue: int, isMany: bool
):
    if isMany:
        print("incrementing data in query")
        collection.update_many(
            {querykey: queryvalue}, {"$inc": {incrementkey: incrementvalue}}
        )
        print("data updated")

    if not isMany:
        print("incrementing data in query")
        collection.update_one(
            {querykey: queryvalue}, {"$inc": {incrementkey: incrementvalue}}
        )
        print("data updated")
