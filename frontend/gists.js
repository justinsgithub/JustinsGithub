function createElements(){
root = document.getElementById("root")
button = document.createElement("button")
button.classList.add("square")
root.appendChild(button)
}

function gameComponents(staticElements, dynamicElements){
	
}

function startGame(gameComponents){
gameComponents()
}
startGame(createElements)
