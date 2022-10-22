primes = []

def is_prime(integer):
    for divisor in range(2,integer-1):
        if integer%divisor == 0:
            return False
    return True

for i in range(2,101):
    # find if prime
    # if prime print, otherwise ignore
    for x in range(2, i):
        if is_prime(i) and i not in primes:
            primes.append(i)

for prime in primes:
    print(prime)
  