# JavaScriptRC 

"use strict";

## Global Variables
var 

- doc = document,
- session = sessionStorage,
- local = localStorage,
- body = doc.body,
- anchors = doc.anchors,
- cookie = doc.cookie,
- lastEdit = doc.lastModified,
- links = doc.links,
- title = doc.title,
- URL = doc.URL,
- getId = doc.getElementById,
- getTag = doc.getElementByTagName,
- query = doc.querySelector,
- queryAll = doc.querySelectorAll,
- getClassList = doc.getElementsByClassName,
- createElement = doc.createElement, 
- newText = doc.createTextNode,
- newEvent = doc.createEvent,
- newAttribute = doc.createAttribute,
- newFrag = doc.createDocumentFragment,



## Global functions


getText("fetch_info.txt");

- async function getText(file) {
  let myObject = await fetch(file);
  let myText = await myObject.text();
  document.getElementById("demo").innerHTML = myText;
}
- function wait2Seconds(functiontowait, milliseconds){
	setTimeout(functiontowait, milliseconds)
}

function log(logcontent){
	console.log(logcontent)
}

function log2seconds(){
	wait2seconds(log(2000), 2000)
}

- function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

- function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

- function checkCookie() {
  let user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
     user = prompt("Please enter your name:","");
     if (user != "" && user != null) {
       setCookie("username", user, 30);
     }
  }
}

- function setCookiePath(cname, cvalue, exdays, cookiepath) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  let path = "path=" + cookiepath
  document.cookie = cname + "=" + cvalue + ";" + expires + ";" + path;
}

- function setCookieExpire(cookieName, cookieValue, expireDate, cookiePath){
	doc.cookie = `${cookieName}=${cookieValue}; expires=${expireDate}; path=${cookiePath}`
};


- function sessionSet(newkey, newvalue){
	session.setItem(newkey, newvalue);
}

- function sessionGet(newkey){
	session.getItem(mykey);
}

- function localSet(newkey, newvalue){
	local.setItem(newkey, newvalue);
}

- function localGet(newkey){
	local.getItem(mykey);
}
- function localRemove(keytoremove){
	local.removeItem(keytoremove);
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

