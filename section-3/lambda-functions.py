
#lambda arguments: expression

def kareAl(a):
    return a ** 2

lambda a: a ** 2
result = (lambda a: a**2)(3)
print(result)

###
def myFunc(n):
    return lambda a: a * n

multiply = myFunc(5)
result2 = multiply(3)
print(result2)
###
