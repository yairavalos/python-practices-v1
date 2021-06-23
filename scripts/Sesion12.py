### Pasos para crear un paquete:
# 1 Crear una carpeta con el nombre del paquete
# 2 Crear un fichero con el nombre de __init__.py
# 3 Depositar tus funciones en un fichero con ese nombre


# ¿Cómo creo un subpaquete?
# 1 Crear una subcarpeta dentro de la carpeta creada anterior con el nombre del subpaquete
# 2 Crear un fichero con el nombre de __init__.py
# 3 Depositar tus funciones en un fichero con ese nombres

# TODO

# Recordemos como importar paquetes:
# import paquete
# import paquete as pkg
# from paquete import funcion1, funcion2
# from paquete import *
from paquete_especial import *
import paquete_especial
import mi_paquete ## Carga todas las funciones
mi_paquete.suma(12, 13)
import mi_paquete as my_pkg ## Carga todas las funciones con alias
my_pkg.suma(13, 5)
from mi_paquete import suma, resta as suma_mi_paquete, resta_mi_pequete## Carga funciones especificas
suma(13, 14)
resta(13, 13)
from mi_paquete import *
suma(13, 14)
suma("12", 13)


from mi_python.ejercicios import hola_mundo as hm



### Dates
import datetime

x = datetime.datetime.now()
print(x) 

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.weekday())
print(x.strftime("%A")) 


dir(x)
help(x)

f"{str(x.year)[2:4]}/{x.month}"

type(x)
x.strftime("%y/%m")
x.strftime("%Y/%m")
x.strftime("%Y/%b")


### crear objeto datetime
import datetime

x = datetime.datetime(2020, 5, 17, 14, 30, 12)
x = datetime.datetime.now()
x
import pickle
f = open("fecha_actual.pkl", "wb")
pickle.dump(x,f)
f.close()

f = open("fecha_actual.pkl", "rb")
x_load = pickle.load(f)
f.close()
x_load





y = datetime.datetime(2020, 5, 18, 14, 30, 12)
delta = y - x
y + delta
print(x) 


#Referenicias
### Para más detalle del strftime
#https://www.w3schools.com/python/python_datetime.asp

#https://docs.python.org/es/3/library/datetime.html

### Math
import math
math.ceil(3.0001)
math.floor(3.99999)
math.trunc(3.99999)
x = 10
y = -10
x + y
y = math.copysign(y, x)
y
x + y

def division(x, y):
    resultado = x/y if y != 0 else math.inf
    return(resultado)



### JSON

import json
json.dumps({'4': 5, '6': 7}, sort_keys=True)
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
json.loads('["elemento1", {"llave2":["test", null, 1.0, 2]}]')

### Abrir archivos
#archivo-salida.py
f = open('holamundo.txt','wt') ### importante ver wb
f.write('hola mundo')
f.close()

f = open ('test.json','r') ### importante ver wb
datos_json = json.load(f)
datos_json
f.close()


f = open ('holamundo.txt','r')
mensaje = f.read()
f.close()
print(mensaje)


f = open('holamundo.txt','a')
f.write('\n' + 'Hola Mundo')
f.close()


f = open ('test.json','wt')
f.write(json.dumps(datos_json, indent=4))
f.close()

diccionario_nuevo = {
    "producto1": 12
}

f = open('test.json', "a")
f.write("\n" + json.dumps(diccionario_nuevo, indent=4))
f.close()

###Ejercicio para actualizar un json

### Problema se crea un diccionario para
### guardarlo en un archivo json
json_temp = [
    {"manzana": 12},
    {"mango": 13}
]

### Se muestra el diccionario como string
json.dumps(json_temp)

### Se crea la conexión con el archivo
### "test.json" y se guarda el diccionario 
### json_temp, recuerda usar json.dumps, sino
### tabla!!!

f = open("test.json", "wt")
f.write(json.dumps(json_temp, indent= 4))
f.close()

### Primer intento, pero no se guardo el formato
### deseado, el resultado fué malo :(
f = open("test.json", "a")
f.write(json.dumps({"pera":11}, indent= 4))
f.close()

### Propuesta, leerlo
f = open("test.json", "r")
var_temp_json = f.read()
f.close()
### Volver ese string a diccionario json.loads
json_temp = json.loads(var_temp_json)
### Agregar el nuevo elemento del dict,
### es valido usar append al ser un único elemento
json_temp.append({"pera":11})
### Alternativa
# json_temp.extend({"pera":11})
json_temp

### Guardamos el resultado
f = open("test.json", "wt")
f.write(json.dumps(json_temp, indent= 4))
f.close()



### Propuesta, leerlo
f = open("test.json", "r")
var_temp_json = json.load(f)
f.close()
### Agregar el nuevo elemento del dict,
### es valido usar append al ser un único elemento
json_temp.append({"pera":11})
### Alternativa
# json_temp.extend({"pera":11})
json_temp

### Guardamos el resultado
f = open("test.json", "wt")
f.write(json.dumps(json_temp, indent= 4))
f.close()


import pickle
f = open("test.pickle", "wb")
pickle.dump(json_temp,f)
f.close()


f = open("test.pickle", "rb")
diccionario_nuevo = pickle.load(f)
f.close()



f = open("data.csv", "r")
datos = f.read()
f.close()
data = [elemento.split(",") for elemento in datos.split("\n")]


import pandas as pd
pd.read_csv("data.csv")
pd.read_pickle("test.pickle")
df = pd.read_json("test.json")

type(df["json_total"][0])
df.to_pickle()