from functools import reduce
from operator import mul

def compose(f, g):
    return lambda x: f(g(x))

def compose_many(*funcs):
    return reduce(compose, funcs)

def make_pipeline(func):
    return lambda data: (func(x) for x in data)

factorial = lambda n: reduce(mul, range(1, n+1), 1)
funcex  = lambda x: x + 1
funcex2 = lambda x: x + 2

pipeline_func = compose_many(funcex, funcex2, factorial)

pipeline = make_pipeline(pipeline_func)

nums = range(1, 6)
result = pipeline(nums)

for value in result:
    print(value)