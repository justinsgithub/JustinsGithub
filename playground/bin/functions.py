import os
import re
import requests


my_string = "  my string to strip  "
print(my_string)

def f(a, b):
    remove_whitespace = re.sub("\s", "", a)

    sub_whitespace = re.sub("\s", "-", a)

    remove_dups = list(dict.fromkeys(a))

    strip = a.strip()

    reverse = a[::-1]

    does_exist = os.path.exists(a)

    cap = a.capitilize()

    lower = cap.lower()

    if b == "rmdir":
        os.rmdir(a)

    if b == "rm":
        os.remove(a)

    if b == "remove_whitespace":
        return remove_whitespace

    if b == "strip":
        return strip
    

my_string2 = my_string

my_string = f(my_string, "remove_whitespace")

my_string2 = f(my_string2, "strip")

print(my_string)
print(my_string2)


