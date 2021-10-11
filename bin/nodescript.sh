#!/bin/bash

echo 'enter new node script name > '

read scriptName

touch /bin/"$scriptName.js"


echo 'const fs = require("fs")' >> /bin/$scriptName.js
echo 'const http = require("http")' >> /bin/$scriptName.js
echo 'const os = require("os")' >> /bin/$scriptName.js
echo 'const path = require("path")' >> /bin/$scriptName.js
echo 'const events = require("events")' >> /bin/$scriptName.js
echo 'const child_process = require("child_process")' >> /bin/$scriptName.js
echo 'const crypto = require("crypto")' >> /bin/$scriptName.js
echo 'const net = require("net")' >> /bin/$scriptName.js
echo 'const url = require("url")' >> /bin/$scriptName.js
echo 'const stream = require("stream")' >> /bin/$scriptName.js
vim /bin/"$scriptName.js"
