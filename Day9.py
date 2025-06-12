# Scope  in Python : Local and Global Scope 

x = 1 # Global veriable scope 
def foo():
    global x 
    x = 11 # Local scope 
    y = 12 # Local scope  
    print(f"foo sees x equal to {x}.")
    print(f"foo sees y equal to {y}.") 
foo()
print(f"global sees x equal to {x}.") # Output 11,12,11 since,global scope value has been changed to 11 after assigning global x value inside the foo() function 

x = 1 
def outer():
    x = 2 
    def inner():
        x = 3 
        print(f"inner sees x equal to {x}")
        return 
    inner()
    print(f"outer sees x equal to {x}.")
    return 
outer()
print(f"Global sees x equal to the {x}.") # Output 3,2,1

x = 1 
def outer():
    x = 2 
    def inner():
        print(f"inner sees x equal to {x}")
        return 
    inner()
    print(f"outer sees x equal to {x}.")
    return 
outer()
print(f"Global sees x equal to the {x}.") # Output 2,2,1

x = 1 
def outer():
    def inner():
        print(f"Inner sees x equal to {x}")
        return 
    inner()
    print(f"Outer sees x equal to {x}.")
    return 
outer()
print(f"Global sees x equal to the {x}.") # Output 1,1,1

x = 1 
def outer():
    x = 2 
    def inner():
        global x 
        x = 3 
        print(f"inner sees x equal to {x}")
        return 
    inner()
    print(f"outer sees x equal to {x}.")
    return 
outer()
print(f"Global sees x equal to the {x}.") # Output 3,2,3

x = 1 
def outer():
    x = 2 
    def inner():
        nonlocal x   # Referencing python one scope out,that is to the outer function as 3.Similar to that of inner function 
        x = 3 
        print(f"inner sees x equal to {x}")
        return 
    inner()
    print(f"outer sees x equal to {x}.")
    return 
outer()
print(f"Global sees x equal to the {x}.") # Global function remain 1 only