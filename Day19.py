# Break and continue 19 cwh
for i in range(12):
    if (i == 10):
        break
    print("5 X", i+1, "=", 5 * (i+1))
print("get out of the loop")

for i in range(12):
    if (i == 10):
        print("Skip the iteration mentioned and execute the next.")
        continue
    print("5 X", i, "=", 5*(i))


student_heights = input("Input the List of student heights below\n")
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
