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

"""
    ejercicios del 15 de Junio del 2021

"""

# ejemplo de generadores

accum = 0

for i in range(10):
    print("Valor de i:" + str(i))
    print("Valor de accum:" + str(accum))
    accum += i

# mismo ejercicio de arriba pero con While (ej. Suma)

suma_total = 0
contador = 0

while contador < 10:
    suma_total += contador
    contador += 1
    # la clave esta en la posición del contador, después de suma_total

print(suma_total)


# mismo ejercicio de arriba pero con While (ej. Multiply)

mul_total = 1
contador1 = 1

while contador1 < 10:
    mul_total *= contador1
    contador1 += 1
    # la clave esta en la posición del contador, después de suma_total

print(mul_total)


# Concepto inicial

def recursiva(n):
    if n == 0:
        return()
    else:
        return(n-1)

# De esta manera el consumo de memoria es alto

def recursiva1(n):
    if n == 1:
        return(n)
    else:
        return recursiva1(n-1) + n

print(recursiva1(4))


# Programación Recursiva, ejemplo con la función de Fibonacci

def fib(n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)
    if n > 1:
        return fib(n-1) + fib(n-2)

# Programación Dinámica, mismo ej. Fibonacci
# busca acarrear el resultado en memoria

def dynamicFib (n):
    if n == 0:
        return(0)
    if n == 1:
        return(1)

    # creo que aqui falta un if n > 1
    
    aux = [0,1]
    
    for n in range(2,n):
        print(n)
        pass
    return(aux[0] + aux[1])


# Tarea es modificar aux [0,1] siguiente es [1,1] = 2 luego [1,2] = 3 luego [2,3] = 5






