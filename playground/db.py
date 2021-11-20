from mongita import MongitaClientDisk
import re
import os
client = MongitaClientDisk()



def use_db(name):
    name = client.name
    return(name)

def use_collection(db, collection_name):
    collection_name = db.collection_name
    return collection_name

def add_data(collection, data):
    collection.insert_one(data)

def count_data(data):
    return data.count_documents({})
    


test_db = use_db("test_db")
test_collection = use_collection(test_db, "test collection")

test_data = {
        "test_string2": "my new data 2"
        }
add_data(test_collection, test_data)

data_count = count_data(test_collection)

print(data_count)


