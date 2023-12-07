
class Person:
		def __init__(self, firstname, lastname):
    		self.__firstname = firstname
    		self.__lastname = lastname
    		self.__addressid = []
        self.__loginid = []
    
class Login:
    def __init__(self, email, password, additional):
        self.__email = email
        self.__password = password
        self.__additional = additional
    
class Address:
    def __init__(self, mooban, house, roadname, soi, subsoi, district, provoince, postalcode):
        self.__mooban = mooban
        self.__house = house
        self.__roadname = roadname
        self.__soi = soi
        self.__subsoi = subsoi
        self.__district = district
        self.__provoince = provoince
        self.__postalcode = postalcode
    
class Admin(Person):    
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
    
class Customer(Person):    
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.cart = []
  
class Product():
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description):
    self.__name = name
    self.__picture = picture
    self.__descrip = description
    self.__list_of_price = list_of_price
    self.__spicy_level = spicy_level
    self.__suit_for_veget = suit_for_veget
    self.__description = description

class ProductCatalog():
  def __init__(self):
    self.__list_product = []
    
class NormalPizzaOrder(Product):
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, crust_size, cook_option, cheese_option, sauce_option, additional_instruction, quantity):
    super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
    self.__crust_size = crust_size
    self.__cook_option = cook_option
    self.__cheese_option = cheese_option
    self.__sauce_option = sauce_option
    self.__additional_instruc = additional_instruction
    self.__quantity = quantity
    
class HalfHalfPizzaOrder(Product):
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, first_half, second_half, crust_size, cheese_option_first_half, cheese_option_second_half, cook_option, sauce_option_first_half, sauce_option_second_half, additional_instruction, quantity):
    super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
    self.__first_half = first_half
    self.__second_half = second_half
    self.__crust_size = crust_size
    self.__cheese_option_first_half = cheese_option_first_half
    self.__cheese_option_second_half = cheese_option_second_half
    self.__cook_option = cook_option
    self.__sauce_option_first_half = sauce_option_first_half
    self.__sauce_option_second_half = sauce_option_second_half
    self.__additional_instruction = additional_instruction
    self.__quantity = quantity
class DrinkOrder(Product):
 def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, size, quantity):
  super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
  self.__size = size
  self.__quantity = quantity
    
    
    #--------------------------------------------------------------------   
class Cart:
  def __init__(self, username):
    self.__username = username
    self.__list_of_items = []
    
    
class Payment:
  def __init__(self, order_id, total, payment_method, payment_date, payment_status):
    self.__order_id = order_id
    self.__total = total
    self.__payment_method = payment_method
    self.__payment_date = payment_date
    self.__payment_status = payment_status
    
class CreditCardInfomation(Payment):
  def __init__(self, order_id, total, payment_method, payment_date, payment_status, card_name, expiration_date, card_numbers, cvv):
    Payment.__init__(self, order_id, total, payment_method, payment_date, payment_status)
    self.__card_name = card_name
    self.__expiration_date = expiration_date
    self.__card_numbers = card_numbers
    self.__cvv = cvv
  

class Cash(Payment):
  def __init__(self, order_id, total, payment_method, payment_date, payment_status, cash, change):
    Payment.__init__(self, order_id, total, payment_method, payment_date, payment_status)
    self.__cash = cash
    self.__change = change
    