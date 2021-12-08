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

  
