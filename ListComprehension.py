# A list in python can have duplicate values.Same as Lists in Java
# Create a list with each of element length 4 from already existing elements

numbers = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
numbers_len4 = []

for num in numbers:
    if len(num)>=4:
        numbers_len4.append(num)


print(numbers_len4)

#List comprehension allows to specify the above logic in single statement.

numbers_len_four = [num for num in numbers if len(num)>=4] # this returns a new list with the elements satisfying the given condition
print(numbers_len_four)

# Find all the even numbers using list comprehension
values = [2,3,4,5,67,18,2]

vals_even = [val for val in values if val%2==0]
print(vals_even)

# List comprehension descreases the overhead that is caused by creating a empty list and then initiaizing it.

# Finding duplicates from a list

values_dups = [20,20,30,1,30,20,40]
print(values_dups.count(20))

values_non_dups = []


for val in values_dups:
    if values_dups.count(val) == 1:
        values_non_dups.append(val)

print(values_non_dups)


