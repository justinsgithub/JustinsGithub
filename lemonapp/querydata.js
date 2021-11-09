const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://justinaawd:GWPmXl8uegAvveBa@online-presence-cluster.rdnj4.mongodb.net/sitedb?retryWrites=true&w=majority";
const client = new MongoClient(uri);




async function querydata() {
    try {
        await client.connect(); 
        await console.log('connecting to db...');
        const cursor = await client.db("sitedb").collection('locations').find({}, { projection: { _id: 0, name: 1 }})
        if ((await cursor.count()) === 0) {
              console.log("No documents found!");
        }
        let new_list = []
        function filter_data(newlist, data){
            let name = data.name
            name = name.trim()
            name = name.toLowerCase()
            name = name.replace(/\s/g, "-")
           newlist.push(name) 
        }
        await cursor.forEach(doc => filter_data(new_list, doc));
        await console.log(new_list)


    }
    finally {
        // Ensures that the client will close when you finish/error
        await console.log('finishing up');
        await client.close();
    }
}
//module.exports.querydata = querydata
querydata().catch(console.dir);
