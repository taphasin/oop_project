class User:
    def init(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, pizza, chrust, cheese):
        item1 = Item(pizza, chrust, cheese)
        self.cart.recieve_item(item1)



class Cart:
    def init(self):
        self.item_list = []

    def recieve_item(self, item):
        self.item_list.append(item)

    def show_item_in_cart(self):
        for x in self.item_list:
            print("name: " + x.pizza.name)
            print("crust: " + x.crust)
            print("cheese " + x.cheese)

class Item:
    def init(self, pizza, crust, cheese):
        self.pizza = pizza
        self.crust = crust
        self.cheese = cheese

class NormalPizza:
    def init(self, name, price):
        self.name = name
        self.price = price

pereroni = NormalPizza("Perperon", 300)
hawaian = NormalPizza("hawaian", 400)

cart_user1 = Cart()
user1 = User("Racha", cart_user1)




user1.add_to_cart(pereroni, "big", "extra")
cart_user1.show_item_in_cart()