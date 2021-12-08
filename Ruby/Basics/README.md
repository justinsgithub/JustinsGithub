# Lambdas vs. Procs
 
- main differences

- a lambda checks the number of arguments passed to it, a proc does not
- a lambda will throw an error if you pass it the wrong number of arguments
- a proc will ignore unexpected arguments and assign nil to any that are missing
- when a lambda returns, it passes control back to the calling method
- when a proc returns, it does so immediately, without going back to the calling method.
