

def is_good(fruit):
    if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
        return True
    else:
        return False

def fruits(fruits_list):
    dict = {}
    for fruit in fruits_list:
        if is_good(fruit):
            if fruit['name'] in dict:
                dict[fruit['name']] += 1
            else:
                dict[fruit['name']] = 1
    return dict

print( fruits ((
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})) )