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

  
