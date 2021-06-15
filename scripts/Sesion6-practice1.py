"""
    una función que le pases una serie de parametros
    los pase como lista y se sume el total de ellos

"""

def sumtotal(*x):
    total = 0
    for i in x:
        total += i
    return total

print(sumtotal(1,2,3,5,7,9,11))
