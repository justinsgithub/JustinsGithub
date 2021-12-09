# JavaScript Basics (JS)

- console is a panel that displays messages
- data is printed, or logged, to the console

- 7 fundamental data types
- strings
- numbers
- booleans
- null
- undefined
- symbol
- object
- 
- Numbers are any number without quotes: 23.8879
- Strings are characters wrapped in single or double quotes: 'Sample String'
- arithmetic operators + -  *  / %
- Objects include instances of data types 
- Objects can have properties
- properties are stored information 
- properties are denoted with . after the name of the object
- Objects can have methods which perform actions
- We can access properties and methods by using the . dot operator
- Built-in objects are collections of methods and properties


- Variables hold reusable data in a program and associate it with a name
- Variables are stored in memory.
- The var keyword is used in pre-ES6 versions of JS.
- let is the preferred way to declare a variable when it might be reassigned
- const is the preferred way to declare a variable with a constant value
- Variables that have not been initialized store the primitive data type undefined
- Mathematical assignment operators make it easy to calculate a new value and assign it to the same variable
- The typeof keyword returns a string with the data type of the passed value

- if statement executes a task if specified condition evaluates to true.
- if...else statements make binary decisions and execute different code blocks based on a provided condition.
- add more conditions using else if statements.
- comparison operators, including <, >, <=, >=, ===, and !== can compare two values.
- && checks if both provided expressions are truthy.
- || checks if either provided expression is truthy.
-  ! switches the truthiness and falsiness of a value.
- ? is shorthand to simplify concise if...else statements.
- switch statement can be used to simplify the process of writing multiple else if statements
-  switch statment break keyword stops the remaining cases from being checked and executed in a switch statement.

- a function is a reusable block of code that groups together a sequence of statements to perform a specific task.
 
- a parameter is a named variable inside a function’s block which will be assigned the value of the argument passed in when the function is invoked:

- ES6 introduces new ways of handling arbitrary parameters through default parameters 

- default parameters allow us to assign a default value to a parameter in case no argument is passed into the function.

- use return statement to get a value from a function.

- function definition can be made concise using concise arrow notation

- scope defines where a variable is accessible from inside a program
- Blocks are statements that exist within curly braces
- a variable in 
- global variables are accessible to the entire program / program context
- local variables are variables that exist within block scope / the block of code they are assigned
- global namespace is the space in our code that contains global data
- scope pollution is when too many variables exist in a namespace / globally or variable names are reused.

- Arrays are lists that store data
- Arrays are created with brackets
- Each item inside of an array is at an index starting at 0
- access item in array using its index
- change item in an array using its index
- Arrays have a length property
- length property allows you to see how many items are in an array
- Arrays have their own methods
- Array methods include .push() .pop() .slice() .shift() 
- Some built-in methods are mutating
- mutating methods change the array
- some array methods are not mutating
- variables that contain arrays can be declared with let or const
- Even when declared with const arrays are still mutable
- an array variable declared with const cannot be reassigned
- arrays mutated inside of a function will stay changed outside the function
- arrays can be nested inside other arrays
- To access elements in nested arrays chain indices using bracket notation

- loops perform repetitive actions so we don’t have to code that process manually every time
- how to write for loops with an iterator variable that increments or decrements
- how to use a for loop to iterate through an array
- a nested for loop is a loop inside another loop
- while loops allow for different types of stopping conditions
- stopping conditions are crucial for avoiding infinite loops.
- do...while loops run code at least once— only checking the stopping condition after the first execution
- the break keyword allows programs to leave a loop during the execution of its block

- abstraction allows writing complicated code in a cleaner way 
- clean code is easy to reuse, debug, and understand for human readers
- functions work the same way as any other type of data
- functions can be reassigned to new variables
- functions have properties and methods like any other object
- functions can be passed into other functions as parameters
- a higher-order function is a function that either accepts functions as parameters, returns a function, or both
