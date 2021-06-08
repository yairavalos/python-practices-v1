### Python no tiene i++, pero...
print("Inicializando i con un valor de 1")
i = 1
print("Sumamos una unidad")
i += 1
print("El resultado es:" + str(i))

### Posición
j = 10
texto_resultado = "El resultado es: {} texto adicional: {}"
print(texto_resultado)
print(texto_resultado.format(i, j))
texto_resultado = texto_resultado.format(i, j)
print(texto_resultado)

### Nombre
j = 10
texto_resultado = "El resultado es: {var2} texto adicional: {var1}"
print(texto_resultado)
print(texto_resultado.format(var1 = i, var2 = j))
texto_resultado = texto_resultado.format(var1 = i, var2 = j)
print(texto_resultado)

x, y = 10, 11

### f-strings
nombre = "Arturo"
apellido = "Tellez"

print(f"Bienvenido {nombre * 3} {apellido}")
print("""
Texto en
Multiples
lineas
""")

mi_empresa = """ GL
Construir Empresas inteligentes
Solución de IoT, Big Data y AI para la industría
"""


#### Funciones type
print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("True es un bool", type(True))
print("3.33333 es un float", type(3.33333))

##Ejemplo con variables
x = 5
print("5 es un entero", type(x))



