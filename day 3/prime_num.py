import math  

def is_prime(n):
    """Check karega ke number prime hai ya nahi."""
    if n < 2:
        return False  
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False  
    return True  

num = int(input("Enter a number: "))

if is_prime(num):
    print("Yes, it's a prime number!")
else:
    print("No, it's not a prime number!")
