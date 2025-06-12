# For loops #17 cwh
name = "Sh"
for i in name:
    print(i)
    if (i == "b"):
        print("this is special")

colors = ["red", "green", "yellow", "blue"]
for color in colors:
    print(color)

for k in range(6):
    print(k+1)
for j in range(1, 9):
    print(j+1)

for u in range(1, 20, 4):
    print(u)

# while loop #18
i = 0
while (i < 3):
    print(i)
    i = i + 1
print("Done with the while loop")

while (i <= 20):
    i = int(input("Enter the number: "))
    print(i)
print("Done with the while loop for now!")

count = 5
while (count > 0):
    print(count)
    count = count - 1
print("Done with the decrementing while loop count ")

count = -5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("Im inside the else")
print("Done with the else print ")

# Do while loop : run irrespective of whether the condition is true or not then the next iteration run only if the condition is true
# Emulation of Do while loop
i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break
