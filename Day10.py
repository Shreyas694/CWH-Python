# *Args **Kwargs 

nums = [2,5,2,1,2,5]
print(nums)
print(*nums) # here,*nums indicate unpacking the list objects 

def order_pizza(size, *toppings,**details):
    print(f"Ordered a {size} Pizza with following toppings:")
    for topping in toppings:
       print(f"- {topping}")
    print("Details of the order are:")
    for key,value in details.items():
        print(f"- {key}: {value}")

order_pizza("large","pepparoni","olives",delivery = True,Tip=5)

# Sorting a dictionary by a value 
scores : dict[str,int] = {'Bob': 102,
                          'James':42,
                          'Sarah':34,
                          'Tom': 504,
                          'Fred':197}
print(dict(sorted(scores.items(),key = lambda x: x[1],reverse = True )))

# Spliting Any list into equally sized chunks 
from itertools import batched 

data : list[int] = [1,2,3,4,5,6,7,6,4,9,8]
batch : batched = batched(data, n = 3) # n should not be zero 
print(list(batch))

# Removing duplicates from a list 
numbers : list[int] = [1,1,3,3,3,2,
                       2,1,2,3,4,4]
print(list(set(numbers)))

# Removing duplicates using dictionary 
numbers : list[int] = [1,1,3,3,3,2,
                       2,1,2,3,4,4]
print(dict.fromkeys(numbers))  # Dictionary cannot be duplicates 



