# Hacer los siguientes ejercicios en base a una lista inicial

# ordernar -> sort

# promedio -> sum(x)/len(x)

# mediana -> [1,2,3,4] -> (2+3)/2

# moda -> lista -> 50

# Generar la lista

x = list(range(100))
x.extend([50,50,50,50])
x.extend([47,47,47,47,47,47,47,47,47,47,47,47,47])
x.extend([19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19])
x.extend([61 for i in range(30)])
x.extend([33 for i in range(41)])
x.sort()

print(x)

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

