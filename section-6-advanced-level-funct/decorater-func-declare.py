def selamlama(fn):
    def inner(ad):
        print("hoş geldiniz")
        fn(ad)
        print("görüşmek üzere")
    return inner

@selamlama
def gunaydin(ad):
    print(f"günaydin benim adim {ad}")

@selamlama
def iyigunler(ad):
    print(f"iyi günler benim adim {ad}")

# g = selamlama(gunaydin)
# i = selamlama(iyigunler)

# g()
# i()
    
gunaydin("Ali")
iyigunler("ibrahim")