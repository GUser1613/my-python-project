square = lambda x: x ** 2
cube = lambda x: x ** 3
double = lambda x: x * 2

funcs = [square, cube, double]
nums = range(1, 6)

result = [list(map(f, nums)) for f in funcs]
print(result)

