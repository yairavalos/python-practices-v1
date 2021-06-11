# Hacer los siguientes ejercicios en base a una lista inicial

# Generar la lista

from typing import Iterator
import math

x = list(range(100))
x.extend([50,50,50,50])
x.extend([47,47,47,47,47,47,47,47,47,47,47,47,47])
x.extend([19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19])
x.extend([61 for i in range(31)])
x.extend([33 for i in range(41)])

# ordernar -> sort

x.sort()
print(x)

# promedio -> sum(x)/len(x)

listSum = 0

for i in x:
    listSum += i

print("Sumatoria de X: " + str(listSum))

listAVG = listSum / len(x)
print("El Promedio de la Lista X es: " + str(listAVG))

# mediana -> [1,2,3,4] -> (2+3)/2

posMed = len(x)
listMedian = 0

if posMed %2 == 0:
    print("La longitud es par: " + str(posMed))
    posMed = int(posMed/2)
    listMedian = (x[posMed] + x[posMed + 1])/2

else:
    print("La longitud es impar: " + str(posMed))
    posMed = math.ceil(posMed/2)
    listMedian = x[posMed]

print("La mediana esta en la pos: " + str(posMed) + " y su valor es: " + str(listMedian))


# moda -> lista -> 50

y = [i for i in range(len(x))]
print(y)

z = [0 for i in range(len(x))]
print(z)

for n in y:
    for m in x:
        if m == n:
           z[n] += 1

print(z)

index = 0

for n in y:
    if n > 1:
        if z[n] > index:
            index = n

print(index)


