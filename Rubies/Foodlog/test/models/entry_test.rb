require "test_helper"

class EntryTest < ActiveSupport::TestCase
    test "is valid with valid attributes" do
        #entry = Entry.new(carbohydrates: 35, proteins: 50, fats: 20, calories: 1000)
        entry = Entry.new(meal_type: "Breakfast", carbohydrates: 35, proteins: 50, fats: 20, calories: 1000)
        assert entry.save
    end
end
