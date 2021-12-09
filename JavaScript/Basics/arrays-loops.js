const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

for(let i = 0; i < rapperArray.length; i++){
  console.log(rapperArray[i]); 
  if (rapperArray[i] === "Notorious B.I.G."){
    break
  }
}

console.log("And if you don't know, now you know.")

const cupsOfSugarNeeded = 5;

let cupsAdded = 0;

do{
  cupsAdded++
  console.log(cupsAdded)
} while(cupsAdded < cupsOfSugarNeeded);

const cards = ['diamond', 'spade', 'heart', 'club'];

let currentCard;

while(currentCard !== "spade"){
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard)
}


const bobsFollowers = ["alex", "richard", "michael", "nick"]

const tinasFollowers = ["alex","nicole","michael"]

const mutualFollowers = []

for (let x = 0; x < bobsFollowers.length; x++){
  for (let y = 0; y < tinasFollowers.length; y++){
    if(bobsFollowers[x] === tinasFollowers[y]){
      mutualFollowers.push(bobsFollowers[x])
    }
  }
}


const vacationSpots = ['Bali', 'Paris', 'Tulum'];

for(let i = 0; i < vacationSpots.length; i ++){
  console.log(`I would love to visit ${vacationSpots[i]}`)
}

for (let counter = 3; counter >= 0; counter--){
  console.log(counter);
}

for(let i = 5; i < 11; i++){
  console.log(i)
}

const x = [1,2,3]

y = `it's as easy as  ${x.map(z => z.toString()).join(", ")}... I mean ${x.reverse().map(a => a.toString()).join(", ")}`

console.log(y)

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
