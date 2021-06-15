#Funciones
def nombre_funcion(parametros):
   código
 
def suma(x, y):
   return(x + y)
 
def resta(x, y):
   return(x - y)
 
def multiplicacion(x, y):
   return x * y
 
def division(x, y):
   if y == 0:
       print("No puedes dividir entre cero")
       return None
   return(x / y)
 
def calculadora(x, y, operacion):
   print("Se usará la operacion", operacion)
   if operacion == "suma":
       return(suma(x, y))
   if operacion == "resta":
       return(resta(x, y))
   if operacion == "multiplicacion":
       return(multiplicacion(x, y))
   if operacion == "division":
       return(division(x, y))
 
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
 
# Recibir por posición
# * al construir función
# * al pasar argumentos a la función
 
 
# Recibir por nombre
# ** al construir función
# ** al pasar argumentos a la función
 
 

 
 
 
### Variables locales y globales
 
# Global
