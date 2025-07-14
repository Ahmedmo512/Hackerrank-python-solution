
# task
# Python Classes: Shopping_Cart and Item
# This program defines two classes: Item and ShoppingCart.
# 1. Item:
#    - Represents a product with a name and price.
#    - Initialized using Item(name: str, price: int).

# 2. ShoppingCart:
#    - Represents a shopping cart that can contain multiple items.
#    - Supports the following operations:
#        - add(item): adds an Item to the cart (items can be repeated).
#        - total(): returns the total cost of all items in the cart.
#        - len(cart): returns the total number of items in the cart
#                     (via __len__ method override).
#



class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price




class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self) :
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)


apple = Item("Apple", 3)
banana = Item("Banana", 5)

cart = ShoppingCart()
cart.add(apple)
cart.add(banana)
cart.add(apple)

print(cart.total())   #  3 + 5 + 3 = 11
print(len(cart))      #  3 
