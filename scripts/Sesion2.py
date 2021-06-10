### Python no tiene i++, pero...
print("Inicializando i con un valor de 1")
i = 1
print("Sumamos una unidad")
i += 1 # i=i+1
print("El resultado es:" + str(i))

print("Restamos una unidad")
i -= 1
print("El resultado es:" + str(i))

print("Multiplicar una unidad")
i *= 5 #i = i * 5
print("El resultado es:" + str(i))

print("Dividir una unidad")
i /= 10
print("El resultado es:" + str(i))

print("Potencia una unidad")
i **= 2
print("El resultado es:" + str(i))

print("Modulo una unidad")
i *= 8
i %= 2
print("El resultado es:" + str(i))

i = 10
print("División entera una unidad")
i //= 3
print("El resultado es:" + str(i))


### Posición
j = 10
texto_resultado = "El resultado es: {} texto adicional: {}"
print(texto_resultado)
print(texto_resultado.format('"10"',8))
print(texto_resultado)
texto_resultado = texto_resultado.format(i, j)
print(texto_resultado)

### Nombre
j = 10
texto_resultado = "El resultado es: {var2} texto adicional: {var1}"
print(texto_resultado)
print(texto_resultado.format(var1 = 8.5, var2 = i))
texto_resultado = texto_resultado.format(var1 = i, var2 = j)
print(texto_resultado)

x, y = 10, 11
print("x tiene:", x)
print("x tiene:", y)

### f-strings
nombre = "Arturo"
apellido = "Tellez"

print(f"Bienvenido {nombre.upper()} {apellido}")
print("""
Texto en
Multiples
lineas
""")

mi_empresa = """ GL
Construir Empresas inteligentes
Solución de IoT, Big Data y AI para la industría
"""

""" nombre_empresa
objetivo
qué hace
"""


#### Funciones type
print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("True es un bool", type(True))
print("3.33333 es un float", type(3.33333))

##Ejemplo con variables
x = 5
print("5 es un entero", type(x))



