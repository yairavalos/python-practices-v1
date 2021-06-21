### Crear la clase Mercancia
### con los siguientes atributos:
### precio
### nombre
### descuento
### stock
#con los siguientes métodos
### llevarse producto decrementa en una unidad el atributo stock

class Merchandise():
    # attributes -> initialized through constructor to avoid be modified by other instancies
    def __init__(self, product_name, flavor, message_str, price, discount, stock_qty):
        self.product_name = product_name
        self.flavor = flavor
        self.calories = message_str
        self.__price = price
        self.__discount = discount
        self.__stock = stock_qty
        
    # methods:
    def get__price(self):
        return self.__price

    def get__discount(self):
        return self.__discount

    def get__stock(self):
        return self.__stock

    def update_price(self, new_price, discount):
        self.__price = new_price
        self.__discount = discount

    def add_stock(self, qty):
        self.__stock += qty

    def remove_stock(self, qty):
        self.__stock -= qty

    def print_stock(self):
        print(f'This is the remaining stock of -- {self.product_name} -- with a quantity of -- {self.__stock} -- unit(s)')

### Crea una subclase de Mercancia que se llame botanas
# Agregar los siguientes atributos:
## sabor
## advertencia_calorias

class Snack(Merchandise):
    # attributes -> initialized through constructor to avoid be modified by other instancies
    def __init__(self, product_name, flavor, message_str, price, discount, stock_qty):
        super().__init__(product_name, flavor, message_str, price, discount, stock_qty)

    # methods
    def get__price(self):
        return super().get__price()

    def get__discount(self):
        return super().get__discount()

    def update_price(self, new_price, discount):
        return super().update_price(new_price, discount)

    def add_stock(self, qty):
        return super().add_stock(qty)

    def remove_stock(self, qty):
        return super().remove_stock(qty)
    
    def print_stock(self):
        return super().print_stock()


### Crea la clase Tarjetas,
#con los siguientes atributos:
### dueño
### saldo
### vigencia
#con los siguientes métodos
### compra(self, Mercancia) ### este método disminuye el saldo en la Tarjeta
### deposito(self) ### este método aumenta el saldo en la Tarjeta

import datetime

class accountCard():
    # attributes -> initialized through constructor to avoid be modified by other instancies
    def __init__(self):
        self.owner_name = "Victor Yair AValos Morales"
        self.expire_date = "09-27-2021"
        self.__balance = 0.00

        self.purchase_log = []
        self.purchase_amount_log = []
        self.purchase_date_log = []

        self.deposit_log = []
        self.deposit_date_log = []

    # methods

    def payment(self, product:Merchandise, product_qty:int, purchase_date:datetime):

        self.product_cost = product.get__price() * product.get__discount() * product_qty
        
        if product.get__stock() >= product_qty:

            if self.product_cost <= self.__balance:

                self.__balance -= self.product_cost

                product.remove_stock(product_qty)

                self.purchase_log.append(product.product_name)
                self.purchase_amount_log.append(self. product_cost)
                self.purchase_date_log.append(purchase_date)
            
            else:
                print("There is not enough Money to do the purchase")
        
        else:
            print(f'There is not enough stock for {product.product_name}, stock is {product.get__stock()}')

    def deposit(self, amount, deposit_date):

        self.__balance += amount

        self.deposit_log.append(amount)
        self.deposit_date_log.append(deposit_date)

    def print_balance(self):
        [print(f'Your current balance is: {self.__balance} pesos')]
        print_line()
        print("This is your balance log file")
        print_line()
        [print(f'Deposit amount of: {deposit} pesos at {deposit_date}') for deposit, deposit_date in zip(self.deposit_log,self.deposit_date_log)]
        print_line()
        print("This is your expenses log: ")
        print_line()
        if len(self.purchase_log) > 0:
            [print(f'Purchase: {purchase}, Price: {price}, Purchase Date {datelog}' for purchase, price, datelog in zip(self.purchase_log, self.purchase_amount_log, self.purchase_date_log))]
        else:
            print("There is not any expense movement in the current period")
        print_line()


# Aid Function in order to print a line into the console
def print_line():
    line_str = ""
    for i in range(40):
        line_str += "-"
    print(line_str)


### 1. Crear una tarjeta con un saldo inicial de $1000, el dueño eres tú y la vigencia es al día de tu próximo cumple
### 2 Crear una mercancia con precio de $12, nombre fritos, stock, que es el número de unidades en la tienda de 20, y 0% de descuento
### 2 Crear una botana con precio de $12, nombre maruchan, stock, que es el número de unidades en la tienda de 20, y 0% de descuento,
#calorías altas y sabor chipotle

print("\n")
print_line()

product1 = Merchandise("Fritos","Chipotle","High Level of Calories",20.01,0.15,50)
product1.print_stock()

product2 = Snack("Maruchan","Shrimp and Chili","Medium Level of Calories",17.53,0.05,200)
product2.print_stock()

creditCard1 = accountCard()
creditCard1.deposit(1000,datetime.datetime.now())
creditCard1.print_balance()

print("\n")

### Realiza las siguientes compras:
# 1 unos fritos
# 1 unos fritos
# 1 maruchan
# depósito de nómina de $5000
# 1 maruchan
# 1 maruchan
# 1 maruchan
# 1 maruchan

#Imprime el saldo actual de la tarjeta y el stock de botana y mercancia

counter = 0
user_action = ""
deposit_amount = 0
purchase_type = ""
product_qty = 0

while counter <= 20:

    user_action = input("What do you want to do: 1 for Deposit, 2 for Purchase, 3 for Stock Report --- ")

    if user_action == "1":

        deposit_amount = float(input("Please provide the Amount of Money that you want to deposit:"))
        creditCard1.deposit()
        creditCard1.print_balance()

    elif user_action == "2":
        
        purchase_type = input("What do you want to purchase: 1 for Fritos, 2 for Maruchan --- ")
        product_qty = int(input("Please provide the number of product that you want to buy --- "))

        if purchase_type == "1":
            creditCard1.payment(product1,product_qty,datetime.datetime.now())
        elif purchase_type == "2":
            creditCard1.payment(product2,product_qty,datetime.datetime.now())
        else:
            print("This product choice doesn´t exist, see you next")

        creditCard1.print_balance()
        print_line()
        product1.print_stock()
        product2.print_stock()

    elif user_action == "3":
        print("This is The Stock Report:")
        print_line()
        product1.print_stock()
        product2.print_stock()
        print_line()
        
    else:
        print("There is no such action, select another one")

    counter += 1

