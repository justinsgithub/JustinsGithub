# ELEGANT RUBY

def square(num)
  puts "implicit return"
  num ** 2
end

favorite_animal ||= "cat"

puts "What's your favorite language?"

language = gets.chomp

case language
  when "Ruby" then puts "Ruby is great for web apps!"
  when "Python" then puts "Python is great for science."
  when "JavaScript" then puts "JavaScript makes websites awesome."
  when "HTML" then puts "HTML is what websites are made of!"
  when "CSS" then puts "CSS makes websites pretty."
  else puts "I don't know that language!"
end
    
puts 1 < 2 ? "One is less than two!" : "One is not less than two."


puts "One is less than two!" if 1 < 2

favorite_things = ["Ruby", "espresso", "candy"]

puts "A few of my favorite things:"

favorite_things.each do |thing|
  puts "I love #{thing}!"
end

alphabet = ["a", "b", "c"]
alphabet << "d" 
caption = "one, two, three, and "
caption << "four!"

age = 26

age.respond_to?(:next)

"L".upto("P") {|letter| puts letter} 

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_array.each {|num| puts num if num % 2 == 0 }

def a
  puts "A was evaluated!"
  return true
end

def b
  puts "B was also evaluated!"
  return true
end

puts a || b
puts "------"
puts a && b


def implicit_return(x=false)
  puts x ? "implicitely returning because true" : "implicitely returning because false"
end

# Write your code on line 2!
favorite_language ||= "Ruby"
puts favorite_language

puts "Hello there!"
greeting = gets.chomp

# Add your case statement below!
case greeting 
  when "English" then puts "Hello!"
  when "French" then puts "Bonjour!"
  when "German" then puts "Guten Tag!"
  when "Finnish" then puts "Haloo!"
  else puts "I don't know that language!'"
end


puts true ?  "true ternary" : "false ternary"

puts "one-liner" if true

puts "unless one-liner" unless false

