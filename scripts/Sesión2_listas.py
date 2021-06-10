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

# filter
list(filter(lambda x: x >= 2, x))

# del


### for en listas
for i in range(100):
    print(i)

lista_con_for = [i * 100 for i in range(100)]
### if en listas
i = 100
### para obtener los números pares
[i for i in range(100) if i % 2 == 0]
### para obtener los números impares
### not, !=
[i for i in range(100) if not i % 2 == 0]
[i for i in range(100) if i % 2 != 0]


### else en listas
x = [i if i % 2 == 0 else "No es par" for i in range(100) ]

### for usando listas
#a lista anterior sumarle 1 a los números enteros
[i + 1 for i in x if isinstance(i,int)]
[i + 1 for i in x if i % 2 == 0] #error por tratar de usar módulo con un str
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]

x[0] = "No es par" #Se equivocaron y en un par pusieron texto!!!!!
[i + 1 for i in x if isinstance(i,int)]
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]


[i + 1 if isinstance(i,int) else x[i] for i in x ] #error
[i + 1 if isinstance(i,int) else i for i in x ]
[i if isinstance(i,str) else i + 1 for i in x ]
[i if isinstance(i,str) else x[i] + 1 for i in x ]

[u for u in x]

[i for i in x]



#[ for variable_que_recorre_el_for in objeto_iterable if condicion depende variable_que_recorre_el_for]

activado = False
x = 1 if activado else 0
x



activado = False
[i for i in range(100) if activado]

activado = True
[i for i in range(100) if activado]

[i  if activado else 0 for i in range(100)]
activado = False
[i  if activado else 0 for i in range(100)]




### promedio


### mediana


### moda


### ordenar

# del

