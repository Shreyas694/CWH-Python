#Day-3 : Conditional Statements,Logical Operators.Code blocks and Scope,global and local name,Tresure hunt game 

#Conditional Statements: if/else
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120: #Greater than equal to 
    print("You can ride the rollercoaster! ") #Indented block of code 
else:
    print("Sorry,you have to grow taller before you can ride.")
# == Equal to, != not equal to 

# Odd or Even Introducing Modulo(remainder of the division) 

number = int(input("Which number do you want to choose? "))

if number % 2 == 0: # The remainder is zero 
    print("This is a even number.")
else:
    print("This is an odd number.")

# Nested if/else statement 

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else :
        print("Please pay $12.")

# Nested if/elif/else statements 

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age >= 11-18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry,you have to grow taller.")

# BMI calculator:

# BMI = weight(kg)/height(m^2)

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
bmi = weight/height**2
round(bmi)
print(f"your bmi is {bmi}")

bmi = int(input("Enter your bmi here.")) 
if bmi <18.5:
    print("You are Underweight.")
elif bmi >=18.5 and bmi <= 25:
    print("You are Normal Weight.")
elif bmi >=25 and bmi <=30:
     print("You are Overweight.")
elif bmi >=30 and bmi <=35:
     print("you are Obese.")
else:
    print("You are clinically obese.")
    
# Leap year calculation 
# If the year evenly divisible by 4 its leap year probably,Next check,immidietly
# If the year not divisible by 100 after evenly divisible by 4 its a leap year 
# if the year is evenly divisible by 100 after it is evenly divisible by 4,it must also be evenly divisible by 400 then only the given year is the leap year.

year = int(input("Enter the year that you want to check? "))
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("The given year is a leap year.")
        else:
            print("The given year is not a leap year.")
    else:
        print("The given year is a leap year.")
else:
    print("The given year is not a leap year at all.")

# Multiple if condition 

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm "))
bill = 0 
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    ask = input("Do you want photos? Y or N. ")
    if ask == "Y":
        bill +=3 
    print("Your final bill is {bill}.")
else:
    print("Sorry,you have to grow taller.")

# Ordering Pizza 

print("Welcome to the Pizza Deliveries!")
size = input("What size of Pizza do you want to order? S,M,L")
bill = 0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
add_pepparoni = input("Do you want Pepparoni? y or n ")
if add_pepparoni == "y":
    if size == "S":
        bill +=2
    else:
        bill +=3
extra_cheese = input("Do want extra chesse? y or n ")
if extra_cheese == "y":
        bill +=1
print(f"Your final bill is ${bill}.")

# Logical Operators: and , or,not
# and if both are true
# or-if any one is true
# not-inverse 

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm "))
bill = 0 
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <=55:
        print("No worries have a free ride!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    ask = input("Do you want photos? y or n. ")
    if ask == "y":
        bill +=3 
    print("Your final bill is {bill}.")
else:
    print("Sorry,you have to grow taller.")

# True Love- Score calculation 
print("Welcome to the love score calculation!")
name_1 = input("What is your name?\n")
name_2 = input("What is their name?\n")

combined_string = name_1 + name_2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
 
true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score<10 or love_score>90 :
    print("Your love score is{love_score},you grow together!")
elif love_score >=40 and love_score <=50:
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"Your score is {love_score}.")