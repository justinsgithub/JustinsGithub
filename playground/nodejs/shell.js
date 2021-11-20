const readline = require('readline');
const { stdin: input, stdout: output } = require('process');
const rl = readline.createInterface({ input, output });
const fs = require('fs');
const ls = fs.readdirSync('.')


//rl.question('What do you think of Node.js? ', (answer) => {
  // TODO: Log the answer in a database
//  console.log(`Thank you for your valuable feedback: ${answer}`);

//  rl.close();
//});