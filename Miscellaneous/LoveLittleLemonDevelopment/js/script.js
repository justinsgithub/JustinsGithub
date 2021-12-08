//console.log('Its working')

requestUrl = "http://localhost:8000/logrequest"

async function makeRequest(url) {
    console.log('making request')
    response = await fetch(url)
    json_response = await response.json()
    console.log(json_response)
    return json_response
}

makeRequest(requestUrl)



