# Python Day-5:Loops in Python 
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# Avg len of student heights 
student_heights = input("Input a list of student heights below\n").split()
for n in range (0,len(student_heights)):
   student_heights[n] = int(student_heights[n])
print(student_heights)
print(len(student_heights))

# Avg height without using the for loop 
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)

# Exercise: Average height of students 
student_heights = input("Input a list of students height here\n").split()
for n in range (0,len(student_heights)):
   student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height 
print(total_height)

number_of_students = 0 
for students in student_heights :
    number_of_students += 1
print(number_of_students)
average_height = round(total_height / number_of_students)
print(average_height)


# Exercise: Highest score in the class 
student_scores = input("Input a list of student score\n").split()
for n in range(0 ,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0 
for score in student_scores:
    if score > highest_score:
        highest_score = score 
print(f"The highest score in the class is:{highest_score}")