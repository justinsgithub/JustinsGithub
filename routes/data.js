const util = require('util');
const path = require('path');
const fs = require('fs')
const process = require('process')
var express = require('express');
var router = express.Router();

const readFileSync = fs.readFileSync

const rootDir = process.cwd()
const database = path.join(rootDir, 'Database')
const databaseList = fs.readdirSync(database)
const fetDatabase = database + "/Fetlife"
const fetList = fs.readdirSync(fetDatabase)
const fetAudience = fetDatabase + "/Audience"
const fetFollowers = fetAudience + "/followers"
const fetFriends = fetAudience + "/friends"
const fetFollowing = fetAudience + "/following"



const execFile = util.promisify(require('child_process').execFile);
const { exec } = require('child_process');

const db = require('../bin/database')

async function lovestatuses(res) {
  const { stdout } = await execFile('fetlovepicturefeed.sh');
  res.send({message: stdout});
}

async function lovepics(res) {
  const { stdout } = await execFile('fetlovestatusfeed.sh');
  res.send({message: stdout});
}


router.get('/lovestatuses', function(req, res, next) {
	lovestatuses(res)
});

router.get('/lovepics', function(req, res, next) {
	lovepics(res)
});


const following = (res) => {
	let numberOfFollowing = readFileSync(fetFollowing, 'utf8');
	res.send({message: numberOfFollowing});
}

const followers = (res) => {
	let numberOfFollowers = readFileSync(fetFollowers, 'utf8');
	res.send({message: numberOfFollowers});
}

const friends = (res) => {
	let numberOfFriends = readFileSync(fetFriends, 'utf8');
	res.send({message: numberOfFriends});
}

router.get('/updatestats', function(req, res, next) {
	exec('python3 bin/py/fetprintaudience.py',
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
			res.send({message: stdout});
        });
});



router.get('/following', function(req, res, next) {
	following(res)
});

router.get('/followers', function(req, res, next) {
	followers(res)
});

router.get('/friends', function(req, res, next) {
	friends(res)
});

module.exports = router;
