# This is a new module - A module can have any number of classes in it.

# Inheritance - is establishing a realtion ship between two related entities.

# Like JAVA , python also supports inheritance.In fact Python also supports multiple inheritance.

# which python - commnad tells where python is installed

# Person class

class Person(object): # Needs to be inherited from root class object for python 2.x
                    # (object) is not needed in python 3.x

    def __init__(self, name):
        self.name = name

    def print_person_details(self):
        print('Name of the persion is :' + str(self.name) + ' and this being printed from super class [ Person ] ')

    def __repr__(self):
        print((self.name))


# Student class - Child
class Student(Person):


    def __init__(self, name, college_name):
        super(Student, self).__init__(name) # this the way how super is called in 2.x , In 3.x super(<Classname>,self) is equal to super()
     #  super().__init__(name) # 3.x style
        self.college_name = college_name

    def print_student_details(self):
        print('Name of the student is :' + str(self.name) + ' and this is being printed from child class [ Student ] ')

    # def print_super_class_details(self):
    #     print('Name from Person class : '+super().__reduce__()))

    def __repr__(self):
        print((self.name, self.college_name))


# Instantiating

person = Person('Hareesha')
person.print_person_details()

student = Student('Hareesha', 'JNTU')

student.print_student_details()
