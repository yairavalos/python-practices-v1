## Ejemplo de función para conocer importancia de tuplas
def prueba(i = []):
    i.append(1)
    print(i)
# Sintaxis de Clases
class Clase(object):
    pass
# Métodos
class Celular(object):
    def llamar(self):
        print("Iniciando llamada")
    def colgar(self):
        print("Se termino la llamada")
mi_cel = Celular()
mi_cel.llamar()
mi_cel.colgar()
# Atributos
class Celular(object):
    estado = "en llamada"
    marca = "Nokia"
    def llamar(self):
        self.estado = "en llamada"
        print("Iniciando llamada")
    def colgar(self):
        self.estado = "en modo ahorro de energia"
        print("Se termino la llamada")
### Crear una clase de tu comida favorita
mi_cel = Celular()
mi_cel.estado
mi_cel2 = Celular()
# Constructor
class Celular(object):
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
    def llamar(self):
        self.estado = "en llamada"
        print("Iniciando llamada")
    def colgar(self):
        self.estado = "en modo ahorro de energia"
        print("Se termino la llamada")
mi_cel = Celular("Xiaomi", "en modo ahorro de energia")
mi_cel2 = Celular("Nokia", "en llamada")
# usar self.i como contador
class Acumulador(object):
    def __init__(self):
        pass
        #TODO
    def sumar_una_unidad(self):
        pass
        #TODO
    def resta_una_unidad(self):
        pass
        #TODO
    def mostar_acumulador(self):
        pass
        #TODO   
#Ejercicio guiado volver nuestro código de registro de usarios visto en clase a la forma orientada a objetos
# Ejercicio en clase crea el objeto producto, 
# a partir de diferentes metodos crea las siguientes acciones:
# Definir un precio sin iva inicial del producto (Constructor) ok
# Modificar el precio actual del producto ok
# Comprar el MISMO producto y agregar al carrito ok
# Mostrar precio con iva del producto ok
# Mostrar el impuesto, subtotal y total de la cantidad de productos agregados al carrito