var express = require('express');
var router = express.Router();
const util = require('util');
const execFile = util.promisify(require('child_process').execFile);


async function fetprintprofile(res) {
  const { stdout } = await execFile('fetprintprofile.sh');
  res.send({message: stdout});
}

async function testing(res) {
  const { stdout } = await execFile('NEWTEST.sh');
  res.send({message: stdout});
}

async function lovestatuses(res) {
  const { stdout } = await execFile('fetlovepicturefeed.sh');
  res.send({message: stdout});
}

async function lovepics(res) {
  const { stdout } = await execFile('fetlovestatusfeed.sh');
  res.send({message: stdout});
}


router.get('/fetprintprofile', function(req, res, next) {
	fetprintprofile(res)
});

router.get('/lovestatuses', function(req, res, next) {
	lovestatuses(res)
});

router.get('/lovepics', function(req, res, next) {
	lovepics(res)
});

router.get('/test', function(req, res, next) {
	testing(res)
});

module.exports = router;
