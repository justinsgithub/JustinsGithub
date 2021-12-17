#!/bin/python3

import typer

import pymongo

from secrets import my_vars

from getpass import getuser

uri = my_vars["uri"]

client = pymongo.MongoClient(uri)

username = getuser()

app = typer.Typer()

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

def collections(database_name, col: bool = False):

    database_list = client.list_database_names()

    db_collections = client[database_name].list_collection_names()

    count = len(db_collections)

    greet = f"here are your {count} {database_name} collections {username}"

    if not database_name in database_list:

        typer.secho("invalid database name, here are your options", fg="red")

        for database in database_list:

            typer.secho(database, fg="green")

        return

    if col:

        typer.secho(greet, fg="blue")

        for collection in db_collections:

            typer.secho(collection, fg="green")

        return

    typer.secho(greet, fg="blue")

    typer.secho(db_collections, fg="green")

if __name__ == "__main__":

    app()

