# The prime factors of 13,195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600,851,475,143

# Option 1 - Calculate Primes first and see if they're factors of n:
    # Calculate all the prime numbers starting with 29, iterating +2 for each one, until you reach (600,851,475,143 + 1) / 2 and see if it's a factor of 600,851,475,143
# Option 2 - Calculate factors first (decrementing) and check if they're prime:
    # Iterate backwards 
# Option 3 - OK THIS MIGHT BE THE BEST:
    # Future-Proofing
        # If n % 2 == 0: Iterate by +1
        # If n% 2 != 0: Iterate by +2
    # Start with 2 or 3 depending on the above. If n % i == 0, see if the OTHER factor is prime

# for even numbers, divide n by 2 until it's odd, that's your new i

def main():
    print(option_3(29))

# def option_2(n):
#     increment = None
#     i = n
#     if n % 2 == 0:
#         increment = 1
#     else:
#         increment = 2
#     i = 

def option_3(n):
    increment = None
    i = None
    if n % 2 == 0:
        increment = 1
        i = 2
    else:
        increment = 2
        i = 3
    while i < (n / 2):
        if n % i == 0:
            if is_prime(n / i):
                return (n / i)
            else:
                i += increment


def is_prime(n):
    i = 2
    for i in range(i, n):
        if n % i == 0:
            return False
        else:
            i += 1
    return True

if __name__ == "__main__":
    main()