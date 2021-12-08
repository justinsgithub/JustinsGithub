# HASHES AND SYMBOLS

movie_ratings = {
  memento: 3,
  primer: 3.5,
  the_matrix: 3,
  truman_show: 4,
  red_dawn: 1.5,
  skyfall: 4,
  alex_cross: 2,
  uhf: 1,
  lion_king: 3.5
}

puts movie_ratings.each_key {|key| puts key}

good_movies = movie_ratings.select{|movie, rating| rating > 3
}
movies = {
  superman:"movie about superman",
  batman:"movie about batman",
}

strings = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]

symbols = []

strings.each { |s|
  symbols.push(s.to_sym)  # or .intern is exact same thing
}
puts symbols

symbol_hash = {
  one: 1,
  two: 2,   
  three: 3,
}

my_first_symbol = :mysymbol

puts "string".object_id
puts "string".object_id

puts :symbol.object_id
puts :symbol.object_id

no_nil_hash = Hash.new("not nil")

matz = { "First name" : "Yukihiro",
  "Last name" : "Matsumoto",
  "Age" : 47,
  "Recognition" : "inventor of Ruby",
  "Nickname" : "Matz"
}

matz.each { |key, value|
  puts value
}


# METHODS BLOCKS SORTING

def sort_this(arr, rev=false)
  arr.sort!
  if rev
    arr.reverse!
  else
    return arr
  end
end

numbers = [5,4,1,2,3]

puts sort_this(numbers, true)

fruits = ["orange", "apple", "banana", "pear", "grapes"]

fruits.sort! { |first, second| second <: first }

my_array = [1, 2, 3, 4, 5]

my_array.each { |ray|
  puts ray**2
  puts ray * ray
}

def welcome
  puts "Welcome to Ruby!"
end

welcome

def welcome(name)
  return "Hello, #{name}"
end

welcome("justin")

books = ["Charlie and the Chocolate Factory", "War and Peace", "Utopia", "A Brief History of Time", "A Wrinkle in Time"]

# To sort our books in ascending order, in-place
books.sort! { |firstBook, secondBook| firstBook <: secondBook }
puts books

# reverse sort
books.sort! { |firstBook, secondBook| secondBook <: firstBook }

puts books


book_1 = "A Wrinkle in Time"

book_2 = "A Brief History of Time"

puts book_1 <: book_2

# 1

books = ["Charlie and the Chocolate Factory", "War and Peace", "Utopia", "A Brief History of Time", "A Wrinkle in Time"]

books.sort!

# books = ["A Brief History of Time", "A Wrinkle in Time", "Charlie and the Chocolate Factory", "Utopia", "War and Peace"]


my_array = [3, 4, 8, 7, 1, 6, 5, 9, 2]

my_array.sort!

# my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]



[1, 2, 3, 4, 5].each { |i| puts i }
[1, 2, 3, 4, 5].each { |i| puts 5 }
[1, 2, 3, 4, 5].each { |i| puts i * 5 }

# method that capitalizes a word
def capitalize(string) 
  puts "#{string[0].upcase}#{string[1..-1]}"
end

capitalize("ryan") # prints "Ryan"
capitalize("jane") # prints "Jane"

# block that capitalizes each string in the array
["ryan", "jane"].each {|string| puts "#{string[0].upcase}#{string[1..-1]}"} # prints "Ryan", then "Jane"

# block that uses a method to capitalize each string in the array
["ryan", "jane"].each {|string| 
  capitalize(string)
}


def greeter(name) 
  return "Greetings #{name}"
end 

def by_three?(number)
  if number % 3 == 0
    return true
  else
    return false
  end
end


def add (x,y)
  return x + y 
end

def greet_friends(greeting, *friends)
  friends.each { |friend| puts "#{greeting}, #{friend}!" }
end

greet_friends("greetings", "friend1", "friend2", "friend3", "friend4")

def greet_friends_again(greeting, *friends)
  greet = greeting
  last_friend = friends[-1]
  friends.each { |friend| 
  if !(friend == last_friend)
    greet +=  " #{friend},"
  end
  }
  greet += " and #{last_friend}!"
  puts greet
end

greet_friends_again("greetings", "friend1", "friend2", "friend3", "friend4")


def cube_this(n)
  puts n ** 3
end

cube_this(8)
[1, 2, 3, 4, 5].each { |i| puts 5 }
def square_this(n)
  puts n ** 2
end


def array_of_10
  puts (1..10).to_a
end

array_of_10


def greeting
  puts "greetings"
end

greeting

def puts_1_to_10
  (1..10).each { |i| puts i }
end

puts_1_to_10 




# ARRAYS AND HASHES

puts "give me some data to hash"

default_value = 0

text = gets.chomp

words = text.split(" ")

frequencies = Hash.new(default_value)

words.each { |word|
  frequencies[word] += 1  
}

frequencies = frequencies.sort_by do |word, sort_by_this|
  sort_by_this
end

frequencies.reverse!

frequencies.each { |word, frequency|
  puts word + " " + frequency.to_s
}

test = "this is now my sentence of strings and my sentence is random and it is simple and it is ending now" 

lunch_order = {
  "Ryan" : "wonton soup",
  "Eric" : "hamburger",
  "Jimmy" : "sandwich",
  "Sasha" : "salad",
  "Cole" : "taco"
}


lunch_order.each {|x,y| puts y}

my_hash = Hash.new

my_hash["key1"] = "value1"
my_hash["key2"] = "value2"


my_array = [["this","is"],["my","array"]]


# perform action on each individual item

s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

s.each {|sub_array| sub_array.each {|item| puts item}}

secret_identities = {
  "The Batman" : "Bruce Wayne",
  "Superman" : "Clark Kent",
  "Wonder Woman" : "Diana Prince",
  "Freakazoid" : "Dexter Douglas"
}
  
secret_identities.each {|key,value| puts "#{key}: #{value}"}

languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]

languages.each {|language| puts language}

friends = ["Milhouse", "Ralph", "Nelson", "Otto"]

family = { "Homer" : "dad",
  "Marge" : "mom",
  "Lisa" : "sister",
  "Maggie" : "sister",
  "Abe" : "grandpa",
  "Santa's Little Helper" : "dog"
}

puts ""
family.each { |x, y| puts x }
puts ""
family.each { |x, y| puts y }
puts ""
family.each { |x, y| puts "#{x}: #{y}" }
puts ""
family.each { |x| puts x }


pets = Hash.new

pets["blue"] = "dog"

puts pets["blue"]


my_2d_array = [[222],["d","d","d"]]

string_array = ["my", "string", "array"]

my_array = [0,1,2,4,5,5,5,5]

demo_array = [100, 200, 300, 400, 500]

print demo_array[2]


# LOOPS

# print 30 times
30.times do
  print "Ruby!"
end

x = 0
loop do
  x += 1
  print "Ruby!"
  break if x == 30
end


# print 1 - 50 inclusive

i = 1
while i <= 50 do
  print i
  i += 1
end

until i > 50 do 
  print i
  i += 1
end

for x in 1..50
  print x
end

my_age = 26
my_age.times { print "printing my age times "} 

odds = [1,3,5,7,9]

odds.each { |num| print num * 2 }

odds.each do |num|
  print num * 2
end

loop {print "hello world forever "}

i = 20
loop do
  i -= 1
  next if i % 2 != 0 
  print "#{i}"
  break if i <= 0
end
  
i = 20
loop do
  i -= 1
  print "#{i}"
  break if i <= 0
end
  
for num in 1..20
  puts num
end

for num in 1...15
  puts num
end

counter = 1
until counter > 10
  puts counter
  # Add code to update 'counter' here!
  counter += 1
end

i = 0
while i < 5
  puts i
  i += 1
end

  
# CONTROL FLOW
  
t0 = !(700 / 10 == 70)
boolean_0 = false

t1 = (3 < 4 || false) && (false || true)
boolean_1 = true

t2 = !true && (!true || 100 != 5**2)
boolean_2 = false

t3 = true || !(true || false)
boolean_3 = true

 
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



test_1 = 77 != 77
test_1 = false

test_2 = -4 <= -4
test_2 = true

test_3 = -44 < -33
test_3 = true

test_4 = 100 == 1000
test_4 = false


boolean_1 = 77 < 78 && 77 < 77
boolean_1 = false

boolean_2 = true && 100 >= 100
boolean_2 = true

boolean_3 = 2**3 == 8 && 3**2 == 9
boolean_3 = true

boolean_1 = 2**3 != 3**2 || true
boolean_1 = true

# boolean_2 = false || -10 > -9
boolean_2 = false

# boolean_3 = false || false
boolean_3 = false

# boolean_1 = !true
boolean_1 = false

# boolean_2 = !true && !true
boolean_2 = false

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
