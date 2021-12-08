movies = {superman: 5}

puts "enter your choice"
choice = gets.chomp

case choice
  when "add"
    puts "enter movie title to add"
    title = gets.chomp
    if movies[title.to_sym]
      puts "movie already exists"
    else
      puts "enter movie rating"
      rating = gets.chomp
      movies[title.to_sym] = rating.to_i
      puts "movie saved"
    end
  when "update"
    puts "enter movie title to update"
    title = gets.chomp
    if !(movies[title.to_sym])
      puts "movie does not exist"
    else
      puts "enter movie rating"
      rating = gets.chomp
      movies[title.to_sym] = rating.to_i
      puts "movie updated"
    end
  when "display"
    movies.each {|movie, rating|
      puts "#{movie}: #{rating}"
    }
  when "delete"
    puts "enter movie title to delete"
    title = gets.chomp
    if !(movies[title.to_sym])
      puts "movie does not exist, nothing to delete"
    else
      movies.delete(title.to_sym)
    end
else 
    puts "Error!"
end
