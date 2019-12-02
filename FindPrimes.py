def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Memory complexity ~ O(n)
# Computational complexity ~ O(n * log(n))
def find_primes(count):
    tab = [2]
    primes = 2
    number = 3

    j = 1
    while j < count:
        if gcd(primes, number) == 1:
            tab.append(number)
            primes *= number
            j += 1
        number += 2
    return tab


tab = find_primes(100)
print(tab)
print(len(tab))
