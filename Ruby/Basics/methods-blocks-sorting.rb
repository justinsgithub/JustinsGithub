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
