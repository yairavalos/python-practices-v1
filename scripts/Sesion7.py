

### Recursivas
suma_acum = 0
for i in range(10):
    suma_acum += i
suma_acum 


suma_acum = 0
contador = 0
while contador < 10:
    suma_acum += contador
    contador += 1
print(suma_acum)


prod_acum = 1
for i in range(1,10):
    prod_acum *= i
prod_acum 


prod_acum = 1
contador = 1
while contador < 10:
    prod_acum *= contador
    contador += 1
print(prod_acum)


### Funciones recursivas
def recursiva(n):
    if n == 1:
        return(n)
    else:
        return(recursiva(n - 1) * n)
recursiva(9)


fibonacci(n) = fibonacci(n-2) + fibonacci(n-1)
fibonacci(1) = 1 
fibonacci(0) = 0


def fib(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    if n > 1:
        return(fib(n - 1) + fib(n - 2))

fib(0)
fib(1)

import datetime
inicio = datetime.datetime.now()
print(fib(12)) #144, 0:00:00.009151
print(datetime.datetime.now() - inicio)


def fib_p_dinamica(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    aux = [0,1]
    for n in range(2,n):
        f_n = aux[0] + aux[1]
        aux = [aux[1], f_n]
    return(aux[0] + aux[1])
fib_p_dinamica(0)
fib_p_dinamica(1)
fib_p_dinamica(2)
inicio = datetime.datetime.now()
fib_p_dinamica(50)
print(datetime.datetime.now() - inicio)




fibonacci(3) = fibonacci(2) + fibonacci(1)
fibonacci(2) = fibonacci(1) + fibonacci(0)
1 + 0 
fibonacci(3) = 1 + 1 = 3


