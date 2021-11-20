const { MongoClient } = require("mongodb");
const uri = "mongodb+srv://justinaawd:GWPmXl8uegAvveBa@online-presence-cluster.rdnj4.mongodb.net/sitedb?retryWrites=true&w=majority";
const client = new MongoClient(uri);
const Apify = require('apify');

const doc = { name: "Neapolitan pizza", shape: "round" };


Apify.main(async () => {
    const input = await Apify.getValue('INPUT');
    console.log('Opening web page...');
    const browser = await Apify.launchPuppeteer();
    const page = await browser.newPage();
    await page.goto('https://fetlife.com/users/sign_in');
    await page.type('#user_login', input.username);
    await page.type('#user_password', input.password);
    await page.click('#remember_me');
    await page.click('button[name="button"]');
    await page.waitForNavigation();
    await page.click('a[title="Places"]');
    console.log('Getting "place" items from the page.');
    const results = await page.$$eval('main > div > div', nodes => nodes.map(node => node.innerText.replace('...', 'Did you know')));
    console.log(results);
    console.log('Actor finished.');
    await browser.close();
});
