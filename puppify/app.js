const Apify = require('apify');

Apify.main(async () => {
    const requestQueue = await Apify.openRequestQueue();
    await requestQueue.addRequest({ url: 'https://apify.com' });

    const handlePageFunction = async ({ request, $ }) => {
        const title = $('title').text();

        console.log(`The title of "${request.url}" is: ${title}.`);
    };

    // Set up the crawler, passing a single options object as an argument.
    const crawler = new Apify.CheerioCrawler({
        requestQueue,
        handlePageFunction,
    });

    await crawler.run();
});
