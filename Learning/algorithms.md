# algorithms

## what are they?

- an algorithm is a set of steps that is created to solve a problem
- the key to alogrithms is choosing the correct one to solve the specified problems
- there are many different types of alogrithms that solve certain problems better than others
- the main factors in determining a good algorithm is one that is solves the problem correctly and does it as efficiently as possible
- just because an algorithm gets the job done, does not mean it was a job well done, such as if it took more than steps than necessary and took more time than needed 

## implementing alogrithms in programming

- explaining an algorithm or how to do something to another human is less detailed than to a computer
- we assume our fellow human has some basic knowlowedge of how to do some of the steps in our instructions
- if we are teaching someone how to make a recipe with milk, we assume we don't have to tell them how to open the fridge
- computers never have this basic knowledge when implementing a new feature or algorithm or automated task, so we need to think about every little detail we want to explain
- what are the inputs tp the problem, what type of outputs do we expect, a string or number?
- what variables need to be created initally, and during the program running?
- what possiblities are conditional based on what the output is?
- which part of a program need to be put into a loop until a specific outcome or result or condition is found?


## linear search 

- let's say you were looking for a certain user_id in a database of users from the united states
- let's say this database had a cluster of servers in each state so that users data was stored closer to them and give all users equal speed on the application 
- lets say a user goes to log in with a username and we have to check the database to see what id lines up with that username.
- if we did not know what state that user was in by ip address or cookies, than we would have to start with id 1 and search through each until we found the right username that would line up with this user 
- this is where we would want to perform a linear search so we are organized and not randomly guessing numbers hoping we do not forget or miss one

## binary search 

- an algorithm for finding an item in sorted list of data, such as numerically or alphabetically
- Lets say we have a user with a stored cookie or some other way of knowing their I.D.
- We still have to look in the database to match up their password
- If we have 100 users and the i.d. is 70, we would hop to jump to spot 70 and find that id, but that is not the case
- Because of users that have joined and then left, we might have 100 ids, but #70 probably would not be at that 70 position anymore
- This where we could do a binary search and start from the middle.
- If #50 is actually id 80, we would guess lower, else we would guess higher
- Each time we would split the range of guesses in half until we found the position containing the i.d.


## binary search pseudocode
- Let minimum = 0 and maximum = n-1.
- Compute guess as the average of maximum and minimum, rounded down (so that it is an integer).
- If array[guess] equals target, then stop. You found it! Return guess.
- If the guess was too low, that is, array[guess] < target, then set minimum = guess + 1.
- Otherwise, the guess was too high. Set maximum = guess - 1.
- Go back to step 2.


## Asymptotic Analysis

- a technique to measure efficiency of an algorithm
- allows algorithms to be compared independently of the language implementation or hardware

