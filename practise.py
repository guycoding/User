def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(5))


def square(x):
    if x == 0:
        return 0
    else:
       return square(x - 1) +( 2 * x - 1)


print(square(2))

for n in range(7+1) :
    star = ""
    for e in range(n+1):
        star = star +'*'
    print(star)
    if n ==7:
        break
def multiplier(func):
    return lambda k: k * func

x = multiplier(5)
print(x(2))
def root(r):
    if r<=0:
        return "root must be greater than 1"
    return lambda y: float(y ** (1/r))

root_type = root(2)
print(root_type(0.6))

