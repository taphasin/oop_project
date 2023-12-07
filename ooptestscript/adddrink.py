class User:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, Drink, quantity):
        item1 = Item(Drink, quantity)
        self.cart.recieve_item(item1)


class Cart:
    def __init__(self):
        self.item_list = []

    def recieve_item(self, item):
        self.item_list.append(item)

    def show_item_in_cart(self):
        for x in self.item_list:
            print(x.drink.name, x.quantity) 

class drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Item:
    def __init__(self, drink, quantity):
        self.drink = drink
        self.quantity = quantity

coke = drink("coke", 30)

cart_user1 = Cart()
user1 = User("Racha", cart_user1)

user1.add_to_cart(coke, "1")
cart_user1.show_item_in_cart()



'''
coke_light = drink("coke_light", 40)
Coke_Zero_No_Sugar = drink("Coke_Zero_No_Sugar", 30)
Coke_Bottle = drink("Coke_Bottle", 30)
sSinglecut_Weird_and_Gilly_Neipa = drink("coke", 30)
Singlecut_18_Watt_American_IPA = drink("coke", 30)
Singlecut_Softly_Spoken_Magic_Spells_Neipa = drink("coke", 30)
Night_Shift_Whirlpool_American_Pale_Ale = drink("coke", 30)
Night_Shift_Santilli_American_IPA = drink("coke", 30)
Night_Shift_Santilli_American_IPA = drink("coke", 30)
Knee_Deep_Deep_Haze_IPA = drink("coke", 30)
Knee_Deep_Deep_Clarity_West_Coast_IPA = drink("coke", 30)
Knee_Deep_Oopsie_D_hazy = drink("coke", 30)
Magnify_Vine_Shine_NEIPA = drink("coke", 30)
Revision_Playafication_NEIPA = drink("coke", 30)
Revision_Snarf_Snarf = drink("coke", 30)
Port_Brewing_Mongo_Imperial_IPA = drink("coke", 30)
Port_Brewing_Wipeout_American_IPA = drink("coke", 30)
Port_Brewing_High_Tide_American_IPA = drink("coke", 30)
The_Hop_Concept_Tropical_and_Juicy_Imperial_IPA = drink("coke", 30)
'''