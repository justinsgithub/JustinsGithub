const mongoose = require('mongoose')



const reqNum = {
  type: Number,
  required: true,
}

const formattedString = (newString) => {
    let cleanString = newString.trim()
    let cleanestString = cleanerString.toLowerCase()
    let niceString = cleanestString.replaceAll(/\s/g, '-')
    return niceString
} 

const reqString = {
  type: String,
  required: true,
}

const userSchema = mongoose.Schema(
  {
    userId: Number,
    userName: reqString,
    numOfPics: Number,
    gender: String,
  },
  {
    timestamps: true,
  }
)

const areaSchema = mongoose.Schema(
  {
    name: reqString,
    formattedName: formattedString(reqString),
    users: [userSchema],
  }
)

const locationSchema = mongoose.Schema(
  {
    name: reqString,
    formattedName: formattedString(reqString),
    areas: [areaSchema],
  }
)

module.exports = mongoose.model('locations', locationSchema)
