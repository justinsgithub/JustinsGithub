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


