const Apify = require('apify');
const { log } = Apify.utils;

const loggedCheck = async (page) => {
    try {
        await page.waitForSelector('#bluebarRoot', { timeout: 10000 });
        return true;
    } catch(err) {
        return false;
    }
};

Apify.main(async () => {
    // Get the username and password inputs
    const input = await Apify.getValue('INPUT');

    const fcbCacheStore = await Apify.openKeyValueStore('fcb-cache');
    const cookiesStoreKey = input.username.replace('@', '(at)');

    const browser = await Apify.launchPuppeteer();
    const page = await browser.newPage();

    let isLogged = false;
    let userCookies = await fcbCacheStore.getValue(cookiesStoreKey);
    if (userCookies) {
        log.info('Trying to use cached cookies...')
        await page.setCookie(...userCookies);
        await page.goto('https://facebook.com');
        isLogged = await loggedCheck(page);
    }

    if (!isLogged) {
        log.info(`Cookies from the cache didn't work. Try to log in.`);
        await page.goto('https://fetlife.com/users/sign_in');
        await page.type('#email', input.username);
        await page.type('#pass', input.password);
        await page.click('button');
        await page.waitForNavigation();
        isLogged = await loggedCheck(page);
    }

    if (!isLogged) {
        throw new Error('Incorrect username or password.')
    }

    // Get cookies and refresh them in store cache
    log.info(`Saving new cookies to cache...`);
    const cookies = await page.cookies();
    await fcbCacheStore.setValue(cookiesStoreKey, cookies);

    // Use cookies in another tab or browser
    const page2 = await browser.newPage();
    await page2.setCookie(...cookies);
    // Opens thepage as a logged-in user
    await page2.goto('https://facebook.com');

    await browser.close();

    log.info('Done.');
});
