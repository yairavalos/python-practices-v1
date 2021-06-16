"""
    Crear una función que recibe:
    
    Entrada:
    precios de productos sin iva como (lista)
    cuantos productos se compraron (lista)
    iva = 16%

    Procesa:
    subtotal = suma (precio sin iva [i] * cantidad [i]) para cada i en el indice de la lista
    impuesto = (suma (precio sin iva [i] * cantidad [i]) para cada i en el indice de la
    lista) * iva
    total = subtotal + impuesto
    
    Regresa:
    Calcular el subtotal, total

"""

def taxCalculator (priceList:list, qtyList:list) -> list:
    
    iva = 0.16
    subtotalList = []
    taxesList = []

    subtotalList = [price * qty for price, qty in zip(priceList, qtyList)]
    taxesList = [(price * qty)*iva for price, qty in zip(priceList, qtyList)]

    totalList = []
    totalList = [sub + tax for sub, tax in zip (subtotalList,taxesList)]

    subTotal = sumFunction(subtotalList)
    taxes = sumFunction(taxesList)
    total = sumFunction(totalList)

    print("Subtotal List: ")
    print(subtotalList)
    print("Taxes List: ")
    print(taxesList)
    print("Total List: ")
    print(totalList)

    return subTotal, taxes, total


def sumFunction (sumList: list) -> float:

    localSum = 0

    for item in sumList:
        localSum += item

    return localSum


productList = [20.33,40.55,17.01,18.09,39.99,47.50]
quantityList = [2,1,3,7,2,1]

mySubTotal, myTaxes, myTotal = taxCalculator (productList, quantityList)

print("Subtotal: ")
print(mySubTotal)
print("Taxes: ")
print(myTaxes)
print("----------------------")
print("Total: ")
print(myTotal)




