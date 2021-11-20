const { MongoClient } = require("mongodb");
const uri = "mongodb+srv://justinaawd:GWPmXl8uegAvveBa@online-presence-cluster.rdnj4.mongodb.net/sitedb?retryWrites=true&w=majority";
const client = new MongoClient(uri);
const doc = { name: "Neapolitan pizza", shape: "round" };

async function run() {
  try {
    // Connect the client to the server
    await client.connect();
    const result = await client.db("test").collection('test').insertOne(doc);
    console.log("Connected successfully to server");
    console.log(
   `A document was inserted with the _id: ${result.insertedId}`,
);
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

export run;
