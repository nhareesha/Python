# Creating a list of user defined objects using python lists
# This is a module and it can have any number of classes

from operator import attrgetter

class Country:

    def __init__(self, name, population, area):
        self.population = population
        self.area = area
        self.name = name

    def __repr__(self):
        return '{} {} {}'.format(self.name, self.population, self.area)


# Creating objects fot the class Country

countries = [Country("India", 100, 700), Country("China", 200, 500)] # creating a list of user defined objects

print(countries)

countries.append(Country("Russia",10,100))

print(countries)


# Sorting userdefined objects based on a attribute

# For accessing an attribute of the class we need to import a method attgetter from  module operator

# Sort countries based on location

# sort() is on the list where as sorted() is a builtin function of builtins module of python

# max() , min() , len() all these are builtin functions of the builtins module of python
cons = sorted(countries,key=attrgetter('area'))
print(cons)

countries.sort(key=attrgetter('population')) # sort, sorts the list inplace abd it doesnt return a new list.
print(countries)

print(max(countries,key=attrgetter('area')))
print(min(countries,key=attrgetter('area')))


