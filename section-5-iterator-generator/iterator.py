# iterable
# iterator

numbers = [1,2,3,4,5,6]

###Manuel iteration ###
iterator = iter(numbers)

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break
###Manuel iteration ###

# print(next(iterator))
# s = "IBOS ACADEMY"
# a = 10

# for i in a:
#     print(i)

print(dir(numbers)) # usable methods