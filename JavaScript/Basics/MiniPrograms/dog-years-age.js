
// age in dog years

// setting variable as my age
let myAge = 26;
const myName = "Justin".toLowerCase();
// the first 2 years in a dog's life age faster than the rest 
const earlyYears = 2;

// the toll in human years that the first 2 years takes on a dog
const earlyYearsToll = earlyYears * 10.5;

// the remaining years of my age to calculate
const laterYears = myAge - earlyYears;

// the toll in human years the rest of the years past the age of 2 take on a dog
const laterYearsToll = laterYears * 4;

// my age in dog years (very old because dogs normally do not live this long)
const myAgeInDogYears = earlyYearsToll + laterYearsToll;

console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`)
