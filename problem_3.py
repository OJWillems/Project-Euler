import math

# The prime factors of 13,195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600,851,475,143

def main():
    print(find_factors(13195))
    print(find_factors(600851475143))

def find_factors(n):
    upper_bound = n
    i = None
    iterator = None
    prime_factor = None

    # Set starting point and iterator depending on if n is even or odd
    if n % 2 == 0:
        i = 2
        iterator = 1
    else:
        i = 3
        iterator = 2

    while i < upper_bound:
        # print(f"i = {i}")
        if n % i == 0:
            if is_prime(i):
                prime_factor = i
                print(f"new prime_factor = {prime_factor}")
            i += iterator
            upper_bound = int(n/i)
        else:
            upper_bound = math.ceil(n/i)
            i += iterator
            # print(f"i = {i}, upper_bound = {upper_bound}")
    return prime_factor

# Measure-Command: 56 milliseconds
def is_prime(n):
    i = 3
    for i in range(i, n):
        if n % 2 == 0:
            return False
        elif n % i == 0:
            return False
        else:
            i += 2
    return True

# Measure-Command: 36 milliseconds
# THIS HAS FUCKED UP SOMEWHERE
# def is_prime(n):
#     i = 3
#     number = n
#     while i < n:
#         if number % 2 == 0:
#             return False
#         elif number % i == 0:
#             return False
#         else:
#             i += 2
#             n = math.ceil(n/i)
#     return True

if __name__ == "__main__":
    main()