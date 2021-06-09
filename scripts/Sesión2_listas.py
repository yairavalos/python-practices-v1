### Listas
# Listas ? <- por qué ### o #

mi_primer_lista = [1,3.1416, "Hola Mundo"]
print("la variable mi_primer_lista es del tipo: ", type(mi_primer_lista))
mi_primer_tupla = (1, 3.1416, "Hola mundo")
print("la variable mi_primer_tupe es del tipo: ", type(mi_primer_tupla))
print("Cambiando una tupla a lista")
print(list(mi_primer_tupla))

###Asigna la referencia a Y
x = [1, 2] #Se crea la variable x, con una lista de 
#[1,2]
y = x
y[0] = 0
print(x)



###Asigna el valor de x a y
x = [1, 2] #Se crea la variable x, con una lista de 
#[1,2]
y = x.copy()
x[0] = 0
print(y)



#append
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append( mi_lista_2)
mi_lista_1[3][0]
mi_lista_1[3][1]

x = [1,
2,
[1, [3,3]]
]
x[2][1][0]

print("Resultado de hacer append de una lista [1, 2, 3] con [1, 3]:",mi_lista_1)
#extend
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.extend(mi_lista_2)
print(mi_lista_1 )


### Crear mi documentación
# ctrl + } # Sublime, notebooks
# ctrl + shift + 7 # VS
""" 
omite este código 
""" 
# puedes usar strings para documentar
# linea_codigo
#remove
u = 3
mi_lista_1.remove(u) #ELIMINA EL PRIMER 2
print(mi_lista_1)
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append( mi_lista_2)

#index
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append( mi_lista_2)
print(mi_lista_1)
#[1, 2, 3, [1, 3]]
mi_lista_1.index(3)
mi_lista_1.index([1, 3])
mi_lista_1 = [1, 2, 3, [1, 3], 3]
print(mi_lista_1.index(3))

#count
mi_lista_1.count(3)

# reverse
mi_lista_1 = [1, 2, 3, [1, 3], 3]
#aplican  reverse y [::-1]
#Resultado
#[1, 2, 3, [1, 3], 3]
mi_lista_1[::-1].reverse()
#mi_lista_1.reverse()[::-1] #error
#mi_lista_1.reverse() regresa None
print("La lista original era:", mi_lista_1)
mi_lista_1.reverse()
print(mi_lista_1)
print("Despues de aplicar reverse:", mi_lista_1)

# insert
print("La lista original era:", mi_lista_1)
mi_lista_1.insert(2, "texto")
print("Despues de aplicar insert:", mi_lista_1)


# pop
print("La lista original era:", mi_lista_1)
contenido_lista = mi_lista_1.pop(2)
print("Despues de aplicar pop:", mi_lista_1)



# sort
print("La lista original era:", mi_lista_1)
mi_lista_1.remove([1,3]) ## opción para quitar lista
print("Despues de aplicar remove:", mi_lista_1)

mi_lista_1.pop(3)
print("La lista original era:", mi_lista_1)
mi_lista_1.sort()
print("Despues de aplicar sort:", mi_lista_1)
# mi_lista_1.reverse()
mi_lista_1[::-1]

mi_lista_1 = ["a", "b", "c"]
mi_lista_1.sort()
mi_lista_1[::-1]




### índices, otra vez!!
# [inicio:(fin + 1):salto]
# [inicio:(fin ):salto] va a mostrar hasta fin - 1

x = [1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1,3] # 13
x[::] #todo los elemtos
x[1::] # del elemento 1 al len(x) - 1
x[1:len(x):] # del elemento 1 al len(x) - 1
# x[len(x)]
x[len(x) - 1] # último elemento
x[-1] # último elemento 
x[len(x)-1:len(x)] # último elemento
x[::-1][0] # último elemento


# 
#[1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 3]
list(map(lambda x: x + 10, x))
#[11, 12, 11, 12, 12, 11, 11, 12, 11, 12, 12, 11, 13]

#filter
list(filter(lambda x: x >= 2, x))

# del

