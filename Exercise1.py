#import string module
import string
# Creating a method in python
def print_a_text():
    print("Hello")


# Calling a method
print_a_text()


# Mehtod accepting parameters
def sum_of_numbers(n1, n2):
    sum = n1 + n2
    return sum

# Calling a method, with parameters
value=sum_of_numbers(10,20)
print(value)

#defining a loop
def multiplication_numbers(n):
    for i in range(0,n):
        print('Hello : '+ str(i))

print(multiplication_numbers(5))

#string module attributes
def string_functions(word):
    print('Word is of ascii characters : '+str(word in string.ascii_letters))
    print('Word is of non acii_characters : '+ str(word not in string.ascii_letters))
    print('Word is of non acii_characters : '+ str(word in string.digits))
    print('Word is of non acii_characters : '+ str(word not in string.digits))
    print('Given word is')
    for i in word:
        print(i)


string_functions('Hareesha')

