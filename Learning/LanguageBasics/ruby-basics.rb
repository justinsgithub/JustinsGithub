# Ruby Comment

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

puts "type Y to continue, H for help"
answer = gets.chomp
if answer.upcase == "Y"
  puts "you chose yes"
elsif answer.upcase == "H"
  puts "sorry no help here"
else 
  puts "qutting now"
end

hungry = false

unless hungry
  puts "I'm writing Ruby programs!"
else
  puts "Time to eat!"
end

is_true = 2 != 3

is_false = 2 == 3

puts is_false
puts is_true



#test_1 = 17 > 16

#test_2 = 21 < 30

#test_3 = 9 <= 9

#test_4 = -11 < 4


# test_1 = 77 != 77
test_1 = false

# test_2 = -4 <= -4
test_2 = true

# test_3 = -44 < -33
test_3 = true

# test_4 = 100 == 1000
test_4 = false


# boolean_1 = 77 < 78 && 77 < 77
boolean_1 = false

# boolean_2 = true && 100 >= 100
boolean_2 = true

# boolean_3 = 2**3 == 8 && 3**2 == 9
boolean_3 = true

# boolean_1 = 2**3 != 3**2 || true
boolean_1 = true

# boolean_2 = false || -10 > -9
boolean_2 = false

# boolean_3 = false || false
boolean_3 = false

# boolean_1 = !true
boolean_1 = false

# boolean_2 = !true && !true
boolean_2 = false

# boolean_3 = !(700 / 10 == 70)
boolean_3 = false

# boolean_1 = (3 < 4 || false) && (false || true)
boolean_1 = true

# boolean_2 = !true && (!true || 100 != 5**2)
boolean_2 = false

# boolean_3 = true || !(true || false)
boolean_3 = true

if 6 < 5 || 6 == 5
  puts "6 is less than 5"
elsif 6 > 7 || 687 == "six ate 7"
  puts "6 is greater than 7"
else
  puts "idk wtf is going on"
end

my_bday = "october"

this_month = "december"

unless this_month == my_bday
  puts "not my bday month"
end

problem = false

print "Good to go!" unless problem

# test_1 should be false
test_1 = 10 > 199

# test_2 = should be false
test_2 = "hi" == "bye"

# test_3 = should be true
test_3 = 100 == 100


# test_1 should be true
test_1 = true && true

# test_2 = should be true
test_2 = false || true

# test_3 = should be false
test_3 = false && false
