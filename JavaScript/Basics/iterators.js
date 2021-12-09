// ITERATORS


const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

const secretMessage = animals.map(animal => animal[0])

console.log(secretMessage.join(''));

const bigNumbers = [100, 200, 300, 400, 500];

const smallNumbers = bigNumbers.map(num => num / 100)
const programmingLanguages = ["python", "ruby", "rust"];
programmingLanguages.forEach(lang => console.log(lang));

const nums = [1,2,3];
const squareNums = nums.map(num => num ** 2);

const stuff = ["chair", "desk", "wallet", 5, 2, {"phrase": "words"}];

const stuffStrings = stuff.filter(item => typeof item === "string");

const noNumbers = stuff.filter(item => typeof item === "number");
