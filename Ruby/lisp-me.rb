puts "please enter some text i can lisp >  "

user_input = gets.chomp

while user_input == ''
  puts "you did give me no input ): > "
  user_input = gets.chomp
end

if user_input.include? "s" || "ce" || "S" || "CE" || "Ce"
  user_input.gsub!(/s/, "th")
  user_input.gsub!(/S/, "Th")
  user_input.gsub!(/ce/, "the")
  user_input.gsub!(/Ce/, "The")
  user_input.gsub!(/CE/, "THE")
  puts user_input
else
  puts "you did not give me anything i could lisp!! ): >"
  user_input = gets.chomp
end

test = "Ceasars Palace So Has The Nicest Niceties"

test_output = "Theatharth Palathe Tho Hath The Nithetht Nithetieth"