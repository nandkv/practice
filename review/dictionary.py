

# grade_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
# for grade in grade_dict:
#     print(grade, grade_dict[grade])

# grade_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
# for grade in grade_dict:
#     print(grade, grade_dict[grade])

# key, value pairs
inventory = {'dog toy': 3,'cat toy': 0, 'remote car':4}

# increment the value to 5 for all items

# inventory['dog toy'] = 5
# print(inventory['dog toy'])

for key in inventory.keys():
    inventory[key] = 5


walmart = {'toys': {'dog toy': 3,'cat toy': 0, 'remote car':4}, 'food': {'oreo': 3,'chips': 0, 'soda':4}}

print(walmart['toys']['cat nand'])
print(walmart['food'])