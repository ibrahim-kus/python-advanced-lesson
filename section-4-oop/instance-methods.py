#class
class CartItem:
    #constructor
    def __init__(self,name,price,quantity): #self oluşturulacak olan instance ı ifade eder.
        #instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity
    
    #instance methods
    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self,rate):
        self.price = self.price * rate

#instance
item1 = CartItem("Iphone15",50000,2)
item2 = CartItem("Xiaomi",30000,3)

print(item1.calculate_total())
item1.apply_discount(0.8)
print(item1.calculate_total())

