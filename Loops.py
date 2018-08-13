#While loop - Print cubes till given number


def print_cubes(n):
    i=1
    while i**3 <= n :
        i = i*i*i
        print(i)
        i = i + 1


print_cubes(10)


##If else loop in puthon

def read_input_print(text):
    if text in ("Hello"):
        print("Hello how are you today")
    elif text in ("Good Morning"):
        print("Good Morning")
    else :
        print(text)


text = input("Enter your text : ")
read_input_print(text)