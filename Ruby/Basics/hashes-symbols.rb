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


