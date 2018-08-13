# In Python , functions are first class citizens.

# Functions can be passed as arguments to another functions.Functions can be assigned to varaibles.

# Functions are more like objects.

from functools import reduce

def add_nums(num1,num2):
    return num1+num2

print(type(add_nums)) # the type og this function is <class 'function'>

#We can also assign this function to another variables.The variable to which this function is assigned will hold the reference of the function.

add_num_func_assign = add_nums # this assigns add_nums function to the add_num_func_assign variable

print(type(add_num_func_assign)) # Now type of this varaible is also a function

## We can also pass function as an argument in the method call

def receive_func(func):
    print(type(func)) # Here it is type of function
    return func(10,20)


print(receive_func(add_nums))

# Lambda : Lambda is used to create a quick inline function and pass as an argument to another function.
# Lambda is piece of code that is passed as an argument to another function.

# Lambda help in avoiding to write lot of functions which have similar behaviour with little variation


# arg->arg*3  - In Java
# lambda arg:arg*3 - In Python - In python we need to preceed with keyword "lambda"


def use_lambda(func,data): # here func is a function that is passed to method use_lambda
    return func(data)

def multiply_2(data):
    return data*3

print(use_lambda(multiply_2,40)) # Directly passing function reference as a parameter

# Now we can pass the actual piece of code instead of passing "multiply_2" function

print(use_lambda(lambda arg:arg*3,100))

# Here instead of defining separate method, we ca actually define a lambda, if it is simple function.We dont have to define a full fledged method.
##########################
# More lambdas
##########################
# In order for us to define a lambda ,we need to have a function that accepts a function first

print(use_lambda(lambda arg:len(arg),"Hareesha"))

print(use_lambda(lambda arg:arg**3,10)) # ** stands for exponential value

####################################################
# using FILTER method in Python
####################################################

# filter(,obj) : Filter method accepts two arguments , one is the lambda or expression  and another is the object on which lambda acts
# Print all the odd numbers of the list - Using Lambdas
list_nums = [10,11,12,13,14]
print(list_nums)

list_odd = filter(lambda arg:arg%2!=0,list_nums)

print(list(list_odd))

list_words = ['Hareesha','Siresha','Sunil','Samnvi',"one"]

# Find list of words that ends with 'sha' at the end

list_res = filter(lambda arg: arg.endswith('sha'),list_words)

print(list(list_res))

print( list( filter( lambda arg: len(arg)==3, list_words))) # Words that has length 3

print( list( filter( lambda arg: arg.startswith('Ha'), list_words))) # Words that starts with string 'Ha'

##############################################################################
# Mapping one element to another is Python - Like map function of Java 8
##############################################################################

# map( , Obj) - map() function accepts two parameters, first one is the function and another one is the list of elements on which funciton needs to be applied.

# In map() function number of elements of the list remains the same
# The type of the elemtns in the resultant map may not be same as the original type of elements in the list, using map

list_ele = ['One','Two','Three']

print( list( map( lambda arg: arg.upper(),list_ele))) # This maps each and every element of the map to corresponsing another element based on the function

print( list( map( lambda arg: len(arg), list_ele))) # This mapped each element to its corresponding lenght of element

##############################################################################
# REDUCE
# reduce( , ) - Reduce function in Python accetps two parameters.First one is the function and second one is the object on which reduce function would act up on
# The function that reduce accepts has 2 parameters and reduces to one
##############################################################################

list_reduce = [10,20,30,40]

print( reduce( lambda x,y: x+y, list_reduce))

# As part of Python3 reduce() function is moved to functools module.
# Find sum of squares of all even numbers from the list

numbers_all = [1,2,3,4,5,6,7,8,9,10] # 4+16+36+64+100

print(reduce(lambda x,y: x+y,map( lambda x: x**2,filter(lambda x: x%2==0, numbers_all))))

# Find sum of days of months

months_list = [('Jan',30),('Dec',31),('Feb',28)] # List of tuples

print(reduce(lambda x,y: x+y, map(lambda arg: arg[1], months_list)))

# Find month with less number of days

print( reduce( lambda x,y: x if x[1]<y[1] else y[1],months_list))


