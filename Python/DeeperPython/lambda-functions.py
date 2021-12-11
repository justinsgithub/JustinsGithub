def add_two(my_input):
  return my_input + 2

add_two = lambda my_input: my_input + 2

def check_if_A_grade(grade):
  if grade >= 90:
    return "Got an A!"
  
  return "did not get an A."

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
