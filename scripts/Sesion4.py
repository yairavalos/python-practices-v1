"""
Crea una lambda en una variable que se llame “suma”
que tome dos valores: x, y, los cuales pueda sumarlos sin
importar si es string o entero o mezcla. Por ejemplo si
recibe: 0 + “a” devolvería: “0a”
"""


suma = lambda x, y: x + y if isinstance(x,int) and isinstance(y,int) else str(x) + str(y)


x = "A"
isinstance(x,int)

y = 5
isinstance(y,str)

print(suma(x,y))

"""
● Crear una lambda que reciba un diccionario, devuelva el
siguiente texto: “El diccionario tiene como la llave <llave>
con valor de <calor>
● Crear un diccionario que almacene las características de
tu celular, (considera 3 características con una númerica
de preferencia)
● A la característica númerica sumale 10.
"""

myDict = lambda d: print(f"Contiene esta llave: {d.keys()} y contiene este valor: {d.values()}")

d = {"my Key":"Este es un valor"}

myDict(d)

"""
Crea dos listas, una con los nombres de tus compañeros y
la otra con la altura que creas que tenga, considera que
coincida el orden, por ejemplo:
Nombres = [“Arturo”]
Alturas = [1.70]
Lo anterior significa que tu piensas que Arturo mide 1.70 mts
Usando list comprehension selecciona los compañeros que
miden más de 1.65
"""

matesList = ["Arturo","Ferdinand","Rosy","Ivan","Toño","Yair"]
heightList = [1.71,1.75,1.68,1.79,1.72,1.70]

myHeights = [matesList[i] for i in range(len(heightList)) if heightList[i] > 1.72]
print(myHeights)

"""
Pregunta la altura real de tus compañeros y guárdala en
una lista
● Usando List comprehension regresa verdadero si
estuviste a 3 centímetros de adivinar la altura real de tu
compañero
● Cuéntanos a cuantos compañeros casi adivinas su altura
"""

realHeightList = [input(f"Dame la altura de {str(mate)} : ") for mate in matesList ]
print(realHeightList)


"""
Crear conjuntos en clase
Propuesta:
Chilangos, no chilangos
Ingenieros, no ingenieros
En cada uno de los conjuntos pon el nombre de tus
compañeros.
¿Cuáles de tus compañeros son Chilangos e ingenieros?
"""

chilangos = {"Arturo","Rosy","Carlos","Leo","Tonio"}
noChilangos = {"Osmar","Yair","Alexa","Victor"}

ingenieros = {"Tonio","Yair","Aaron","Leo"}
noIngenieros = {"Rosy","Ferdinand","Alexa"}

chilengines = chilangos.intersection(ingenieros)
print(chilengines)

otherSet1 = noChilangos.intersection(noIngenieros)
print(otherSet1)


"""
    Ejercicios visto en clase Sesión 5

"""

lista_lista = [1,2,3,4,5]
validar_lista = len([1 for myResult in lista_lista if isinstance(myResult,list) ]) > 0
print(validar_lista)










