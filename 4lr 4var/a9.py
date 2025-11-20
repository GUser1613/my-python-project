from functools import reduce

square = lambda x: x ** 2
cube = lambda x: x ** 3
double = lambda x: x * 2

def compose(*steps):
    return lambda x: reduce(
        lambda acc, f: f(acc),  
        steps,                  
        x                      
    )

pipeline = compose(square, cube, double)

result = pipeline(3)

print(result)  


