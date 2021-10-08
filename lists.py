# using For and In constructs with lists
# For Var in list

squares = [5, 7, 9, 6, 3]
sum = 0
for num in squares:
    sum += num
    print(sum)

# using the in construct on its own- testing if a conntruct appears in a list

list = ['kemo', 'ken', 'kate']
if 'kemo' in list:
    print("That's right")


"""
while loops give total control over the index numbers  i.e 
yu can access any element in a list
"""
i = 0
a = [3, 5, 6, 7, 8, 9]
while i < len(a):
    print(a[i])
    i = i + 3
