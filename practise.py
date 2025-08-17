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

for n in range(7) :
    star = ""
    for e in range(n+1):
        star = star +'*'
    print(star)
def multiplier(func):
    return lambda k: k * func

x = multiplier(5)
print(x(2))
def root(r):
    if r<=0:
        return "root must be greater than 1"
    return lambda y: float(y ** (1/r))

root_type = root(2)
print(root_type(4))
#when n =0,start = 1,n=1 star = 2
def percentage_converter(value):
    return value/100

def percent(func,a):
    c= func(a)
    return c * 100

print(percent(percentage_converter,100))




