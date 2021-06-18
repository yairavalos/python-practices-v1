# Métodos especiales
## __len__
# def __getitem__(self, ix):
#         return self.productos[ix]
###objeto[i]
###__eq__
class Poderosa(object):
    def __init__(self, tamanio = 10):
        self.tamanio = tamanio
    def __len__(self) -> int:
        print(f"tamaño {self.tamanio}")
        return(self.tamanio)
    def __floordiv__(self, objeto2:Poderosa) -> int:
        if isinstance(objeto2, Poderosa):
            return(self.tamanio // objeto2.tamanio)
        elif isinstance(objeto2, int):
            return(self.tamanio // objeto2)
        else:
            print("La comparación tiene que hacerse con objetos de la clase Poderosa")
            return None
poderosa = Poderosa()
len(poderosa)
poderosa1 = Poderosa()
poderosa1.__floordiv__(poderosa)
poderosa1 // poderosa
poderosa1 // 1
poderosa1.__floordiv__(1)
Operadores binarios
Operador           Método
+                  object.__add__(self, other)
-                  object.__sub__(self, other)
*                  object.__mul__(self, other)
//                 object.__floordiv__(self, other)
/                  object.__div__(self, other)
%                  object.__mod__(self, other)
**                 object.__pow__(self, other[, modulo])
>                 object.__rshift__(self, other)
&                  object.__and__(self, other)
^                  object.__xor__(self, other)
|                  object.__or__(self, other)
Operadores de asignación:
Operador          Método
+=                object.__iadd__(self, other)
-=                object.__isub__(self, other)
*=                object.__imul__(self, other)
/=                object.__idiv__(self, other)
//=               object.__ifloordiv__(self, other)
%=                object.__imod__(self, other)
**=               object.__ipow__(self, other[, modulo])
>=               object.__irshift__(self, other)
&=                object.__iand__(self, other)
^=                object.__ixor__(self, other)
|=                object.__ior__(self, other)
Operadores unarios:
Operador          Método
-                 object.__neg__(self)
+                 object.__pos__(self)
abs()             object.__abs__(self)
~                 object.__invert__(self)
complex()         object.__complex__(self)
int()             object.__int__(self)
long()            object.__long__(self)
float()           object.__float__(self)
oct()             object.__oct__(self)
hex()             object.__hex__(self)
Operadores de comparación
Operador          Método
=                object.__ge__(self, other)
>                 object.__gt__(self, other)
object.__lt__(a, b) <
object.__le__(a, b) <=
object.__eq__(a, b) ==
object.__ne__(a, b) !=
object.__ge__(a, b) >=
object.__gt__(a, b) >
### Crear la clase Hogar, crearle por lo menos 3 métodos y atributos, considera adicionalmente el atributo número de cuartos y el de superficie en M2
### Crear la clase Departamento que hereda la clase hogar, crearle por lo menos 3 métodos y atributos
### Utilizar __add__ en hogar que sume los cuartos de una casa o un departamento con otra casa o departamento.
### Utilizar __len__ para devolver las dimensiones de la casa o depa
casa1 + depa1 # número de cuartos
len(casa1) # M2
class Hogar():
    def __init__(self, n_cuartos, m2):
        self.m2 = m2
        self.n_cuartos = n_cuartos
    def __len__(self):
        return self.m2
    def __add__(self, other):
        if isinstance(other, Hogar):
            return self.n_cuartos + other.n_cuartos
        else:
            print("NO es válida esa adición")
            return None
class Departamento(Hogar):
    def __init__(self, n_cuartos, m2, piso):
        super().__init__(n_cuartos, m2)
        self.piso = piso
depa1 = Departamento(m2 = 50, n_cuartos = 2, piso = 5)
len(depa1) # 50
casa1 = Hogar(7, 120)
depa1 + casa1
depa1 + 112
casa1 + 112
casa1 + depa1
isinstance(depa1, Hogar)
isinstance(casa1, Departamento)
issubclass(Hogar, Departamento)
issubclass(Departamento, Hogar)
### Interacción de clases
class Persona():
class Comida():
## Video juevos
## Vida y Ataques
class Guerrero():
class Arquero():
## set y get
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
### 1. Crear una tarjeta con un saldo inicial de $1000, el dueño eres tú y la vigencia es al día de tu próximo cumple
### 2 Crear una mercancia con precio de $12, nombre fritos, stock, que es el número de unidades en la tienda de 20, y 0% de descuento
### 2 Crear una botana con precio de $12, nombre maruchan, stock, que es el número de unidades en la tienda de 20, y 0% de descuento,
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