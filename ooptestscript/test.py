from typing import Union

from fastapi import FastAPI

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

class Drink:
    def init(self, name, price):
        self.name = name
        self.price = price

class NormalPizza:
    def init(self, name, price):
        self.name = name
        self.price = price

class Item:
    def init(self, pizza, crust, cheese):
        self.pizza = pizza
        self.crust = crust
        self.cheese = cheese

class Catagoloug:
    def init(self):
        self.list = []

    def add_item_to_list(self, item):
        self.list.append(item)

    def show_item_list(self):
        for i in self.list:
            print(i.name, i.price)

app = FastAPI()


@app.get("/")
def read_root():
    return {drink_cataloug.show_item_list()}


pereroni = NormalPizza("Perperon", 300)
hawaian = NormalPizza("hawaian", 400)
coke = Drink("coke", 40)
spike = Drink("spike", 40)

pizza_cataloug = Catagoloug()
pizza_cataloug.add_item_to_list(pereroni)
pizza_cataloug.add_item_to_list(hawaian)

drink_cataloug = Catagoloug()
drink_cataloug.add_item_to_list(coke)
drink_cataloug.add_item_to_list(spike)

cart_user1 = Cart()
user1 = User("Racha", cart_user1)