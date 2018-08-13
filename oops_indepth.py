# This is a new module and it can contain any number of classes

# In python, an object is empty hash of attribute key/value pairs whic can be added or deleted dynamically.
# [This is not possibe in JAVA]

# In python if we

# This is how in Python a empty class is created

# Class Plant - Empty
class Planet:
    pass


# Creating a object
mars = Planet()  # Isn't this a call to empty constructor ? But we have not defined one in the above class !!
print(mars)
print(mars.__module__) # __main__
print(mars.__class__)  # __main__.Planet
print(mars.population )  # this will throw a run time exception, as there is no population attribute

# Note : This will not give compilation error as Java because Python is not a compiled code.It interprets the code .Where Java
# is both compiled and interpreted

earth = Planet()
earth.population = 'In millions'

print(earth.population)


