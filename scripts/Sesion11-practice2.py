#2
lista = [1, 2, "3", 4, 5]

try:
    myTest = lista[2]
except IndexError as myerr:
    print(f'This is my Error: {myerr}')
    print(f'The list lenght is {len(lista)}')
else:
    print(f'This is the result {myTest}')
finally:
    print("Finishing the Testing")

#3
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }

try:
    myTest2 = colores['blanco']
except Exception as myerr2:
    print(f'This is my Error: {myerr2}')
    print(f'The list lenght is {len(colores)}')
else:
    print(f'This is the result {myTest2}')
finally: 
    print("Finishing Testing #2")

#4
resultado = 0
a = 15
b = "20"

try:    
    resultado = a + b
except Exception as myerr3:
    print(f'This is my Error: {myerr3}')
    resultado = float(a) + float(b)
    print(f'Second try {resultado}')
else:
    print(f'This is the result {resultado}')
finally: 
    print("Finishing Testing #3")

