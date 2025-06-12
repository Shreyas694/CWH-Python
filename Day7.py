nums = range(1,1000)

def is_prime(num):
    for x in range(2,num):
        if(num%x) == 0:
            return False
    return True 
prime = list(filter(is_prime,nums))
print(prime)