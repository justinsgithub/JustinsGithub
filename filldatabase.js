const fs = require('fs')

for (let i = 0; i < 2988; i++){
	fs.appendFileSync('database/fetlife/followers/' + i.toString(), i.toString())
}
