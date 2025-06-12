inv = [None,None,None] #string is Truthy value None is falsy value

if all(inv):
    print("Inventory full")
elif any(inv):
    print("Inventory has items!")
else:
    print('Inventory is empty!')

# Tuples are hashable 
coords = set()
a = (1,2)
b = (2,2)
coords.add(a)
coords.add(a)
coords.add(b)
coords.add(b)
print(coords)

#Memory sharing 
a = (1,2)
b = (1,2)
print(id(a))
print(id(b))

#No memory sharing in list 
c = [1,2]
d = [1,2]
print(id(c))
print(id(d))

# Packing and Unpacking 
#Unpacking 
a,b,c = (1,2,3) 
print(a)
print(b)
print(c)

#Packing 
nums = a,b,c 
print(nums)