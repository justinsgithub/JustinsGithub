# JavaScriptRC 

"use strict";

## Global Variables
var 

### dom 

- doc = document,
- body = doc.body,
- anchors = doc.anchors,
- cookie = doc.cookie,
- lastEdit = doc.lastModified,
- links = doc.links,
- title = doc.title,
- URL = doc.URL
- 

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

- function listen(element, newevent, listenfunction){
	element.addEventListener(newevent, listenfunction)	
}

function addClick(element, clickfunction){
	listen(element, 'click', clickfunction)
}

function

f newShortcut(element, shortcutKey){
// IE, Chrome, Safari, Opera 15+: [ALT] + accesskey
//Opera prior version 15: [SHIFT] [ESC] + accesskey
//Firefox: [ALT] [SHIFT] + accesskey
    element.accessKey = shortcutKey;
}

f addText(element, text){
    element.textContent = text
}
   


f addChild( parentElement, element ){
    parentElement.appendChild(element)
}

