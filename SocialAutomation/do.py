#!/bin/python3

import typer

import pymongo

from secrets import my_vars

from getpass import getuser

from bson.objectid import ObjectId

uri = my_vars["uri"]

client = pymongo.MongoClient(uri)

username = getuser()

app = typer.Typer()

begin = """

"""
end = """

"""


@app.command()
def countCityData():

    db = client["CitiesData"]

    collection_names = db.list_collection_names()

    data_count = 0

    number_of_states = len(collection_names)

    for collection_name in collection_names:

        collection = db[collection_name]

        data_count += collection.count_documents({})

    average_cities_per_state = int(data_count / number_of_states)

    output1 = f"          we have data for {data_count} cities and {len(collection_names)} states for an "

    output2 = f"average {average_cities_per_state} cities per state"

    output = begin + output1 + output2 + end

    typer.secho(output, fg="green")


@app.command()
def delete(db_name, collection_name, this_key, this_value):

    db = client[db_name]

    collection = db[collection_name]

    result = collection.delete_one({this_key: this_value})

    typer.secho(f"deleted first document matching result", fg="green")

    typer.secho(result, fg="red")


@app.command()
def find(db_name, collection_name, this_key, this_value):

    db = client[db_name]

    collection = db[collection_name]

    result = collection.find_one({this_key: this_value})

    typer.secho(f"found first document matching result", fg="green")

    typer.secho(result, fg="red")


@app.command()
def update(db_name, collection_name, query_key, query_value, new_key, new_value):

    db = client[db_name]

    collection = db[collection_name]

    result = collection.update_one(
        {query_key: query_value}, {"$set": {new_key: new_value}}
    )

    typer.secho(f"inserted new data, result object = {result}", fg="green")


@app.command()
def insert(db_name, collection_name, this_key, this_value):

    db = client[db_name]

    collection = db[collection_name]

    result = collection.insert_one({this_key: this_value})

    typer.secho(f"inserted new data, result object = {result}", fg="green")


@app.command()
def databases(col: bool = False):

    database_list = client.list_database_names()

    count = len(database_list)

    greet = f"Hello {username} here are your {count} databases"

    if col:

        typer.secho(greet, fg="green")

        for database in database_list:

            typer.secho(database, fg="green")

        return

    typer.secho(greet, fg="blue")

    typer.secho(database_list, fg="green")


@app.command()
def countdocs(collection_name: str = "", dbname: str = "users", getall: bool = False):
    db = client[dbname]
    count = 0
    if getall:
        collection_names = db.list_collection_names()
        for collection_name in collection_names:

            collection = db[collection_name]

            count += collection.count_documents({})

        message = f"{begin}           {count} total documents in {dbname} database{end}"

        typer.secho(message, fg="green")

        return

    if dbname and getall:
        db = client[dbname]

        collection_names = db.list_collection_names()

        for collection_name in collection_names:

            collection = db[collection_name]

            count += collection.count_documents({})

        message = f"{begin}           {count} total documents in {dbname} database{end}"

        typer.secho(message, fg="green")

        return

    collection_names = db.list_collection_names()
    
    collection = db[collection_names[0]]
      
    count += collection.count_documents({})

    message = f"{begin}           {count} total documents in {collection_names[0]} collection from {dbname} database{end}"

    typer.secho(message, fg="green")

    return


@app.command()
def findstate(
    state_name: str,
    many: bool = False,
    col: bool = False,
    fatalerr: bool = False,
    likedpics: str = "",
    oid: str = "",
):
    db = client["users"]

    if likedpics:
        results = db[state_name].find({"state": state_name, likedpics: True})

    if oid:
        results = db[state_name].find({"state": state_name, "_id": ObjectId(oid)})

    if many:
        results = db[state_name].find({"state": state_name})
        for result in results:
            typer.secho(result, fg="green")
            return

    if fatalerr:
        result = db[state_name].find_one({"state": state_name, "fatalErr": True})
        typer.secho(result, fg="green")
        return

    result = db[state_name].find_one({"state": state_name})
    typer.secho(result, fg="green")


@app.command()
def collections(col: bool = False):

    db_collections = client["users"].list_collection_names()

    count = len(db_collections)

    greet = f"here are your {count} scraped data collections {username}"

    if col:

        typer.secho(greet, fg="blue")

        for collection in db_collections:

            typer.secho(collection, fg="green")

        return

    typer.secho(greet, fg="blue")

    typer.secho(db_collections, fg="green")


if __name__ == "__main__":

    app()
