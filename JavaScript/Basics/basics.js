let athleteFinalPosition = 'first place';

switch (athleteFinalPosition) {
  case "first place":
    console.log("You get the gold medal!");
    break;
  case "second place":
    console.log("You get the silver medal!");
    break;
  case"third place":
    console.log("You get the bronze medal!")
    break;
  default:
    console.log("No medal awarded.");
    break;
}

let isLocked = false;

isLocked ? console.log('You will need a key to open the door.') :
  console.log('You will not need a key to open the door.');

let isCorrect = true;

isCorrect ? console.log('Correct!') :  console.log('Incorrect!');

let favoritePhrase = 'Love That!';

favoritePhrase === 'Love That!' ? console.log('I love that!') : console.log("I don't love that!")


let tool = 'marker';

let writingUtensil = tool || "pen"

console.log(`The ${writingUtensil} is mightier than the sword.`);

let wordCount = 1;

if (wordCount) {
  console.log("Great! You've started your work!");
} else {
  console.log('Better get to work!');
}


let favoritePhrase = '';

if (favoritePhrase) {
  console.log("This string doesn't seem to be empty.");
} else {
  console.log('This string is definitely empty.');
}

let mood = 'sleepy';
let tirednessLevel = 6;

if (mood === "sleepy" && tirednessLevel > 8){
  console.log("time to sleep")
} else {
  console.log("not bed time yet")
}

console.log(Math.random() * 100);

let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;

levelUp += 5;
powerLevel -= 100;
multiplyMe *= 11;
quarterMe /= 4;


console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

let gainedDollar = 3;
let lostDollar = 50;

gainedDollar ++;
lostDollar -- ;

const favoriteAnimal = "armadillo";

console.log("My favorite animal: " + favoriteAnimal);

const myName = "Justin";

const myCity = "Kenai";

console.log(`My name is ${myName}. My favorite city is ${myCity}.`;

let newVariable = 'Playing around with typeof.';

console.log(typeof newVariable);

newVariable = 1;
console.log(typeof newVariable);

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

