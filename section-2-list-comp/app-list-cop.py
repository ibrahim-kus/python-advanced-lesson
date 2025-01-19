# 4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.

ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80] 
# => "{'ahmet': 60, 'canan': 80}"

# [("ali", 50), ("ahmet", 60), ("canan", 80)]
liste = [(ogrenciler[i], notlar[i]) for i in range(0, len(ogrenciler))]
liste_dict = { key:value for (key, value) in liste if value > 50}

# 5- For döngüsüyle yazılan uygulamayı list comprehension ile yazınız.
 
sonuc = [] 
# 0 - 0
# 0 - 1
# 0 - 2
# 1 - 0
# 1 - 1
# 1 - 2

for x in range(3):
    for y in range(3):
        for z in range(3):
            sonuc.append((x,y,z))

sonuc = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]