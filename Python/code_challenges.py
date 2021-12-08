def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent)
        return True
    return False

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

def twice_as_large(num1, num2):
    if num1 > (num2 * 2):
        return True
    return False
    
def divisible_by_ten(num):
    if not num % 10 == 0:
        return False
    return True

def not_sum_to_ten(num1, num2):
    if num1 + num2 == 10:
        return False
   return True

