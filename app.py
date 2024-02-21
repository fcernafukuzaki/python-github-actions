# Clase Pedido pedido.py
class Pedido():
    def __init__(self):
        self.destinatario = None
        self.productos = []
        self.costo_envio = None

    def __str__(self):
        return f'El destinatario {self.destinatario} ha pedido los productos: {self.productos}. El costo de envío es: {self.costo_envio}'

# Clase PedidoBuilder pedido_builder.py
from abc import ABC, abstractmethod

class PedidoBuilder(ABC):
    """
    Interfaz a la clase Pedido con los métodos para crear la clase Pedido.
    """

    @abstractmethod
    def set_destinatario(self, destinatario) -> None:
        pass

    @abstractmethod
    def add_productos(self, producto) -> None:
        pass

    @abstractmethod
    def set_costo_envio(self, costo_envio) -> None:
        pass

    @abstractmethod
    def build(self):
        pass

# Clase ClientePremiumPedidoBuilder clientepremiumpedido_builder.py
class ClientePremiumPedidoBuilder(PedidoBuilder):
    """
    Clase que construye un objeto en concreto.
    Dentro de la clase se especifica qué valores va a tener.
    """
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.pedido = Pedido()

    def get_pedido(self) -> Pedido:
        return self.pedido

    def set_destinatario(self, destinatario) -> None:
        self.pedido.destinatario = destinatario
        return self

    def add_productos(self, producto) -> None:
        if isinstance(producto, list):
            self.pedido.productos.extend(producto)
        else:
            self.pedido.productos.append(producto)
        return self

    def set_costo_envio(self, costo_envio) -> None:
        self.pedido.costo_envio = costo_envio
        return self

    def build(self) -> Pedido:
        pedido = self.pedido
        self.reset()
        return pedido

# Clase PedidoDirector pedido_director.py
class PedidoDirector:
    def __init__(self, builder):
        self.builder = builder

    def make(self, destinatario=None, productos=[], costo_envio=0.0):
        return self.builder \
            .set_destinatario(destinatario) \
            .add_productos(productos) \
            .set_costo_envio(costo_envio) \
            .build()

# Clase Main main.py
# Uso del patrón Builder
builder = ClientePremiumPedidoBuilder()
director = PedidoDirector(builder)

# Construcción de un carro con un conjunto específico de características
pedido1 = director.make(destinatario='Francisco', productos=['Mouse', 'Mochila'], costo_envio=9.5)

# Imprimir el resultado
print(pedido1)

pedido2 = director.make(destinatario='Yann LeCun', productos=['Laptop'], costo_envio=20.98)
print(pedido2)
