
/*
function createSquares(){
button = document.createElement("button")
button.classList.add("square")
root.appendChild(button)
}
*/

function createElement(elementName, tag, cssClass, parentElement,pe2){
	parentElement = document.getElementById(parentElement)
	elementName = document.createElement(tag)
	elementName.classList.add(cssClass)
	parentElement.appendChild(elementName)
}

function 

function startGame(gameComponents, param1, param2, param3, param4){
	gameComponents(param1, param2, param3, param4)
}

startGame(createElement,'game','div','game','root')
startGame(createElement,'gameBoard','div','game-board','root')
startGame(createElement,'button','button','square','root')
startGame(createElement,'button','button','square','root')

startGame(createElement,'button','button','square','root')
startGame(createElement,'button','button','square','root')
startGame(createElement,'button','button','square','root')

