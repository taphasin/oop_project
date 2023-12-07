
class Person:
  def __init__(self, firstname, lastname, adressid, userid):
    self.first_name = firstname
    self.last_name = lastname
    self.adress_id = adressid
    self.user_id = userid
    
    
class Login:
    def __init__(self, email, password, additional, personid):
        self.email = email
        self.password = password
        self.additional = additional
        self.person_id = personid
    
class Adress:
    def __init__(self, mooban, house, roadname, soi, subsoi, district, provoince, postalcode, addressid):
        self.mooban = mooban
        self.house = house
        self.road_name = roadname
        self.soi = soi
        self.sub_soi = subsoi
        self.district = district
        self.provoince = provoince
        self.postalcode = postalcode
        self.address_id = addressid
    
class Admin(Person):    
    def __init__(self, firstname, lastname, adressid, userid, adminid):
        Person.__init__(self, firstname, lastname, adressid, userid)
        self.admin_id = adminid
    
class Customer(Person):    
    def __init__(self, firstname, lastname, adressid, userid, customerid):
        Person.__init__(self, firstname, lastname, adressid, userid)
        self.customer_id = customerid
    
#---------------------------------Example----------------------------------
class Emp():
  	def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
 
Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)
#--------------------------------------------------------------------    
    
        
class Product():
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description):
    self.name = name
    self.picture = picture
    self.descrip = description
    self.list_of_price = list_of_price
    self.spicy_level = spicy_level
    self.suit_for_veget = suit_for_veget
    self.description = description

class ProductCatalog():
  def __init__(self):
    self.list_product = []
    
class NormalPizzaOrder(Product):
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, crust_size, cook_option, cheese_option, sauce_option, additional_instruction, quantity):
    super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
    self.crust_size = crust_size
    self.cook_option = cook_option
    self.cheese_option = cheese_option
    self.sauce_option = sauce_option
    self.additional_instruc = additional_instruction
    self.quantity = quantity
    
class HalfHalfPizzaOrder(Product):
  def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, first_half, second_half, crust_size, cheese_option_first_half, cheese_option_second_half, cook_option, sauce_option_first_half, sauce_option_second_half, additional_instruction, quantity):
    super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
    self.first_half = first_half
    self.second_half = second_half
    self.crust_size = crust_size
    self.cheese_option_first_half = cheese_option_first_half
    self.cheese_option_second_half = cheese_option_second_half
    self.cook_option = cook_option
    self.sauce_option_first_half = sauce_option_first_half
    self.sauce_option_second_half = sauce_option_second_half
    self.additional_instruction = additional_instruction
    self.quantity = quantity

class DrinkOrder(Product):
 def __init__(self, name, picture, list_of_price, spicy_level, suit_for_veget, description, size, quantity):
  super().__init__(name, picture, list_of_price, spicy_level, suit_for_veget, description)
  self.size = size
  self.quantity = quantity
    
    
    #--------------------------------------------------------------------   
class Cart:
  def __init__(self, username, list_of_items):
    self.__username = username
    self.__list_of_items = []
    
    
class Payment:
    def __init__(self, order_id, total, payment_method, payment_date, payment_status):
        self.order_id = order_id
        self.total = total
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.payment_status = payment_status

class Customer(Person):    
    def __init__(self, firstname, lastname, adressid, userid, customerid):
        Person.__init__(self, firstname, lastname, adressid, userid)
        self.customer_id = customerid

class CreditCardInfomation(Payment):
    def __init__(self, order_id, total, payment_method, payment_date, payment_status, card_name, expiration_date, card_numbers, cvv):
        Payment.__init__(self, order_id, total, payment_method, payment_date, payment_status)
        self.card_name = card_name
        self.expiration_date = expiration_date
        self.card_numbers = card_numbers
        self.cvv = cvv

class Person:
  def __init__(self, firstname, lastname, adressid, userid):
    self.first_name = firstname
    self.last_name = lastname
    self.adress_id = adressid
    self.user_id = userid

    

