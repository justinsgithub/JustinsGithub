const fs = require('fs')
const readFileSync = fs.readFileSync
const path = require('path')
const process = require('process')
const rootDir = process.cwd()

const database = path.join(rootDir, 'Database')
const databaseList = fs.readdirSync(database)

const fetDatabase = database + "/Fetlife"
const fetList = fs.readdirSync(fetDatabase)

const fetAudience = fetDatabase + "/Audience"

const fetFollowers = fetAudience + "/followers"
const fetFriends = fetAudience + "/friends"
const fetFollowing = fetAudience + "/following"

exports.numberOfFollowers = readFileSync(fetFollowers, 'utf8');
exports.numberOfFriends = readFileSync(fetFriends, 'utf8');
exports.numberOfFollowing = readFileSync(fetFollowing, 'utf8');
