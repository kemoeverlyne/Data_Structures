x = {'a': 10, 'b': 9, 'c': 8, 'd': 7, 'e': 6, 'f': 5}
x.clear()  # clears a dictionary

x = {'a': 10, 'b': 9, 'c': 8, 'd': 7, 'e': 6, 'f': 5}
print(x.get('b'))  # returns value of a key

print(x.get('g'))

# if key is not found and defalt argument specified value is returned
print(x.get('h', 3))

# displays 3
x = {'a': 10, 'b': 9, 'c': 8, 'd': 7, 'e': 6, 'f': 5}

list(x.keys())
# returns a list of keys in a dictionary
#['a', 'b', 'c', 'd', 'e' 'f']


list(x.values())
# returns a list of values in a dictionary
#['10', '9', '8', '7', '6' '5']


x.pop('b')
# removes key from the dictionary if present and returns its value

# returns 9

x.popitem()
# removes a last key-value pair added from x returns it as tuple

# returns {'f':5}

x2 = {'a': 10, 'b': 9, 'g': 4}
x.update(x2)

# merges a dictionary with another dictionary

# returns {'a': 10, 'b': 9, 'c': 8, 'd': 7, 'e': 6, 'f': 5, 'g': 4}
