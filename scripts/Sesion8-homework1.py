
#Ejercicio guiado volver nuestro código de registro de usarios visto en clase a la forma orientada a objetos

# Ejercicio en clase crea el objeto producto, 
# a partir de diferentes metodos crea las siguientes acciones:
# Definir un precio sin iva inicial del producto (Constructor) ok
# Modificar el precio actual del producto ok
# Comprar el MISMO producto y agregar al carrito ok
# Mostrar precio con iva del producto ok
# Mostrar el impuesto, subtotal y total de la cantidad de productos agregados al carrito


class myProduct(object):

    # Attributes initialized into constructor
    # to avoid be modified by other instances of the class
       
    def __init__(self,product_name:str,price:float):
 
        self.myName = product_name
        self.myprice = price
        self.tax = 0.16
        self.mytax = price * self.tax
        self.mytotal = self.myprice + self.mytax

    # Methods

    def modify_price(self,new_price):
        
        self.myprice = new_price
        self.mytax = new_price * self.tax
        self.mytotal = self.myprice + self.myprice
        print(f'The product: {self.myName} its price: ${self.myprice} USD, the tax is ${self.mytax} USD and the final price is ${self.mytotal} USD has been modified')

    def display_prices(self):
        print(f'The product: {self.myName} its price is: ${self.myprice} USD, the tax is ${self.mytax} USD and the final price is ${self.mytotal} USD')



class myCart(object):
    
    # Attributes initialized into constructor
    # to avoid be modified by other instances of the class

    def __init__(self):
        self.cartList = []
        self.Qty = 0
        self.subTotal = 0
        self.taxes = 0
        self.total = 0
        print("Initializing Cart")

    # Methods

    def add_to_cart(self,product_obj:myProduct):
        self.cartList.append(product_obj)
        self.Qty = len(self.cartList)
        self.subTotal += product_obj.myprice
        self.taxes += product_obj.mytax
        self.total += product_obj.mytotal
        print(f'The product {product_obj.myName} has been added to the cart')

    def reduce_one_to_cart(self,product_obj:myProduct):
        self.productList = [item.myName for item in self.cartList]
        myIndex = self.productList.index(product_obj.myName)
        self.productList.pop(myIndex)
        self.Qty = len(self.cartList)
        self.subTotal -= product_obj.myprice
        self.taxes -= product_obj.mytax
        self.total -= product_obj.mytotal
        print(f'The product {product_obj.myName} has been removed by one from the cart')

    def remove_from_cart(self,product_obj:myProduct):
        self.cartList = [itemObj for itemObj in self.cartList if itemObj.myName != product_obj.myName]
        self.Qty = len(self.cartList)
        self.subTotal -= product_obj.myprice
        self.taxes -= product_obj.mytax
        self.total -= product_obj.mytotal
        print(f'All the items from {product_obj.myName} product has been removed from the cart')

    def display_total_bill(self):
        print(f'This is the subtotal: ${self.subTotal} USD of {self.Qty} items in your Cart, consider ${self.taxes} USD of taxes you need to pay the great total of: ${self.total} USD')
        print("This is the list of items you have selected")
        [print(item.myName) for item in self.cartList]

    def buy_cart_list(self):
        #Missing Code
        pass


productCart = myCart()

product1 = myProduct("Headset",20.01)
product1.display_prices()

productCart.add_to_cart(product1)
productCart.display_total_bill()

product2 = myProduct("Mouse",30.52)
product2.display_prices()

productCart.add_to_cart(product2)
productCart.display_total_bill()

product3 = myProduct("Keyboard",40.99)
product3.display_prices()

productCart.add_to_cart(product3)
productCart.display_total_bill()

productCart.remove_from_cart(product2)
productCart.display_total_bill()

product4 = myProduct("Screen 19-in",200.33)
product4.display_prices()

product4.display_prices()
productCart.add_to_cart(product4)
productCart.display_total_bill()

product1.display_prices()
productCart.add_to_cart(product1)
productCart.display_total_bill()

product1.display_prices()
productCart.add_to_cart(product1)
productCart.display_total_bill()

product5 = myProduct("USB Extention",10.99)
product5.display_prices()

productCart.add_to_cart(product5)
productCart.display_total_bill()

product1.display_prices()
productCart.reduce_one_to_cart(product1)
productCart.display_total_bill()

product1.display_prices()
product1.modify_price(20.99)

[myObj for myObj in productCart.cartList][0].myName




