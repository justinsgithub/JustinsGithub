// weather converter

// the weather forecast today
let kelvin = 293

// converting kelvin to celsius
const celsius = kelvin - 273
console.log(`The temperature is ${celsius} in fahrenheit`)
// converting celsius to fahrenheit
const fahrenheit = Math.floor(celsius * (9/5) + 32)

const newton = Math.floor(celsius * (33 / 100))

console.log(`The temperature is ${fahrenheit} in fahrenheit`)

console.log(`The temperature is ${newton} in newton`)

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

