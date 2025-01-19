def filter(fn, liste):
    result = []
    for item in liste:
        if fn(item): #function
            result.append(item)
    return result


def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0 

numbers = [1,2,3,-3,-5,6]

result = filter(is_even,numbers)
result2 = filter(is_positive,numbers)


print(result)
print(result2)


