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
        await client.connect(); 
        const cursor = await client.db("sitedb")
            .collection('locations')
            .find({}, { projection: { _id: 0, name: 1 }})
        if ((await cursor.count()) === 0) {
              console.log("No documents found!");
        }
        let new_list = []
        let old_list = []
        function filter_data(newlist, data){
            let name = data.name
            old_list.push(name)
            name = name.trim()
            name = name.toLowerCase()
            name = name.replace(/\s/g, "-")
            newlist.push(name) 
        }
        await cursor.forEach(doc => filter_data(new_list, doc));
        await console.log(new_list)
        const page = await browser.newPage();
        await page.goto(
            'https://fetlife.com/users/sign_in'
            , { timeout:0 });
        await page.type('#user_login', input.username);
        await page.type('#user_password', input.password);
        await page.click('button[name="button"]');
        await page.waitForNavigation();
        //   for (let i = 0; i < new_list.length; i++) {
        //let location_selector = `a[href$="/${new_list[i]}"]`
        let location_selector = `a[href$="/${new_list[0]}"]`

        let related_selector = `a[href$="/related"]`

        let area_selector = `a[href^="/p/${new_list[0]}"]`
        
            let kinkter_selector = `a[aria-controls="Kinksters"]`
        
            let username_selector = `a[href^="/users/"][class="link f5 fw7 secondary mr1"]`
            let user_selector = `a[href^="/users/"][class="link f5 fw7 secondary mr1"]`
            
            let nextselector = 'a[class="next_page"]'
            
            await page.click('a[title="Places"]');
              
            await page.waitForNavigation();
              
            await page.click(location_selector);
          
            await page.waitForNavigation();
              
            await page.click(related_selector);

            await page.waitForNavigation();

            const areaNames = await page.$$eval(area_selector, nodes => nodes.map(node => node.innerText.trim()));

            for (let j = 0; j < areaNames.length; j++) {
                const areaName = areaNames[j] 
                await console.log(areaName);
            }

            await page.click(kinkter_selector);
            await page.waitForNavigation();
            const userNames = await page.$$eval(username_selector, nodes => nodes.map(node => node.innerText.trim()));
            for (let j = 0; j < userNames.length; j++) {
                const userName = userNames[j] 
                await console.log(userName);
            }
            await page.click(user_selector);


            await page.waitForNavigation();
            await page.click('#user_pictures_link')
            await page.waitForNavigation();
            await console.log('DONE')

        //}
    }
    finally {
        await client.close();
        await browser.close();
    }
}

run().catch(console.dir);
