#class
class CartItem:
    #constructor
    def __init__(self,name,price,quantity):
        #instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity
#instance
item1 = CartItem("Iphone15",50000,1)
item2 = CartItem("Xiaomi",30000,1)

