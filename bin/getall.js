const fs = require("fs"), readFile = fs.readFileSync, writeFile = fs.appendFileSync,
	http = require("http"), 
	os = require("os"), 
	path = require("path"), join = path.join
	events = require("events"), 
	child_process = require("child_process"), 
	crypto = require("crypto"),
	net = require("net"),
	url = require("url"),
	stream = require("stream")


const database = join(process.cwd(), 'database'),
	todosDir = `${database}/project/todos`

export default function handler(req, res) {
res.status(200).json({ name: "John Doe" })
}
