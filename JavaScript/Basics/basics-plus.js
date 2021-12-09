
// HIGH ORDER FUNCTIONS

const timeFunctionRuntime = (functionParameter) => {
  const t1 = Date.now();
  functionParameter();
  const t2 = Date.now(); 
  return t2 - t1;
}

const addTwo = num => num + 2;



const checkConsistentOutput = (x, y) => {
  if (x(y) === x(y)){
    return x(y)
  } else {
    return "This function returned inconsistent results";
  }
}

console.log(checkConsistentOutput(addTwo, 5));
