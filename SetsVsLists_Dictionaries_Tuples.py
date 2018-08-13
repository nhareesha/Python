# List allows duplicate elements to be present and also List allows accessing of elements based on the index.

# Sets doesnt allows duplicate elements to be present and elements of the list cannot be accessed using the index.

# Set can be created using set([])

numbers_set = set([1,2,3,3]) # creation of set

print(numbers_set)

numbers_set_usingRange = set(range(10,20))
print(numbers_set_usingRange)

#Adding elements the set using add() methos and removing elements from the set using remove() method

numbers_set_usingRange.add(100)
numbers_set_usingRange.add(0)
numbers_set_usingRange.add(20)

numbers_set_usingRange.remove(15) # Removing a elements from the set
numbers_set_usingRange.remove(16)
numbers_set_usingRange.add(-1)
numbers_set_usingRange.add(15) # Adding an element from the Set
print(numbers_set_usingRange)

# In addition to the operations avaliable in Lists, like min(), max(), sum() , On sets we can do the operations like

# union(|) , intersection(&) and minus (-)

numbers_1_5 = set(range(1,6)) # Here 6 is exclusive
numbers_4_10 = set(range(4,11)) # Here 11 is exclusive

set_union = numbers_1_5 | numbers_4_10 # this combines elements from the given set and prints it.Removes the duplicates
print(set_union)

set_intersection = numbers_1_5 & numbers_4_10 # This will get the common elements from both the sets

print(set_intersection)

set_minus = numbers_1_5 - numbers_4_10 # this prints the elements from the first set that are not in the second set
print(set_minus)

# Dictionaries

# Dictionaries in Python are like key:value pair.Key and values can be any type.This is simmilar to HashMap in Java.
# Dictionaries can be created by using a class called dict
# Adictionary doesn't allow duplicate keys.Like HashMap in JAVA

dict_ex = dict(a=5, b=10, c=11, d=12, e=13)

print(dict_ex)

dict_ex['12']=13 # Adding an element to the dictionary.Key and value can be of any type in the dictionary
dict_ex['hello']=13 # Adding an element to the dictionary.Key and value can be of any type in the dictionary

print(dict_ex)

print(dict_ex.get('b')) # Gives 10. Getting an element from the dictionary using the key.

print(dict_ex['c']) # This also retrieves elements based on the Key.

dict_ex.keys(); # this return the set of all the Keys of the Dictionaries
dict_ex.values(); # This provides the set of values from the Dictionaries

print(type(dict_ex.keys())) # <class 'dict_keys'> is the type of the object

print(type(dict_ex.values())) # <class 'dict_values'> is the type of values returned from the Dictionaries

print(dict_ex.items()) # This prints the items of the dictionary as tuples

for i in dict_ex.keys():
    print(dict_ex[i]) # This prints all the values for given keys

#Tuples : Tuples in Python are set of values separated by commas.The main difference between Tuple and List is that Tuple once created cannot be
# changed, means it is immutable.

# Tuple usually represent set of attribute values for ceratin type.

# List is comma separated values.
# One common usage of Tuple is that if we want to return multiple values from a method , then we can create a tuple and return.
# Also indivudual elements of the tuple can be accessed.
# Tuple can be accessed using the index, same like List
tuple_ex = ('Hello','This is tuple',1,'this is another value in tuple')
print(tuple_ex)

for t in tuple_ex:
    print(tuple_ex.index(t)) # For each values of the tuple this gives the index of that value in the tuple


def tuple_return():
    return ('Hareesha','Sunil','Samanvi')
print(tuple_return())

x=1
y=2

tuple_xy = x,y # A tuple can simply be created by separating values by commas

print(type(tuple_xy))

x,y = y,x # tuple makes it very easy to do a swap

print(x,y)

# We can create a tuple using just one element also

tuple_one_ele = (0,) # this creates the single element tuple

print(tuple_one_ele[0]) # This prints the element of the tuple at the index 0
#tuple_one_ele[0] = 'Hello'
#print(tuple_one_ele[1]) # Once a tuple is created it doesnt allow to reassign any value to the tuple.It is a immutable DS




