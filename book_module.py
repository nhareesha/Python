# This is module.A module in python is any python file.A module can have any number of classes

# Name of the module needs to be high level.Name of the module dosen't need to match with any of the class defined in the module
# __init__(self) is the constructor in python. This is same in every class. Any it is also a special method in python.

# Instance variables needs to be defined in side the constructor in any of the python class
# Any of the variable defined out side of the constuctor are defined as the class level varaibles in the python.

# All the instance methods, cosntructors and instance variables needed to be reference by self [ like this in java and it is implicit ]
# but not implicit in python

# In python there is no concept of over loading of constructors .If we define two constuctors with different arguments, then the
# latest will override the earlier defined cosntructor and acts as if the earlier defined construtor never existed.[Dynamic typing]

# In python there is no concept of overloading of instance methods.[Dynamic typing ]


# Book class

class Book:

    # This is the constructor in Python with one argument
    # We can also assign a default value to the parameter
    def __init__(self, book_name='This is the Default Name'): # Here default value to a variable is used
        self.book_name = book_name
        self.copies = 0

    # This is technical representation of toString() method in python
    def __repr__(self):
        return repr((self.book_name,
                     self.copies))  # repr class construtor accepts only one param, if there are more than one param
                                    # we need to define a tuple (,)

    # @property
    # def __str__(self):
    #     return repr(self.book_name)

    # This is instance method in python
    def increase_no_copies(self, number):
        self.copies = self.copies + number
        print('Total number of copies : ' + str(self.copies))

    def decrese_no_copies(self, number):
        if number <= self.copies:
            self.copies -= number  # compund operators are supported in python same as Java
            print('Total nmber of copies after decrement:' + str(self.copies))
        else:
            print('Total nmber of copies avaliable are only :' + str(self.copies))


# Instantiating Book class - creating a object

b1 = Book('Python - For Hareesha')  # Here self is implicilty passed
b2 = Book()  # Not to pass a argument is valid in here as we have assigned a default value to name parameter in the constructor

# Calling a instance methods using object b1

b1.increase_no_copies(10)  # Here self is implicitly passed
b1.decrese_no_copies(2)
b1.decrese_no_copies(8)
b1.increase_no_copies(80)
b1.decrese_no_copies(81)

print(b1) # printing of object, now prints the attribute values ,as we have defined __repr__ is used.
print(b2)
