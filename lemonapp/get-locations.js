const { MongoClient } = require("mongodb");
const puppeteer = require("puppeteer")

const uri = "mongodb+srv://justinaawd:GWPmXl8uegAvveBa@online-presence-cluster.rdnj4.mongodb.net/sitedb?retryWrites=true&w=majority";
const client = new MongoClient(uri);


const input = {
       username:"lovelittlelemon",
       password:"Ilovelemon93"
}



async function run() {
    const browser = await puppeteer.launch({ headless: false }); // default is true
  try {
    // Connect the client to the server
    await client.connect();
    await console.log('Opening web page...');
    await console.log('connecting to db...');
    const page = await browser.newPage();
    await page.goto('https://fetlife.com/users/sign_in');
    await page.screenshot({ path: 'example.png' });
    await page.type('#user_login', input.username);
    await page.type('#user_password', input.password);
    await page.click('button[name="button"]');
    await page.waitForNavigation();
    await page.click('a[title="Places"]');
    await console.log('Getting "place" items from the page.');
    await page.waitForNavigation();
      //const results = await page.$$eval('main > div > div', nodes => nodes.map(node => node.innerText.trim()));
    const locationNames = await page.$$eval('a[href^="/p/"]', nodes => nodes.map(node => node.innerText.trim()));

    for (let i = 0; i < locationNames.length; i++) {
        locationName = locationNames[i] 
        await console.log(locationNames[i]);
        /*
        const location = { 
            name: locationName, 
            foundRelated: false, 
            numOfCities: 0,
            totalKinksters:0,
            cities: [],
            kinksters:[]
            } 
        await client.db("sitedb").collection('locations').insertOne(location);
        */ 
    };
}   finally {
    // Ensures that the client will close when you finish/error
    await console.log('finishing up');
    await browser.close();
    await client.close();
  }
}
run().catch(console.dir);
