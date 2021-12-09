


const numberClusters = [[1,2], [3,4],[5,6]]

const target = numberClusters[2][1]

const numberClusters = [[1,2], [3,4],[5,6]]

const target = numberClusters[2][1]

const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];

groceryList.shift()
console.log(groceryList)

groceryList.unshift("popcorn")

console.log(groceryList)

console.log(groceryList.slice(1,4))
console.log(groceryList)

const pastaIndex = groceryList.indexOf("pasta")
console.log(pastaIndex)

const chores = ['wash dishes', 'do laundry', 'take out trash', 'cook dinner', 'mop floor'];

chores.pop()

console.log(chores)


const chores = ['wash dishes', 'do laundry', 'take out trash'];

chores.push("munch", "snack")

console.log(chores)

let condiments = ['Ketchup', 'Mustard', 'Soy Sauce', 'Sriracha'];

const utensils = ['Fork', 'Knife', 'Chopsticks', 'Spork'];

condiments[0] = "Mayo";

console.log(condiments);

condiments = ["Mayo"];

console.log(condiments);

utensils[3] = "Spoon";

console.log(utensils);
console.log(utensils.length);

const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];

let listItem = famousSayings[0]
const firstItem = famousSayings[0]

console.log(listItem)
console.log(famousSayings[2])
console.log(famousSayings[3]) // undefined



const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];

listItem = famousSayings[0]

console.log(listItem)


const hobbies = ["eat", "munch", "snack"]

console.log(hobbies)

const logVisibleLightWaves = () => {
  let lightWaves = 'Moonlight';
	let region = 'The Arctic';
  if  (region === "The Arctic"){
    let lightWaves = "Northern Lights";
    console.log(lightWaves);
  }
  console.log(lightWaves);
};

// the if statement does not change the first lightWaves assignment
logVisibleLightWaves();

const satellite = 'The Moon';
const galaxy = 'The Milky Way';
let stars = 'North Star';

const callMyNightSky = () => {
  stars = "Sirius";
	return 'Night Sky: ' + satellite + ', ' + stars + ', ' + galaxy;
};

console.log(callMyNightSky());
console.log(stars)


/* throws error 
const logVisibleLightWaves = () => {
  const lightWaves = "Moonlight";
  console.log(lightWaves)
}

console.log(logVisibleLightWaves())

console.log(lightWaves)
*/

const satellite = "The Moon";

const galaxy = "The Milky Way";

const stars = "North Star";

const callMyNightSky = () => {
  return "Night Sky: " + satellite + ", " + stars + ", and " + galaxy;
}

console.log(callMyNightSky())

const city = "New York City"

const logCitySkyline = () => {
  let skyscraper = "Empire State Building";
  return "The stars over the " + skyscraper + " in " + city;
}

console.log(logCitySkyline())

const plantNeedsWater = day => day === 'Wednesday' ? true : false;


const plantNeedsWater = (day) => {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};

const plantNeedsWater = function(day) {
  if (day === 'Wednesday') {
    return true;
  } else {
    return false;
  }
};



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
