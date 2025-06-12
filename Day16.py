nm = "harry"
print(nm[-4:-2])

# strings are immutable
a = "!!!!Harry!!!! !! Harry"
print(len(a))
# strip hides the only trailing characters not the leading characters
print(a.rstrip("!"))

print(a.replace("Harry", "John"))
print(a.split(" "))

b = "scalar scholl of technology"
print(b.capitalize())

str1 = "Welcome to python"
print(len(str1))
print(str1.center(34))  # add the 17 spaces to the first
print(a.count("Harry"))
str1 = "He's name is Dan.He is an honest man."
print(str1.find("ishh"))  # returns the -1

str2 = "WelcomeTOTheConsole23"
print(str2.isalnum())
print(str2.isalpha())

str3 = "We wish you a Marry Christmas\n"
print(str3)
print(str3.isprintable())

str4 = "   "
print(str4.isspace())

str5 = "World Health Organization"
print(str5.istitle())

str6 = "To Kill A Mocking Bird"
print(str6.istitle())

str7 = "Python is an Interpreted Language"
print(str7.swapcase())  # Make lower case to upper case and vice versa

str8 = "his name is dan and he is honest man ever."
print(str8.title())

# if else CWH
num = 18
if (num < 0):
    print("Number is negative")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    else:
        print("Number is > 10")
else:
    print("Number is zero")
