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



### functions

f = function,


let myHeader = getId('myHeader'),
headerText = 'welcome to my site'

f addText(element, text){
    element.textContent = text
}
   


f addChild( parentElement, element ){
    parentElement.appendChild(element)
}

