# Functions in python 20 CWH
# function used to reuse a block of code.It prevents writing the logic repetatively.Unlike we do in the normal code
def Calc_Gmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


def is_Greater(a, b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")


def is_Lesser(a, b):
    pass


a = 6
b = 7
Calc_Gmean(a, b)
is_Greater(a, b)
is_Lesser(a, b)

c = 8
d = 9
Calc_Gmean(c, d)
is_Greater(c, d)

# Function Arguments-Python 21 cwh

# Positional Argument : The arguments are matched to the parameter in the function definition based on their positional order.


def average(a, b):  # Positional/required argument
    print("The average is ", (a+b)/2)


average(6, 8)  # positional/required argument


def ave(c=4, d=7):  # Default argument (preffered after the positional argument)
    print("The average is ", (c+d)/2)


def name(fname, mname="Jhonson", lname="Whatson"):
    print("Hellow,", fname, mname, lname)


name("Amy", "Agarwal")

# Keyword arguments : We can explicitly name the parameter when calling the function,this allows us to pass the argument in any order as long as we use the parameter names.


def greet(name, message):
    print(f"Hellow,{name}! {message}")


greet(message="Good morning!", name="Shreyas")  # Order does not matter here


# Variable length arguments(*args): Used when we dont know in advance how many positional arguments a function will receive.*args syntax will allows a function to accept an arbitary number of positional arguments.These arguments usually collected into a tuple inside a function.
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is : ", sum / len(numbers))


average(2, 3, 4, 5, 7)


def name(**name):
    print(type(name))
    print("Hellow ,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")

# Lists in Python 22 cwh

marks = [3, 5, 6, "Harry", True]
print(marks)
print(type(marks))
print(len(marks))

print(marks[-3])  # 5-3 =2 [6]
print(marks[len(marks)-3])  # similar as above

if 7 in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry":
    print("Yea")

print(marks[1:-1])  # same as [1:(5-1) = 4]
print(marks[1:4:2])  # start from 1st index upto 4th

# index jump 1 extra index after the 1st index

# List Comprehension
lst = [i*i for i in range(4)]  #
print(lst)

lst_1 = [i*i for i in range(10) if i % 2 == 0]
print(lst_1)

# List Methods 23 cwh
l = [3, 2, 5, 4, 6, 9]
l.append(7)
l.sort(reverse=True)  # sort out in reverse (decending) order
print(l)

m = 1  # m is just a reference here,the content of the l same except it starting from 0
m[0] = 0
print(l)

m = l.copy()
m[0] = 0
print(l)

l.insert(1, 455)

m = [858, 33, 475, 7]
l.extend(m)
print(l)

k = l + m
print(k)  # lists can be concatinated

