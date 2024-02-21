from abc import ABC, abstractmethod


# Clase PedidoBuilder pedido_builder.py
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
