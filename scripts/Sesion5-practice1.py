"""
    Ejercicios visto en clase Sesión 5

"""

lista_lista = [1,2,3,4,5]
validar_lista = len([1 for myResult in lista_lista if isinstance(myResult,list) ]) > 0
print(validar_lista)


"""
    Ejercicio de actualización de Diccionarios

"""

## actualizar el siguiente diccionario dict_ejercicio
l_nombres2 = ["Osmar","Ivan","Carlos","Tonio","Rosy","Ferdinand"]
l_horas = [7,6,9,7,8,7]
 
dict_ejercicio = {}
 
for i, j in zip(l_nombres2, l_horas):
   dict_ejercicio.update({i: j})
   # dict_ejercicio.setdefault(i, j)
   # dict_ejercicio[i] = j
   print(f'{i} duerme {j} horas')

