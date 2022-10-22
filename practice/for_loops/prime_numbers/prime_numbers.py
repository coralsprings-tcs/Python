primes = []

def is_prime(integer) -> bool:
    for divisor in range(2, integer-1):
        if not integer % divisor: # same as saying "if integer%divisor == 0"
            return False
    return True

for i in range(1, 101):
    if i == 1:
        continue # skips i = 1 and moves to next i value
    if is_prime(i) and i not in primes:
        primes.append(i)

for prime in primes:
    print(prime)
   
