# 15
import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = int(time.strftime("%H"))
print(timestamp)

# Match case statements #16 cwh
x = int(input("Enter the value of x : "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x != 90:
        print(x, "is not 90")

    case _:
        print(x)
