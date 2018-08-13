# Any py file in python is called a module.

# Any class level variable created outside of the method is called static variable.Like JAVA  this doesn't require any
# key word like "static"

# static variables can be accessed with the class name or instance name [ same as JAVA ]

# Note : Never set a variable using a instance variable in python. Because this effect stays only till that instance.
# static variables needs to be always referred using the class name . Like in JAVA they cannot be referred just by name
# even in side the class

# For all the instance methods, self is required.For defining a static method, @staticmethod annoataion is required and for such methos
# there is no need of self


class Test:
    count = 0

    def __init__(self):
        Test.count += 1

    def print_count(self):
        print(Test.count)  # Accessing static variable using the class name Test

    @staticmethod
    def static_method():
        return Test.count


test1 = Test()
test2 = Test()

test2.print_count()  ## Accessing a instance method .In python an instance method can also refer a static variable.
## Like in JAVA there is no restrict saying - staic can only be accessed in static methods

print(Test.count)  ## This is the way to access the static variable using class name

test1.count = 100  ## This is okay.But this only overrides the static variable of same name in Test class.This effect only
## lasts untill this instance.

print(test1.count)  ## this prints the 100 . This overrides the class level  variable
