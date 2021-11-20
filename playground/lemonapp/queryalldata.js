const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://justinaawd:GWPmXl8uegAvveBa@online-presence-cluster.rdnj4.mongodb.net/sitedb?retryWrites=true&w=majority";
const client = new MongoClient(uri);



async function querydata() {
    try {
        await client.connect();
        await console.log('connecting to db...');
        const cursor = await client.db("sitedb").collection('locations').find({})
        if ((await cursor.count()) === 0) {
              console.log("No documents found!");
        }
        await cursor.forEach(console.dir);
    }
    finally {
        // Ensures that the client will close when you finish/error
        await console.log('finishing up');
        await client.close();
    }
}
//module.exports.querydata = querydata
querydata().catch(console.dir);
