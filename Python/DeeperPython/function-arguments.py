# function arguments


## BAD - for most use cases, same array is used every time 
def add_signature_message(signature_message, list_of_paragraphs=[]):
  list_of_paragraphs.append(signature_message)
  return list_of_paragraphs

def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

# Write your code below: 

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)

nums_collection = [1, 2, 3]

def power_two(*nums):
  for num in nums:
    print(num**2)
    
power_two(*num_collection)

my_tuple = (3,4,5)

merged_tuple = (1,2,*my_tuple,6,7)

a, *b, c = [1,2,3,4,5] 

start_stop = [3, 6]

range_values = range(*start_and_stop)
print(list(range_values))


nums2 = ["n1": 3, "n2": 6, "n3": 8]
nums = [3, 6, 9]

def sum(n1, n2, n3):
  print(n1 + n2 + n3)
  
sum(*nums)
sum(**nums2)
  
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)


single_prix_fixe_order("Baby Beets", "Salmon, Scallops", sides="Mashed Potatoes", dessert="Vanilla,  Cookies and Cream")

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')

assign_food_items(2, food="Seabass, Gnocchi, Pizza", drinks="Margarita, Water")

print(tables)
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}


# Write your code below: 
print(tables)

def assign_food_items(**order_items):
  print(order_items)
  food = order_items.get("food")
  drinks = order_items.get("drinks")
  print(food)
  print(drinks)

# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Write your code below: 

def assign_and_print_order(table_number, *order_items):
  tables[table_number]["order"] = order_items
  for item in order_items:
    print(item)

assign_table(2, "Arwa", True)
assign_and_print_order(2, "Steak", "Seabass", "Wine Bottle")
print(tables)


def truncate_sentences(8, *sentences):
  for sentence in sentences:
    print(sentence[:length])

def shout_strings(*args):
  for argument in args:
    print(argument.upper())

shout_strings("these", "will", "all", "be", "capitalized")

  

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Write your code below: 

def assign_table(table_number, name, vip_status=False):
  tables[table_number] = [name, vip_status]

assign_table(6, "Yoni", False)

assign_table(table_number=3, name="Martha", vip_status=True)

assign_table(4, "Karla")

print(tables)
