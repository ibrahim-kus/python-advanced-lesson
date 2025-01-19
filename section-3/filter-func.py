numbers = [1,3,5,-4,-3]

def negatifSayilar(x):
    if x < 0:
        return True
    else:
        return False

sonuc = list(filter(lambda x: x < 0, numbers))
sonuc = list(filter(lambda x: x % 2 == 1, numbers))

isimler = ["çınar","ali","ada","yiğit","sena"]
filteredResult = list(filter(lambda x: x[0] == 'a', isimler))
sonuc = list(map(lambda x: x.upper(), filteredResult))

users = [
    {"username":"ibrahim", "posts": ["post 1","post 2"]},
    {"username":"hasan", "posts": []},
    {"username":"yigitbilgi", "posts": ["post 1","post 2","post 3"]},
]

filteredUsers = list(filter(lambda u: len(u["posts"])>0, users))
sonuc = list(map(lambda u: u["username"], filteredUsers))

sonuc = [user["username"].upper() for user in users if len(user["posts"]) > 0]

print(sonuc)