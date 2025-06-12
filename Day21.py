import time
i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break

# Tuples 24 CWH
# Tuples cant be single element python get confuse,so apply comma after the element
# tuples can't be further changed once assigned,like we can't add,remove the original elments by creating another tuple
tup = (1, 4, 6, 8)
print(tup[0])

tup_1 = (1, 2, 4, 7, 665, 4, 43, "heytap", False)
print(len(tup_1))
print(tup_1[-1])  # prints the 8th index

# tuples can be sliced similar to the list
tup_2 = tup_1[1:5]  # prints upto the 4th index only if 5(5-1 = 4)
print(tup_2)

print(tup_1[:5])

# Tuples methods 25 cwh
# tuples can be changed by converting it into a list and then make changes to that list again covert the changed list back to the tuple.
countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# Tuples can be concatinated
countries = ("Pakistan", "Afghanistan", "Bangladesh", "Shrilanka")
countries_2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries_2
print(southEastAsia)

tuple_1 = (0, 35, 6, 3, 2, 7, 3, 2, 12, 6, 9)
res = tuple_1.count(3)
res = tuple_1.index(3, 4, 8)  # counting the index of the 3 in between 4:8
print("Count of 3 in tuple_1 is:", res)

t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("Enter current hour: "))
print(hour)

if (hour > 00 and hour < 12):
    print("Good morning")
elif (hour >= 12 and hour < 16):
    print("Good afternoon")
elif (hour >= 16 and hour < 21):
    print("Good Evening")
else:
    print("Good Night")

# f string 28: String formatting cwh
letter = "Hey my name is {} and im from {}"
country = "India"
name = "Shreyas"

print(letter.format(name, country))

price = 45.9048
txt = f"for only {price: .2f} dollars"
print(txt)

# Doc String 29 cwh
# like the comments doc string cannot be ignored
# doc string written right above the function body or just below the function name


def square(n):
    ''' Take in a number n return the square of n '''  # doc string
    print(n**2)


square(5)
print(square.__doc__)  # for printing the doc string

# PEP 8 (Python Enhancement Proposal) to make python programme readable and mentanable

# Recursion : Function inside the function


def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        # calling the function with different argument
        return n * factorial(n-1)


print(f"The value of 6! is : {factorial(6)}")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))


