


class Application
  attr_accessor :status

  public
  def print_status
    puts "All systems go!"
  end
  
  private
  def password
    return 12345
  end
end

module ThePresent
    def now
      puts "It's #{Time.new.hour > 12 ? Time.new.hour - 12 : Time.new.hour}:#{Time.new.min} #{Time.new.hour > 12 ? 'PM' : 'AM'} (GMT)."
    end
end

class TheHereAnd
  extend ThePresent
end

module MartialArts
  def swordsman
    puts "I'm a swordsman."
  end
end


class Ninja
  include MartialArts
  def initialize(clan)
    @clan = clan
  end
end

class Samurai
  include MartialArts
  def initialize(shogun)
    @shogun = shogun
  end
end


module Action
  def jump
    @distance = rand(4) + 2
    puts "I jumped forward #{@distance} feet!"
  end
end

class Rabbit
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
  end
end

class Cricket
  include Action
  attr_reader :name
  def initialize(name)
    @name = name
  end
end

peter = Rabbit.new("Peter")
jiminy = Cricket.new("Jiminy")

peter.jump
jiminy.jump

class Angle
  include Math
  attr_accessor :radians
  
  def initialize(radians)
    @radians = radians
  end
  
  def cosine
    cos(@radians)
  end
end

acute = Angle.new(1)
acute.cosine


module MyCircle
  PI = 3.14159265358979323846
end

require "mycircle"
puts MyCircle::PI
puts Math::PI


module MyLibrary
  FAVE_BOOK = "Harry Potter"
end

class Person
  attr_reader :name
  attr_writer :favhoby
  attr_accessor :job
  def initialize(name, favhobby,job)
    @name = name
    @job = job
    @favhobby = hobby
  end
end

class Person
  def initialize(name, job)
    @name = name
    @job = job
  end
  
  def name
    @name
  end
  
  def job=(new_job)
    @job = new_job
  end
end

class Dog
  def initialize(name, breed)
    @name = name
    @breed = breed
  end

  public
  def bark
    puts "Woof!"
  end

  private
  def id
    @id_number = 12345
  end
end

class Computer
  @@users = {}
  def initialize(username, password)
    @username = username
    @password = password
    @files = {}
    @@users[username] = password
  end
  
  def Computer.get_users
    return @@users
  end

  def create(filename)
    time = Time.now
    @files[filename] = time
    puts "#{filename} was created at #{time} by #{@username}. "
  end
  
  def delete(filename)
    time = Time.now
    @files.delete(filename)
    puts "#{filename} was deleted at #{time} by #{@username}. "
  end
  def update(filename)
    time = Time.now
    @files[filename] = time
    puts "#{filename} was updated at #{time} by #{@username}. "
  end

end

my_computer = Computer.new("justinsname", "justinspass")


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
