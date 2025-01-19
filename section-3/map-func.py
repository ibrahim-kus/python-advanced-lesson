
numbers = [1,2,3,4,5,6]
numbers_str = ["1","2","3"]
names = ["ali","veli"]
users = [
    {"ad":"cenkk", "soyad":"has"},
    {"ad":"verdi", "soyad":"cass"}
]
# kareleri = []
# for number in numbers:
#     kareleri.append(number ** 2)

def kareAl(number):
    return number ** 2



result = map(kareAl,numbers)
print(result) # returned object
result2 = list(map(kareAl,numbers))
print(result2)

sonuc = list(map(lambda sayi: sayi ** 2, numbers))
sonuc = list(map(int, numbers_str))
sonuc = list(map(str.capitalize, names))
sonuc = list(map(lambda kisi: kisi["ad"], users))

print(sonuc)
