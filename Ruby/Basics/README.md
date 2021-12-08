# Ruby Basics


## BLOCKS, PROCS, AND LAMBDAS

- a Ruby block is a little "block" of code that can be executed

- A Block is not an object

- Block syntax uses either do..end or curly braces ({})

- Blocks can be combined with methods like .each and .times to execute an instruction for each 
element in a collection (like a hash or array)

- .collect method takes a block and applies the expression in the block to every element in an array

- .collect returns a copy, but doesn’t change (or mutate) the original

- yield allows Blocks being ran inside methods

- a lambda checks the number of arguments passed to it, a proc does not

- a lambda will throw an error if you pass it the wrong number of arguments

- a proc will ignore unexpected arguments and assign nil to any that are missing

- when a lambda returns, it passes control back to the calling method

- when a proc returns, it does so immediately, without going back to the calling method

- .collect! and .map! do the exact same thing

- & can be used to convert a proc into a block 
 
- .collect! and .map! normally take a block

-  use & any time we pass a proc to a method that expects a block







