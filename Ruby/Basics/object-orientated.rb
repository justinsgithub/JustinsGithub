class Message 
  @@messages_sent = 0
  def initialize(from, to)
    @from = from 
    @to = to 
    @@messages_sent +=1 
  end
end

class Email < Message
  def initialize(from, to)
    super
  end
end

my_message = Message.new("Ian", "Alex")


# throws error inheriting from multiple classes
=begin
class Creature
  def initialize(name)
    @name = name
  end
end

class Person
  def initialize(name)
    @name = name
  end
end

class Dragon < Creature; end
class Dragon < Person; end
=end

class Creature
  def initialize(name)
    @name = name
  end
  
  def fight
    return "Punch to the chops!"
  end
end

class Dragon < Creature
  def fight
    puts "Instead of breathing fire..."
    super
  end
end

class ApplicationError
  def display_error
    puts "Error! Error!"
  end
end

class SuperBadError < ApplicationError
end

err = SuperBadError.new
err.display_error

class Person

  @@people_count = 0
  
  def initialize(name,age,profession)
    @name = name
    @age = age
    @profession = profession
    @@people_count += 1
  end
  
  def self.number_of_instances

    return @@people_count    
  end
end

matz = Person.new("Yukihiro")
dhh = Person.new("David")

puts "Number of Person instances: #{Person.number_of_instances}"


class MyClass
  $my_variable = "Hello!"
end

puts $my_variable
