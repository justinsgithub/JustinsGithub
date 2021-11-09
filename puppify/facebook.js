const Apify = require('apify');

const { log } = Apify.utils;

Apify.main(async () => {
    // Get the username and password inputs
    const input = await Apify.getValue('INPUT');

    const browser = await Apify.launchPuppeteer();
    const page = await browser.newPage();
    await page.goto('https://facebook.com');

    // Login
    await page.type('#email', input.username);
    await page.type('#pass', input.password);
    await page.click('#u_0_b');
    await page.waitForNavigation();

    // Get cookies
    const cookies = await page.cookies();

    // Use cookies in another tab or browser
    const page2 = await browser.newPage();
    await page2.setCookie(...cookies);
    // Open the page as a logged-in user
    await page2.goto('https://facebook.com');

    await browser.close();

    log.info('Done.');
});
