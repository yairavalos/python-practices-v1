### Polimorfismo
### __add__
class Entero():
    def __init__(self, x):
        self.x = int(x)
    def __str__(self, x):
        pass
    def __add__(self, ext):
        return(self.x + int(ext.x))

class Cadena():
    def __init__(self, x):
        self.x = str(x)
    def __add__(self, ext):
        return(self.x + str(ext.x))


entero1 = Entero(10)
entero2 = Entero(10)
entero1.__add__(entero2)
Entero.__add__(entero1, entero2)

str.upper("Hola Mundo")
"Hola Mundo".upper()


cadena1 = Cadena("10")
entero1.__add__(cadena1) #10 + "10"
entero1 + cadena1
cadena2 = Cadena("Hola mundo")
entero1 + cadena2
cadena1 + entero1 #"10" + 10
entero1.x
cadena1.x
10 + "10"


### Encapsulamiento
##__
class Producto(object):
    def __init__(self, precio_sin_iva = 100, iva = 0.16):
        self.carrito = []
        self.__precio_sin_iva = precio_sin_iva
        self.iva = iva
        self.__precio_con_iva = (1 + iva) * precio_sin_iva
        self.__calcular_totales()
    def modificar_precio(self, precio_sin_iva):
        self.__precio_sin_iva = precio_sin_iva
        self.__precio_con_iva = (1 + self.iva) * self.__precio_sin_iva
        self.__calcular_totales()
        # self.precio_con_iva = (1 + self.iva) * nuevo_precio_sin_iva
    def mostrar_precio_iva(self):
        print(self.__precio_con_iva)
    def comprar(self, unidades = 3):
        self.carrito.extend(unidades * [1])
        self.__calcular_totales()
    def __calcular_totales(self):
        self.subtotal = self.__precio_sin_iva * len(self.carrito) #[1, 1, 1]
        self.impuesto = self.subtotal * self.iva
        self.total = self.subtotal + self.impuesto
    def mostrar_totales(self):
        print(f"Has comprado: {len(self.carrito)}, dando un subtotal de: {self.subtotal}, pagas de impuesto: {self.impuesto}, el total que vas a pagar es: {self.total}")
producto1 = Producto(150) # Se crea un producto de un precio sin iba de 150
print(producto1.comprar()) # Se compran 3 unidades de este producto
print(producto1.mostrar_totales()) # Se muestra los detalles de la compra
producto1.precio_sin_iva = 120 # Se intenta modificar el precio sin iva
print(producto1.mostrar_totales())
producto1.modificar_precio(170)


#Crear la clase AparatoElectronico
#Atributos
#encendido (True, False)
#marca
#dimensiones
#funciona (True, False)
#Métodos
#encender afecta el atributos encendido
#descomponer afecta el atributos estado_general
#componer afecta el atributos funciona
#apagar afecta el atributo encendido
##################################################################
#Crear la clase Telefono
#Atributos
#encendido (True, False)
#marca
#dimensiones
#funciona (True, False)
#funcionan_teclas (True, False)
#Métodos
#encender afecta el atributos encendido
#descomponer afecta el atributos funciona
#componer afecta el atributos funciona
#apagar afecta el atributos encendido
#descomponer_teclas afecta el atributos funcionan_teclas
#componer_teclas afecta el atributos funcionan_teclas
#Crear la clase Celular
#Atributos
# wifi
# gsm
# llamada = (True, Falses)
#Métodos
# conectar(, red = {wifi, gsm})
# desconectar(, red = {wifi, gsm})
# realizar_llamada()
# colgar()
# tomar_foto

class AparatoElectronico(object):
  def __init__(self, encendido, marca, dimensiones, estado_general = True):
    self.encendido = encendido
    self.marca = marca
    self.dimensiones = dimensiones
    self.estado_general = estado_general
  def encender(self):
    self.encendido = True
  def descomponer(self):
    self.estado_general = False
  def componer(self):
    self.estado_general = True
  def apagar(self):
    self.encendido = False


class Telefono(object):
  def __init__(self,encendido, marca,dimensiones,estado_general,estado_teclas):
    self.encendido = encendido
    self.marca = marca
    self.dimensiones = dimensiones
    self.estado_general = estado_general
    self.estado_teclas = estado_teclas
  def encender(self):
    self.encendido = True
  def descomponer(self):
    self.estado_general = False
  def componer(self):
    self.estado_general = True
  def apagar(self):
    self.encendido = False
  def descomponer_teclas(self):
    self.estado_teclas = False
  def componer_teclas(self):
    self.estado_teclas = True


class Celular(object):
  def __init__(self,llamada, wifi = True,gsm = True):
    self.wifi = wifi
    self.gsm = gsm
    self.llamada = llamada
  def conectar(self, red="wifi"):
    if red == "wifi":
      self.wifi = True
    elif red == "gsm":
      self.gsm = True
  def desconectar(self, red="wifi"):
    if red == "wifi":
      self.wifi = False
    elif red == "gsm":
      self.gsm = False
  def realizar_llamada(self):
    self.llamada = True
  def colgar(self):
    self.llamada = False
  def tomar_foto(self):
    print("Estoy tomando una foto")
    self.llamada = False
aparato = AparatoElectronico(True, "sony", [40, 60], True)
celular = Celular(False)
celular.desconectar()
celular.wifi




### Herencia

class AparatoElectronico():
  def __init__(self, encendido, marca, dimensiones, estado_general = True):
    self.encendido = encendido
    self.marca = marca
    self.dimensiones = dimensiones
    self.estado_general = estado_general
  def encender(self):
    self.encendido = True
  def descomponer(self):
    self.estado_general = False
  def componer(self):
    self.estado_general = True
  def apagar(self):
    self.encendido = False
  def mostrar_estado(self):
    print(self.encendido,
        self.marca,
        self.dimensiones,
        self.estado_general)


class Telefono(AparatoElectronico):
  def __init__(self,encendido,dimensiones,estado_teclas, estado_general = False, marca = "Generico"):
    super().__init__(encendido, marca, dimensiones, estado_general)
    self.estado_teclas = estado_teclas
  def descomponer_teclas(self):
    self.estado_teclas = False
  def componer_teclas(self):
    self.estado_teclas = True
  def mostrar_estado(self):
    print(self.encendido,
        self.marca,
        self.dimensiones,
        self.estado_general, 
        self.estado_teclas
        )
  def mostrar_estado_anterior(self):
    super().mostrar_estado()
telefono1 = Telefono(True, [40, 60], True, True)
telefono1.mostrar_estado()
telefono1.mostrar_estado_anterior()




### Overwriting
### Super clases Sub clases
### Herencia multiple
### Se da preferencia a la primer clase que se coloca
# class Clase1():
#   def correr():
#     print("estoy corriendo")
# class Clase2():
#   def correr():
#     print("ejecutando correr")
# class Clase(Clase1, Clase2)
#     def __init__(self, params):
#         Clase1.__init__(params)
#         Clase2.__init__(params)
# ### Se hereda correr de Clase1
# ### aplica para métodos y atributos
# class Clase (Clase1)
#     def __init__(self, params):
#         Clase1.__init__(params)
#         # super().__init__(params) equivalente a la línea anterior


### Ejercicio en clase
class IntrumentoMusical(object):
    def __init__(self, material, dimensiones, peso):
        self.material = material
        self.dimensiones = dimensiones
        self.peso = peso
    def sonar(self):
        print("Estoy sonando")
    def afinar(self):
        print("Me estan afinando")
    def mantenimiento(self):
        print("Me estan arreglando")

class InstrumentoElectrico(IntrumentoMusical):
    def energizar(self):
        print("Se conecto a la toma de corriente")
    def encender(self):
        print("Se encendió el instrumento")
    def sonar(self):
        print("Estoy sonando usando un amplificador")
    def mantenimiento(self):
        print("Me estan cambiando los cables")

class InstrumentoAcustico(IntrumentoMusical):
    pass

class InstrumentoCuerda(IntrumentoMusical):
    def rasgar(self):
        print("Estan rasgando mis cuerdas")
    def mantenimiento(self):
        print("Cambiando cuerda")

class InstrumentosViento(IntrumentoMusical):
    pass

class Guitarra(InstrumentoCuerda, InstrumentoElectrico):
    pass

guitarra = Guitarra("madera", [110, 140], 3)
guitarra.mantenimiento()
guitarra.sonar()
guitarra.rasgar()
guitarra.encender()
guitarra.afinar()

dir(guitarra)

### Antonio pregunta:
### ¿Cómo ejecuto mantenimiento asociado a la clase InstrumentoElectrico?
class Guitarra(InstrumentoCuerda, InstrumentoElectrico):
    def mantenimiento(self):
        super().mantenimiento()
        return InstrumentoElectrico.mantenimiento(self)
guitarra = Guitarra("madera", [110, 140], 3)
guitarra.mantenimiento()


# Llevar las clases creadas a una estructura jerárquica para reutilizar código
# Principio de sustitución
# Un objeto creado a partir de la subclase es una instancia de la súper clase
isinstance(guitarra, IntrumentoMusical) 

instrumento = IntrumentoMusical("madera",[150, 140], 7)
isinstance(instrumento, Guitarra) 


# Crear las siguientes clases
### Transportes
#Atributos
#Marca
#Dimensiones
#Capacidad de usuarios
#Desplazamiento
print("Se esta moviendo el transporte ")
### Terrestres
#Atrubutos
#Número de llantas (n_llantas)
#Tipo de terreno de desplazamiento
#Desplazamiento
print("Se esta moviendo el transporte terrestres")
### Autos
# A/C
# Rin
#Desplazamiento
desplazamiento_clase_padre
print("Se esta moviendo el auto")
### Motos
#Método
# Cabillito
# Revase en corto espacio
#Desplazamiento
print("Se esta moviendo la moto")
# Relaciones
# Transportes -> Terrestre
# Terrestre -> Auto
# Terrestre -> Moto
class Transporte(object):
    def __init__(self, marca, dimensiones, capacidad_usuarios):
        self.marca = marca
        self.dimensiones = dimensiones
        self.capacidad_usuarios = capacidad_usuarios
    def desplazar(self):
        print("Me estoy moviendo Transporte")
class Terrestre(Transporte):
    def __init__(self, marca, dimensiones, capacidad_usuarios, n_llantas, tipo_terreno):
        super().__init__(marca, dimensiones, capacidad_usuarios)
        #Transporte.__init__(self,marca, dimensiones, capacidad_usuarios)
        self.n_llantas = n_llantas
        self.tipo_terreno = tipo_terreno
    def desplazar(self):
        print("Me estoy moviendo Terrestre")

class Tigre():
    def desplazar(self):
        print("El tigre se esta desplazando")
tigre1 = Tigre()
jeep = Terrestre("jeep", "4x7", 5, 4, "4x4")
transporte = Transporte("df", "md", 100)
tigre1.desplazar()
jeep.desplazar()
transporte.desplazar()

def mover(objeto):
    objeto.desplazar()

mover(tigre1)
mover(jeep)
mover(transporte)


class ReadEXcel():
    def read(self):
        print("Estoy leyendo un excel")

class ReadTxt():
    def read(self):
        print("Estoy leyendo un txt")

def read_(objecto):
    objecto.read()

excel = ReadEXcel()
txt = ReadTxt()

read_(excel)
read_(txt)



### Crear la clase Mercancia
### con los siguientes atributos:
### precio
### nombre
### descuento
### stock
#con los siguientes métodos
### llevarse producto decrementa en una unidad el atributo stock
### Crea una subclase de Mercancia que se llame botanas
# Agregar los siguientes atributos:
## sabor
## advertencia_calorias
### Crea la clase Tarjetas,
#con los siguientes atributos:
### dueño
### saldo
### vigencia
#con los siguientes métodos
### compra(self, Mercancia) ### este método disminuye el saldo en la Tarjeta
### deposito(self) ### este método aumenta el saldo en la Tarjeta
### 1. Crear una tarjeta con un saldo inicial de $1000, el dueño eres tú y la vigencia es el día de tu próximo cumple
### 2. Crear una mercancia con precio de $12, nombre fritos, stock, que es el número de unidades en la tienda de 20, y 0% de descuento
### 3. Crear una botana con precio de $12, nombre maruchan, stock, que es el número de unidades en la tienda de 20, y 0% de descuento,
#calorías altas y sabor chipotle
### Realiza las siguientes compras:
# 1 unos fritos
# 1 unos fritos
# 1 maruchan
# depósito de nómina de $5000
# 1 maruchan
# 1 maruchan
# 1 maruchan
# 1 maruchan
#Imprime el saldo actual de la tarjeta y el stock de botana y mercancia