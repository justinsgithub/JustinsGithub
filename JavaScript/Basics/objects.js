
function robotFactory(model, mobile){
  return {
    model: model,
    mobile: mobile,
    beep() {
      console.log('Beep Boop');
    }
  }
}

const robotFactory = (model, mobile) => {
  return {
    model,
    mobile,
    beep() {
      console.log('Beep Boop');
    }
  }
}

// To check that the property value shorthand technique worked:
const newRobot = robotFactory('P-501', false)
console.log(newRobot.model)
console.log(newRobot.mobile)
// To check that the property value shorthand technique worked:
const newRobot = robotFactory('P-501', false)
console.log(newRobot.model)
console.log(newRobot.mobile)


const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  get energyLevel() {
    if (typeof this._energyLevel === "number"){
      return `My current energy level is ${this._energyLevel}`
    } else {
      return "System malfunction: cannot retrieve energy level" 
    }
 },  
  _numOfSensors: 15,
  get numOfSensors(){
    if(typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    } else {
      return 'Sensors are currently down.'
    }
  },
  set numOfSensors(num){
    if(typeof this._numOfSensors === 'number' && num >= 0){
      this._numOfSensors = num
    } else {
      console.log("Pass in a number that is greater than or equal to 0")
    }
  },
  provideInfo(){
    return `I am ${this.model} and my current energy level is ${this.energyLevel}.`
  },
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};

const robotKeys = Object.keys(robot);
console.log(robotKeys);

const robotEntries = Object.entries(robot)

console.log(robotEntries);

const newRobot = Object.assign({
  laserBlaster: true,
  voiceRecognition: true
}, robot)

console.log(newRobot);
robot.numOfSensors = 100
console.log(robot.numOfSensors)
console.log(robot.energyLevel)

const { functionality } = robot

functionality.beep()

console.log(robot.provideInfo())



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
