# Lists in python can acts both STACK and QUEUE

# STACK - Last In First Out - LIFO

# QUEUE - First In First Out - FIFO

# List has some great variety of methods that can be used to achieve this functionality

# LIST AS STACK - LIFO

numbers = []  # this is a empty List

print(numbers)

# List has a method called append() . This can be used to append elements to the end of the stack
# List has a method called pop() . This can be used to remove elements from the end of the stack

numbers.append(1) # this add the elements to the end of the list .
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5) # This is the last inserted element and with pop() this is the first element that is removed from the stack

print(numbers)

numbers.pop()# If there is no index specifed to the pop() method it takes out the last element in the list. 5
numbers.pop()# If there is no index specifed to the pop() method it takes out the last element in the list. 4
numbers.pop()# If there is no index specifed to the pop() method it takes out the last element in the list. 3

print(numbers)


# List has a method called append() . This can be used to append elements to the end of the list
# List has a method called pop(0) . This can be used to remove elements from the  of the begigning of the list.This is index based removal of the element from the list

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)

print(queue)

queue.pop(0) # This pops the element from the start of the queue. Here 0 is the index of the element that needs to be removed - 1
queue.pop(0) #  2
queue.pop(0) # 3
queue.pop(0) # 4
print(queue)

