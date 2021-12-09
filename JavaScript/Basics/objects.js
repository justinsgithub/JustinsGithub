let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';



let spaceship = {
  homePlanet: 'Earth',
  color: 'silver',
  'Active Mission' : true,
  'Fuel Type': 'Turbo Fuel',
  numCrew: 5,
  'Secret Mission' : 'Discover life outside of Earth.',
  flightPath: ['Venus', 'Mars', 'Saturn'],
  passengers: null,
  telescope: {
    yearBuilt: 2018,
    model: "91031-XLT",
    focalLength: 2032 
  },
  crew: {
    captain: { 
      name: 'Sandra', 
      degree: 'Computer Engineering', 
      encourageTeam() { console.log('We got this!') },
     'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
  },
  engine: {
    model: "Nimbus2000"
  },
  nanoelectronics: {
    computer: {
      terabytes: 100,
      monitors: "HD"
    },
    'back-up': {
      battery: "Lithium",
      terabytes: 50
    }
  },  
  retreat(){ console.log(retreatMessage) },
  akeOff(){ console.log("Spim... Borp... Glix... Blastoff!") }
};
spaceship.passengers = [
  {firstName:"larry", lastName:"smith"},
  {firstName:"jessica"},
  {firstName:"stan"}
]

for (let passenger in spaceship.passengers){
  console.log(`passenger name: ${spaceship.passengers[passenger]}`)
}
for (let crewmember in spaceship.crew){
  console.log(`${spaceship.crew[crewmember].name}: ${spaceship.crew[crewmember].degree}`)
}
const firstPassenger = spaceship.passengers[0]
const isActive = spaceship["Active Mission"]
const crewCount = spaceship.numCrew;
const planetArray = spaceship.flightPath;
const capFave = spaceship.crew.captain["favorite foods"][0];

const greenEnergy = thisObject => thisObject["Fuel Type"] = "avocado oil"
const remotelyDisable = obj => obj.disabled = true

greenEnergy(spaceship)
remotelyDisable(spaceship)

spaceship.takeOff()
spaceship.retreat()


let propName =  'Active Mission';

spaceship.numEngines = 5
spaceship.color = "glorious gold"
console.log(spaceship[propName])


delete spaceship.propName
