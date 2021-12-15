// Foursquare API Info
const clientId = 'T4EXA5ZFOD3UYOQH1WDCEMGOXNO2GCGC35GLCHPT2D3RAJCW';
const clientSecret = 'OJOFY24RK4VDXVHYBYVYSOIMCFHU0XQVT245ZIDUDVPR5B5O';
const url = 'https://api.foursquare.com/v2/venues/explore?near=';

// OpenWeather Info
const openWeatherKey = 'e935d0084d9e18f78a478f2d2b04d584';
const weatherUrl = 'https://api.openweathermap.org/data/2.5/weather';

// Page Elements
const $input = $('#city');
const $submit = $('#button');
const $destination = $('#destination');
const $container = $('.container');
const $venueDivs = [$("#venue1"), $("#venue2"), $("#venue3"), $("#venue4")];
const $weatherDiv = $("#weather1");
const weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

const getVenues = async () => {
    const city = $input.val();
    const urlToFetch = `${url}${city}&limit=10&client_id=${clientId}&client_secret=${clientSecret}&v=20211212`;
    try {
        const response = await fetch(urlToFetch);
        const jsonResponse = await response.json();
        if (response.ok) {console.log(response)}
        console.log(jsonResponse);

        const venues = jsonResponse.response.groups[0].items.map(item => item.venue);
        console.log(venues);
        return venues;
  } catch (err) {
    console.log(err);
  }

}

const getForecast = async () => {
    const urlToFetch = `${weatherUrl}?&q=${$input.val()}&APPID=${openWeatherKey}`; 
    console.log(urlToFetch)
    const response = await fetch(urlToFetch);
    if (response.ok){
        const jsonResponse = await response.json()
        console.log(jsonResponse)
        return jsonResponse
    }

    try {
         
    } catch (err){
        console.log(err)
    }

}


const renderVenues = (venues) => {
  $venueDivs.forEach(($venue, index) => {
    const venue = venues[index];
    const venueIcon = venue.categories[0].icon;
    const venueImgSrc = `${venueIcon.prefix}bg_64${venueIcon.suffix}`;
    let venueContent = createVenueHTML(venue.name, venue.location, venueImgSrc);
    $venue.append(venueContent);
  });
  $destination.append(`<h2>${venues[0].location.city}</h2>`);
}

const renderForecast = (day) => {
    const weatherContent = createWeatherHTML(day);
    $weatherDiv.append(weatherContent);
  };

const executeSearch = () => {
    $venueDivs.forEach(venue => venue.empty());
    $weatherDiv.empty();
    $destination.empty();
    $container.css("visibility", "visible");
    getVenues().then(venues => renderVenues(venues));
    getForecast().then(forecast => renderForecast(forecast));
    return false;
}

$submit.click(executeSearch)
