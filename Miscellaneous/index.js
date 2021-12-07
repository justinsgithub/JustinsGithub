const pageRequestApi = 'https://aiosoftware.com/api/logs/logrequest'
const logClickApi = 'https://aiosoftware.com/api/logs/logpageclick'

const doc = document.querySelector('html')
const docBody = document.querySelector('body')

var logRequest = () => {
		fetch(pageRequestApi)
		.then(response => response.json())
		.then(data => console.log(data));
}

logRequest()

var logClick = () => {
		fetch(logClickApi)
		.then(response => response.json())
		.then(data => console.log(data));
}
docBody.addEventListener('click', logClick)


console.log('Its working')