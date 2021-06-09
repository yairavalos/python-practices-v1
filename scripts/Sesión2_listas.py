### Listas
# Listas ? <- por qué ### o #

mi_primer_lista = [1,3.1416, "Hola Mundo"]
list()
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
omite este código """ # puedes usar strings para documentar

#remove
mi_lista_1.remove(2) #ELIMINA EL PRIMER 2
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append( mi_lista_2)

### Ejemplo de eliminación de varios elementos
ejemplo_emma = [1, 2, 3, [1, 3]]
ejemplo_emma.remove([1,3])
ejemplo_emma.remove(3)

### ¿Cómo elimino un elemento de una lista en otra lista?
ejemplo_mario = [1, 2, 3, [1, 3]]
ejemplo_mario[3].remove(1)

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

# insert
mi_lista_1.insert(2, "texto")

# pop
mi_lista_1.pop(2)


# sort
mi_lista_1.remove([1,3]) ## opción para quitar lista
mi_lista_1.pop(3)
mi_lista_1.sort()

mi_lista_1 = ["a", "b", "c"]
mi_lista_1.sort()




### índices, otra vez!!
# [inicio:(fin + 1):salto]
x = [1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1,3] # 13
x[::] #todo los elemtos
x[1::] # del elemento 1 al len(x) - 1
x[1:len(x):] # del elemento 1 al len(x) - 1

x[len(x) - 1] # último elemento
x[-1] # último elemento 
x[len(x)-1:len(x)] # último elemento
x[::-1][0] # último elemento


# copy

# map


# filter

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