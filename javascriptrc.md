# JavaScriptRC 

"use strict";

## Global Variables
var 

### storage

- var session = sessionStorage


### dom 

- doc = document,
- body = doc.body,
- anchors = doc.anchors,
- cookie = doc.cookie,
- lastEdit = doc.lastModified,
- links = doc.links,
- title = doc.title,
- URL = doc.URL

#### selecting dom elements
- getId = doc.getElementById,
- getTag = doc.getElementByTagName,
- query = doc.querySelector,
- queryAll = doc.querySelectorAll,

- getClassList = doc.getElementsByClassName,

#### manipulating dom elements
- createElement = doc.createElement, 
-  newText = doc.createTextNode,
- newEvent = doc.createEvent,
- newAttribute = doc.createAttribute,
- newFrag = doc.createDocumentFragment,



## Global functions

- function sessionSet(newkey, newvalue){
	session.setItem(newkey, newvalue);
}

- function sessionGet(newkey){
	session.getItem(mykey);
}

- function sessionCounter(displayelement) {
	if(typeof(Storage) !== "undefined") {
    		if (sessionGet(clickcount) {
      			sessionSet(clickcount) = Number(sessionGet(clickcount))+1;
    		} else {
      			sessionSet(clickcount) = 1;
    		}
    		displayelement.innerHTML = "You have clicked the button " + sessionGet(clickcount) + " time(s) in this session.";
  		} else {
    		displayelement.innerHTML = "Sorry, your browser does not support web storage...";
  	}
}

- function listen(element, newevent, listenfunction){
	element.addEventListener(newevent, listenfunction)	
}

- function addClick(element, clickfunction){
	listen(element, 'click', clickfunction)
}


function newShortcut(element, shortcutKey){
// IE, Chrome, Safari, Opera 15+: [ALT] + accesskey
//Opera prior version 15: [SHIFT] [ESC] + accesskey
//Firefox: [ALT] [SHIFT] + accesskey
    element.accessKey = shortcutKey;
}

- function addText(element, text){
    element.textContent = text
}
   


f addChild( parentElement, element ){
    parentElement.appendChild(element)
}

