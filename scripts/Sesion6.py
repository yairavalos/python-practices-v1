#Funciones
# def nombre_funcion(parametros):
#    código
 
def suma(x, y):
   return(x + y)
 
def resta(x, y):
   return(x - y)

resta(10, 5)
resta(x = 10, y = 5)
resta(y = 10, x = 5) #Tratar de mantener el orden original de la función

 
def multiplicacion(x, y):
   return x * y

a = 10
b = 20
respuesta = multiplicacion(x = a, y = b) == multiplicacion(y = a, x = b) 
respuesta = "si" if respuesta else "no"
print(
    "¿Es lo mismo x*y que y*x?", 
    respuesta
)
 
def division(x, y):
    if y == 0:
        print("No puedes dividir entre cero")
        return None
    return(x / y)

x = division(9, 0)
if x is None:
    print("Cuidado!!, x esta vacío")

division(9, 3)

 
def calculadora(x, y, operacion):
    print("Se usará la operacion", operacion)
    if operacion == "suma":
        return(suma(x, y))
    elif operacion == "resta":
        return(resta(x, y))
    elif operacion == "multiplicacion":
        return(multiplicacion(x, y))
    elif operacion == "division":
        return(division(x, y))
    else:
        print("No tenemos esa opearación")
        return None
 

bandera1 = True
bandera2 = True
if bandera1:
    print("bandera1")
elif bandera2:
    print("bandera2")

calculadora(10, 3, "elavar_al_cubo")
calculadora(10, 3, "suma")


 
# Valores por default
def calculadora(x, y, operacion = "suma"):
    print("Se usará la operacion", operacion)
    if operacion == "suma":
        return(suma(x, y))
    if operacion == "resta":
        return(resta(x, y))
    if operacion == "multiplicacion":
        return(multiplicacion(x, y))
    if operacion == "division":
        return(division(x, y))

print("Llamo a la función con un valor por defecto de operacion = 'suma'",calculadora(12, 15))
calculadora(12, 15, "division")



 
# def calculadora(operacion = "suma", x, y): #error!!!
#     print("Se usará la operacion", operacion)
#     if operacion == "suma":
#         return(suma(x, y))
#     if operacion == "resta":
#         return(resta(x, y))
#     if operacion == "multiplicacion":
#         return(multiplicacion(x, y))
#     if operacion == "division":
#         return(division(x, y))
 
def imprimir_hola(usuario):
   print(f'Hola {usuario}')
 
imprimir_hola("Ferdinand")

###############################
# Recibir por posición
# * al construir función
def imprimir(*x):
    for i in x:
        print(i)
imprimir(1,2,3,4,5)

#Otra opción x como lista
def imprimir(x:list) -> None:
    for i in x:
        print(i)
imprimir([1,2,3,4,5])

# * al pasar argumentos a la función
def suma(x, y, z, *a):
    return(x + y + z + a[0])

suma(*[5,6,7], 10, 11, 11, 11)

###############################
# Recibir por nombre
# ** al construir función
def imprimir(u, v, **x):
    print(x)
    for llave, valor in x.items():
        print(f"Recibí el argumento {llave} con valor de {valor}")
imprimir(u = 10, v = 11, x = 1, y = 2, z = 3, a = 4, k = 7)
imprimir(10, 11, x = 1, y = 2, z = 3, a = 4, k = 7)


# ** al pasar argumentos a la función
def suma(x, y):
    return(x + y)
suma(**{"x":12, "y":13})



### Descompreción de tuplas
def identidad(x, y, z):
    return x + 1, [1,2,3], "texto"
identidad(1,2,3)

x = 12
x, y, z = identidad(0,1,2)
print(x)
 
 
 
### Variables locales y globales
 
# Global
x = 15
def prueba():
    print(x)
prueba()
del x

# Locales
def imprimir_v_local():
    x = 15
    print(x)

imprimir_v_local()
# x


y = 10
def imprimir_v_local():
    y = 100
    print(y)
imprimir_v_local()


y = 10
def imprimir_v_local():
    global y
    y = 80
    print(y)
imprimir_v_local()
print(y)


def imprimir_v_local():
    global w, h, k, var1
    w = 80
    print(y)
imprimir_v_local()
print(w)







def generador(limite = 10):
    for i in range(limite):
        yield(i)

##Forma peligrosa
# lista = list(range(100000000))
# print(lista)
# for i in lista:
#     print(i)

for i in generador(100000000):
    print(i)
