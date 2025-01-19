liste = [1,2,3]

print(len(liste)) # hata çünkü list sınıfında len methodu yok.

# sayi = 10
# print(len(sayi))

s = "Merhaba BTK Akademi"

print(len(s))

class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title}, {self.director} tarafindan {self.year} yilinda yayinlandi."
    
    def __len__(self):
        return self.duration    
    
    def __del__(self):
        print("film silindi")   

m = Movie("Simpsons", "benn", "1997", 120)

print(m.__repr__()) # representation
print(len(m))

del m