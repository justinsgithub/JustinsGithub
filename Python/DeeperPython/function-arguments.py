
# function arguments

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
