from functools import reduce
from operator import mul
factorial = lambda n: reduce(mul, range(1, n + 1), 0)
print(factorial(0))


