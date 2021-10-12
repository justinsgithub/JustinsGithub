const fs = require("fs"), readFile = fs.readFileSync, readDir = fs.readdirSync, 
	appendFile = fs.appendFileSync,
	http = require("http"), 
	os = require("os"), 
	path = require("path"), join = path.join,
	events = require("events"), 
	child_process = require("child_process"), 
	crypto = require("crypto"),
	net = require("net"),
	url = require("url"),
	stream = require("stream")


const database = join(process.cwd(), 'database'),
	pageRequestsDir = `${database}/logs/pagerequests`


let jsonResponse = (responseObject, serverResponse) => {
	responseObject.status(200).json({serverResponse})
}

let okayResponse = (responseObject) => {
	responseObject.status(200).json({message: "ok"})
}


export default function handler(request, response) {
	let totalPageRequests = readDir(pageRequestsDir).length, 
		newRequest = totalPageRequests + 1,
		logFileName = newRequest.toString(),
		logFile = `${pageRequestsDir}/${logFileName}`,
		logRequest = () => {
			fs.appendFile(logFile, 'newRequest')
			}


	logRequest();

	console.log(totalPageRequests)
	
	okayResponse(response);

}
