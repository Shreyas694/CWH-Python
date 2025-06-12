# For loops Python 
for number in range(3):
    print("Attempt",number+1,(number+1)*".")

for number in range(1,4):
    print("Attempt",number,(number)*".")

for number in range(1,10,2):
    print("Attempt",number)

successful = True 
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break    # indicate only 1 attempt 
else:
    print("Attempted 3 times and failed!")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break    # indicate only 1 attempt 
else:
    print("Attempted 3 times and failed!") # Executed only if successful is false 

#Nested Loop 
for x in range(5): # Outer loop 
    for y in range(3): #Inner loop
        print(f"({x},{y})")

print(type(5))
print(type(range(5)))

#Iterable : Reapeating Itself 
for x in "Python": # for string 
    print(x)

for x in [1,2,3,4]: # Iterating over list
    print(x)         

shopping_cart = 1,2,3,4,5
for item in shopping_cart:
    print(item)

# Printing Even numbers only /
count = 0 
for even_numbers in range(1,10):
    if even_numbers % 2 == 0:
        count += 1
        print(even_numbers)
print(f"we have {count} even numbers.")