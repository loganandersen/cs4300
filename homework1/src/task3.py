# important function
def get_sign(num) :
    """This gives -1 if the thing is negative, +1 if it's positive, 
    or 0 if it's zero."""
    if num > 0 :
        return 1
    elif num < 0 :
        return -1
    elif num == 0:
        return 0

# helper function
def prime_numbers(n) :
    """This gets the first n prime numbers"""
    primes = []
    def isprime(num) :\
        # if value is divisible
        for p in primes :
            if num % p == 0 :
                return False
        return num > 1 ## remove 1 and zero from prime list
    i = 1
    while len(primes) < n :
        if isprime(i) :
            primes.append(i)
        i += 1
    return primes

def print_10_primes() :
    "this prints the first 10 prime numbers"
    for i in prime_numbers(10) :
        print(i)
    
    
def sum_first_100_numbers() :
    "This takes numbers 1 through 100 and sums them together"
    i = 1
    count = 0
    while (i <= 100) :
        count += i
        i += 1
    return count



