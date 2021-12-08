# VERY BASICS

my_num =  25  
my_boolean = true 
my_string = "Ruby"
puts my_num
puts my_boolean
puts my_string
puts "What's up?"
puts "Oxford Montalvo" # new line
print "What's up?"
print "Oxford Montalvo" # same line
puts "puts 6".length
puts "erehT olleH".reverse
puts "Justin".upcase 
puts "Justin".downcase 

=begin
I'm 
a 
multi-line
comment
=end

sum  = 13 + 379
product = 923 * 15
quotient = 13209 / 17

name = "Justin"
name.downcase
name.reverse
name.upcase

name = "Justin"
name.downcase.reverse.upcase

print("What's your first name?")
first_name = gets.chomp
puts "Your first name is #{first_name}!"


print("What is your last name?")
last_name = gets.chomp
puts "Your last name is #{last_name}!"

print("What city are you from?")
city = gets.chomp
puts "Your hometown is #{city}!"

print("What's the abbreviation of the state you are from?")
state = gets.chomp
puts "You are from #{state}!"

print("What's your first name?")
first_name = gets.chomp
first_name.capitalize!
puts "Your first name is #{first_name}!"


print("What is your last name?")
last_name = gets.chomp
last_name.capitalize!
puts "Your last name is #{last_name}!"


print("What city are you from?")
city = gets.chomp
city = city.capitalize!
puts "Your hometown is #{city}!"

print("What's the abbreviation of the state you are from?")
state = gets.chomp
state.upcase!
puts "You are from #{state}!"
# control flow

print "Integer please: "
user_num = Integer(gets.chomp)
puts user_num
