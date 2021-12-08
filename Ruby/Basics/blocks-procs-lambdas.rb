# BLOCKS PROCS LAMBDAS

strings = ["leonardo", "donatello", "raphael", "michaelangelo"]

symbolize = lambda {|parameter| parameter.to_sym}

symbols = strings.collect(&symbolize)
print symbols

def lambda_demo(a_lambda)
  puts "I'm the method!"
  a_lambda.call
end

lambda_demo(lambda { puts "I'm the lambda!" })

numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

strings_array = numbers_array.map(&:to_s)

puts strings_array

hi = Proc.new {puts "Hello!"}

hi.call

def greeter
  yield
end

phrase = Proc.new {puts "Hello there!"}

greeter(&phrase)

# at the amusement park, you have to be four feet tall or taller to ride the roller coaster. 
# use .select on each group to get only the ones four feet tall or taller.

group_1 = [4.1, 5.5, 3.2, 3.3, 6.1, 3.9, 4.7]
group_2 = [7.0, 3.8, 6.2, 6.1, 4.4, 4.9, 3.0]
group_3 = [5.5, 5.1, 3.9, 4.3, 4.9, 3.2, 3.2]

over_4_feet = Proc.new { |height| height >= 4 }

can_ride_1 = group_1.select(&over_4_feet) 
can_ride_2 = group_2.select(&over_4_feet)
can_ride_3 = group_3.select(&over_4_feet)

puts can_ride_1
puts can_ride_2
puts can_ride_3

floats = [1.2, 3.45, 0.91, 7.727, 11.42, 482.911]

round_down  = Proc.new {|decimal| decimal.floor}

ints = floats.collect(&round_down)
print ints

multiples_of_3 = Proc.new do |n|
  n % 3 == 0
end

print (1..100).to_a.select(&multiples_of_3)

def double(num)
  puts "double parameter with a block"
  puts "Y to confirm, CTRL-C to rewrite method call"
  confirm = gets.chomp
  test = yield(num)
  if num * 2 == test
    puts "good job"
  else
    puts "you did not double the parameter, should have been #{num * 2}"
  end
  return test
end

puts double(5) {|num| num * 3}
def yield_name(name)
  puts "In the method! Let's yield."
  yield("Kim")
  puts "In between the yields!"
  yield(name)
  puts "Block complete! Back in the method."
end

yield_name("Eric") { |n| puts "My name is #{n}." }

yield_name("Justin") { |n| puts "My name is #{n}." }

def block_test
  puts "We're in the method!"
  puts "Yielding to the block..."
  yield
  puts "We're back in the method!"
end

block_test { puts ">>> We're in the block!" }


fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

doubled_fibs = fibs.collect {|fib| fib * 2}


5.times {puts "I'm a block!"}
