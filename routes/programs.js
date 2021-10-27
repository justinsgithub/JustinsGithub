var express = require('express');
var router = express.Router();
const util = require('util');
const { exec } = require('child_process');



router.get('/lovewritings', function(req, res, next) {
	exec('python3 bin/py/lovewritings.py',
        (error, stdout, stderr) => {
            if (error !== null) {
				res.send({message: error});
            } 
			else if (stderr !== null) { 
				res.send({message: stderr});
				}
			else {
				res.send({message: stdout});
				}
        });
});


router.get('/lovestatuses', function(req, res, next) {
	exec('python3 bin/py/lovestatuses.py',
        (error, stdout, stderr) => {
            if (error !== null) {
				res.send({message: error});
            }
			else if (stderr !== null) { 
				res.send({message: stderr});
				}
			else {
				res.send({message: stdout});
				}
        });
});

router.get('/lovepictures', function(req, res, next) {
	exec('python3 bin/py/lovepictures.py',
        (error, stdout, stderr) => {
            if (error !== null) {
				res.send({message: error});
            } 
			else if (stderr !== null) { 
				res.send({message: stderr});
				}
			else {
				res.send({message: stdout});
				}
        });
});

module.exports = router;
