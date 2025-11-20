import math

def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))

gen = (x for x in range(2, 50) if is_prime(x))

for p in gen:
    print(p, end=' ')
