# In python every py file is Module. A module can have any number of classes.

# In order to define a abstract class it needs to extend a base class called ABC[Abstract Base Class] and annotate
# abstract method with @abstractmethod.These are from module abc.

# Using a abstract class and creating implementations is called - Template design patterns

# In python there is no concept of interface like in Java .We can achieve the behaviour of interface

from abc import ABC,abstractmethod


class AbstractClassExample(ABC):

    def non_abstract_method(self):
        print("This is non abstract method - AbstractClass")
        self.abstract_method_first()

    #With the below annotation, the method is marked as Abstract method
    @abstractmethod
    def abstract_method_first(self):
        pass

    # This is still not an abastract method without annotation
    def abstract_method_second(self):
        pass


#Concrete class that extends AbstractClass
class ConcreteClass(AbstractClassExample):

    # this method provides the impl for abstract method
    def abstract_method_first(self):
        print("This is implementation for abstract_method_first - Concrete class")




#Creating an instance

inst = ConcreteClass()
inst.non_abstract_method()

## Polymorphims and Duck typing

# Same code behaves differently based on input is polymorphism

# Duck typing : Totally un related classes behaves as if they are related.

# In JAVA two class are related if they implement same interface or extend from same super class.

#Example :Here Test1 and Test2 are both unrelated even then their instances are assigned to tests variable.


class Test1 :


    def method(self):
        print("From one")

class Test2:


    def method(self):
        print("From two")


tests = [Test1(),Test2()]

for test in tests:
    test.method()


#Polymorphism : Two classes extends from same parent class or implement same interface.This behviour is called Polymorphism
# Here these two classes are related as they have extended Test classes

class Test :

    def methodTest(self):
        print("Method Test")

class Test1(Test):

    def methodTest1(self):
        print("Method Test1")

class Test2(Test):

    def methodTest2(self):
        print("Mehtod Test2")


tsts = [Test1(),Test2()]

for tst in tsts:
    tst.methodTest()


