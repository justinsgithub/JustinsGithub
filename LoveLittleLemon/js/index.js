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

let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}

function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = 'css/index.css'
	}

	if(mode == 'pink'){
		document.getElementById('theme-style').href = 'css/pink.css'
	}

	if(mode == 'lightgreen'){
		document.getElementById('theme-style').href = 'css/lightgreen.css'
	}

	if(mode == 'orange'){
		document.getElementById('theme-style').href = 'css/orange.css'
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = 'css/purple.css'
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href = 'css/green.css'
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href = 'css/blue.css'
	}

	if(mode == 'dlight'){
		document.getElementById('theme-style').href = 'css/default.css'
	}


	localStorage.setItem('theme', mode)
}
