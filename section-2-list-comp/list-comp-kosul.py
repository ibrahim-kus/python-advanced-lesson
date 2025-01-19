
# for item in liste:
#     if (kosul):
#         expresssion

#ls
# [ expression for item in liste if kosul ]

numbers = [3,4,5,7,8,9,46]
result = []

for number in numbers:
    if(number%2 == 0):
        result.append(number)
print(result)
#ls
result = []
result = [number for number in numbers if number % 2 == 0]
result = [number if number % 2 == 0 else "odd" for number in numbers] 
print(result)