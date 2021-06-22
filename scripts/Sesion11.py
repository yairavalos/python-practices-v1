### try
try:
   pass
except:
   pass
### except
0/0
texto
2+1
try:
   0/0
   texto
except NameError:
   print("algo salió mal con la variable que estas consultando")
except ZeroDivisionError:
   print("Error, no puedes dividir entre cero")
try:
   0/0
   texto
except (ZeroDivisionError, NameError):
   print("algo salió mal con la variable que estas consultando")
except:
   print("Error desconocido")
ZeroDivisionError:
NameError:
lista = [1, 2]
try:
   lista[2]
except IndexError:
   print("Estás fuera de rango, Loco!")
try:
   0/0
   texto
except:
   print("algo salió mal con la variable que estas consultando")
try:
   0/0
except Exception as e:
   print(f'El error que te ocurrió es: {e}')
### else
try:
   0/0
   x = 1
except:
   print("DIvisión entre cero")
else:
   x += 1
try:
   x = 1
except NameError:
   print("la variable no ha sido creada")
except ZeroDivisionError:
   print("DIvisión entre cero")
else:
   x += 1
print(x)
try:
   x = 1
except ZeroDivisionError:
   print("DIvisión entre cero")
else:
   x = x + y
print(x)
### Ejercicios
#1
resultado = 10/0
#2
lista = [1, 2, 3, 4, 5]
lista[10]
#3
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
colores['blanco']
#4
resultado = 15 + "20"
error = True
try:
   x = 1
   x = x /0
   error = False
except ZeroDivisionError:
   print("DIvisión entre cero")
   del x
else:
   x = x ** 2
finally:
   if error:
       del x
### Creación de paquetes, Python es poderoso por sus paquetes
### Organizar código
### Reutilizar código
### importar paquetes.
import datetime
import datetime as dt
from datetime import datetime as dt
### cargar pi
from math import pi
### Usar las funciones
### Crear nuestro paquete
### Calculadora