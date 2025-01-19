class CartItem:
    discount_rate = 0.8
    item_count = 0

    #Class seviyesinde method
    @classmethod #decorator
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu."
    
    @classmethod
    def create_item(cls,data_str):
        name, price, quantity = data_str.split(",")
        #return cls(name,price,quantity)
        return CartItem(name,price,quantity)


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
    
    # instance methods
    def calculate_total(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

print(CartItem.display_item_count())
item1 = CartItem("Iphone",50000,3)
item2 = CartItem("Xiaomi",30000,2)
print(CartItem.display_item_count())

CartItem.create_item("Mouse,800,3")
print(CartItem.display_item_count())