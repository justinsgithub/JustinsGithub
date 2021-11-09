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

    const page = await browser.newPage();
    await page.goto('https://fetlife.com/users/sign_in');
    await page.screenshot({ path: 'example.png' });
    await page.type('#user_login', input.username);
    await page.type('#user_password', input.password);
    await page.click('button[name="button"]');
    await page.waitForNavigation();
      
        for (let i = 0; i < new_list.length; i++) {
        
            let location_selector = `a[href$="/${new_list[1]}"]`

            let area_selector = `a[href$="/${new_list[1]}/related"]`
        
            let kinkter_selector = `a[aria-controls="Kinksters"]`
        
            let username_selector = `a[href^="/users/"][class="link f5 fw7 secondary mr1"]`
            
            let nextselector = 'a[class="next_page"]'
            
            await page.click('a[title="Places"]');
              
            await page.waitForNavigation();
              
            await page.click(location_selector);
          
            await page.waitForNavigation();
              
            await page.click(area_selector);

            await page.waitForNavigation();

            await page.click(kinkster_selector);
         
            await page.waitForNavigation();
            let count = 3 
            for (let i = 0; i < count; i++) {
                let links = await page.$$eval(username_selector, nodes => nodes.map(node => node.innerText.trim()));
                for (let i = 0; i < links.length; i++) {
                    if(links[i] != ''){
                        console.log(links[i])
                    }
                }
                await page.click(nextselector);
                await page.waitForNavigation();
            }
        }
      //const results = await page.$$eval('main > div > div', nodes => nodes.map(node => node.innerText.trim()));
      //const locationNames = await page.$$eval('a[href^="/p/"]', nodes => nodes.map(node => node.innerText.trim()));
    }

    finally {
        await browser.close();
        await client.close();
    }   
}
run().catch(console.dir);
