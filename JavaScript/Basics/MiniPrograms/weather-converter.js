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
