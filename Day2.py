#Day-2 Python: Data Types,Numbers,Operations,Type convergence and f-string,Tip calculator  

# Basic Data Types 

print("Hellow"[5]) # printing indexing letter
print("3.142") # Floating point
print(True) # Boolean
print(False)

# Type Checking and type conversion 
num_char = len( input("What is your name? "))
print(num_char)
t= type(num_char) # type is integer
print(t)
new_num_char = str(num_char) # Converting 'int' to 'string' 
print("Your name has " + new_num_char + " character") 

a = float(123)
print(a)

print(70 + float("100.5")) # Adding the two floating point numbers 
print(str(40) + str(55)) # Concatinating the two int objects by converting to the strings objects 

two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))

first_digit =  two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)
print(7/3) # giving rise to float result number
print(2 ** 4) # give rise to exponent

# Methematical operation follows "PEMDAS" rule 
# P(),E**,M*,D/,A+,S-
print(4**5*3*4+5/7-6) #Follows the "PEMDAS" rule

#Body Mass Index(BMI) calculation 
#BMI = Weight(kg)/height^2(m^2)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
i = str(bmi_as_int)
a = "Your BMI is " + i  #Concatination of two string objects 
print(a)

#Number manipulation and f string 
print(round(8/3,2)) #rounding a number to the two decimal places 
print(type(3/3)) #class is float not the int 
print(type(3//2)) # class is int 
score = 0
score -= 1

#fstring: converts directly int into the string 
score = 0 
height = 1.5
iswinning = True
print(f"Your score is {score},your height is {height},you are winning is {iswinning}")

f_name = "Shreyas" 
l_name = "Chillal"
print(f"My name is {f_name.upper()} {l_name.upper()}.") # Capitallizing the name inside f string 

person = {'name':'Shreyas','age':13}
print(f"My name is  {person['name']} and I am {person['age']} years old ")

pi = 3.14159265
print(f"pi is equal to {pi:.4f}") # Rounding of to the 4 decimal places 

print(f"4 times 11 is equal to the {4*11}") #  calculates the value

for n in range(1,11):
    print(f"The value of the {n:02}") # Zero padding to the two digits 

from datetime import datetime
birthday = datetime(2001,12,3) #year,month,day
print(f"My birthday is on {birthday:%B %d,%Y}") # Says the birthday in order of month,day and year 

# f-strings Tricks 
n: int = 1000000000
print(f'{n:_}')
print(f'{n:,}')

var : str = 'var'
print(f"{var:_>20}:") #var placed after the 20 space with underscore(_)
print(f"{var:#<20}:") #var placed before the 20 spaces with the hash(#)
print(f"{var:|^20}:") #var placed at the centre with the pipeline(|)

from datetime import datetime
now: datetime = datetime.now()
print(f"{now:%d.%m.%y (%H:%M:%S)}")
print(f"{now:%c}") # Local version of date and time 
print(f"{now:%I %p}") # first 12 hr format followed by AM and PM 

n: float  = 288.8977
print(round(n,2)) 
print(f"Result:{n:.2f}")  # round off to 2 decimal places 
print(f"Result:{n:.0f}")  # round off to the exact integer 
print(f"Result:{n:_.3f}") # round off to the 3 decimal places 

a: int = 5 
b: int = 10
my_var: str = "Bob says Hi"

print(f"{a + b = }") 
print(f"{my_var = }") # Writes my_var without writing my_var manually 


# Calculating weeks,days,months left for me if i lived for 90 yrs.
age = input("What is your current age in year?: ")
age_as_int = int(age)
year_remaining = 90 - age_as_int 
months_remaining = (90 - age_as_int)*12
weeks_remaining = (90 - age_as_int)*52
days_remaining = (90 - age_as_int)*365

print(f"You have left only {days_remaining} days,{weeks_remaining} weeks and {months_remaining} months!.")

#Project-2: Creating Tip Calculator 

bill = float(input("What was the total bill? $"))
tip = int(input("How much percent tip would you(customer)like to give? 10,12 or 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person) #fomatting two decimal places converts float into a string
print(f"Each person should pay:${final_amount}")

