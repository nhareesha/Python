# List in python are very powerful .They exhibit all the features of arrays,lists in JAVA and very much more than that.

# Slicing and dicing is a great feature in List .

# A list in python can hold any kind of object type.It doesn't have any ristriction on types of elements present in the list.

# List is a comma separated list of objects.Objects can be of any type

list_numbers = [0,1,2,3,4]

print(max(list_numbers))

print(min(list_numbers))

print(sum(list_numbers))

print(len(list_numbers))

del list_numbers[2] # Deleting element based on the index

print(list_numbers)

list_numbers.remove(3) # Removes the value specified

print(list_numbers)

list_numbers.append(10) # Adds the given element at the end of the list

list_numbers.extend([11,22,33]) # Adds given list of elements to the end of the list

print(list_numbers)

print(list_numbers.index(4)) # Gives index of given element

print(4 in list_numbers) # this checks if the given element is present in the list

## Slicing and dicing in Python's Lists

list_str = ['Dad','Mom','Hareesha','Sireesha','Sunil','Sujith','Samanvi']

print(len(list_str))

print(list_str[1:2]) # 2nd index is exclusive

print(list_str[2:]) # prints all the elements from index 2.

print(list_str[:4]) # prints all the elements till index 4. And index 4 is exclusive

print(list_str)

print(list_str[1::2]) # This prints all the elements starting from given index to end [exclusive] and every 2nd element in the range

print(list_str[0:5:3])

# Printing list in reverse order

print(list_str)

print(list_str[::-1]) # this prints the list in reverse order

print(list_str[-1:2:-2]) #When reversing, the start index can be anything

## Replacing elements of the list

list_str[2:4] = ('Hello','Hola','Hey','What is this','what is happeing') # this replaces the elements with the corresponding elements and if there are any extra elements present it appends to range

print(list_str)

list_str[3:] = 'Hello' # Here it replaces all the elements with the corresponding elements from the right side of the list.

print(list_str)

# Deleting elements of the list

del list_str[2:4] # this deletes elements from index 2 till 3 , as 4 is exclusive

print(list_str)

# Reversing a list IN PLACE
list_str = ['Dad','Mom','Hareesha','Sireesha','Sunil','Sujith','Samanvi']

list_str.reverse() # this is inplace reverse and it changes the element indexes inside list given

print(list_str)
print(list_str[0])

# To access list in reverse order and not to change ordering of elements
list_str = ['Dad','Mom','Hareesha','Sireesha','Sunil','Sujith','Samanvi']
for l in reversed(list_str):
    print(l)

print(list_str[0])

# We can define a key - Which specifies the value for the key to use in sorting
list_str = ['Dad','Mom','Hareesha','Sireesha','Sunil','Sujith','Samanvi']

print(list_str.sort()) # this does the in place sorting of the list .It changes the index of the elements in side the list

#Not working - printing None

print(list_str.sort()) # Printing None

# We can do the sorting of the list , and it is NOT IN PLACE
list_str = ['Dad','Mom','Hareesha','Sireesha','Sunil','Sujith','Samanvi']

print(sorted(list_str,key=len,reverse=True))



