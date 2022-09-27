"""List of prime numbers generator."""

def primes(number_of_primes):
    list = []

    if number_of_primes < 2:
        return list

    prime = [True for _ in range(number_of_primes + 1)]

    for i in range(2, number_of_primes + 1):
        if prime[i]:
            list.append(i)
            for j in range(i*i, number_of_primes, i):
                prime[j] = False

    return list