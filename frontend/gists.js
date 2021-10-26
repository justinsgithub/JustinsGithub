<h2>JavaScript Array.forEach()</h2>
<p>Calls a function once for each array element.</p>

<p id="demo"></p>

<script>
const numbers = [45, 4, 9, 16, 25];

let txt = "";

numbers.forEach(myFunction);

document.getElementById("demo").innerHTML = txt;

function myFunction(value, index, array) {
	txt += value +  " is the value at index " + index + " ( which is the first item of the array )" + "<br> "; 
}
</script>


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

