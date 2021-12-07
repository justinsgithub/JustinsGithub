# using mongodb with python

## connection uri

- uniform resource locator
- uri is used to connect for the pymongo driver to connect to mongo db
- starts with 
> mongodb+srv://
- continues with username and password
- mongodb+srv://<username>:<password>
- then the host name for the srv record and cluster name for the database to connect to 
- mongodb+srv://<username>:<password>@<host>/<database>
- srv stands for service record
- we can add additional options at the end of the uri after a ?
- mongodb+srv://<username>:<password>@<host>/<database>?otherOption=true


## MongoClient 
- comes with the official pymongo driver
- accepts optional keyword arguments to fine-tune connection 
- after instantiating / initializing connection 


## read operations

### collection.find_one() and collection.find() 
- used to query documents in a collection 
- allow a query predicate to target specific documents
- allow field projection to specify which fields we want returned
- find() returns a cursor object while find_one() does not 


## code examples 

> using mflix database from mongodb university

```python

from pymongo import MongoClient

uri = "mongodb+srv://my-username:my-password@my-cluster.my-host.mongodb.net/mflix"
better_uri = uri +  "?retryWrites=true&w=majority"


client = MongoClient(uri)
print(client.stats)


# similiar effect to the better_uri above
better_client = MongoClient(uri, connectTimeoutMS=200, retryWrites=True)
print(better_client.stats)

client = better_client

mflix = client.mflix

# same thing as above
mflix = client["mflix"]

movies = mflix["movies"]

# displays information about connection, automatically has an ssl connection and authenticates against the admin database information

print(client.list_database_names())

print(mflix.list_collection_names())


# counts all movie documents
print(movies.count_documents({}))


# returns first movie in collection 
print(movies.find_one())

#returns first movie with salma in the cast 
print(movies.find_one( {"cast": "Salma Hayek"} ))

#returns a cursor object with all documents containing salma in the cast
print(movies.find( {"cast": "Salma Hayek"} ))

#returns a count of all the documents found
print(movies.find( {"cast": "Salma Hayek"} ).count())


#assign cursor object to a variable
salma_cursor = movies.find( {"cast": "Salma Hayek"} )

# easier to read with limited data returned
title_only = movies.find( {"cast": "Salma Hayek"}, {"title": 1} )

# id must explicitely be set to 0 if we do not want it returned 
no_id = movies.find( {"cast": "Salma Hayek"}, {"title": 1, "_id": 0} )

# print cursor data
from bson.json_util import dumps
cursor = movies.find( {"cast": "Salma Hayek"} )
print(dumps(cursor, indent=2))
```

