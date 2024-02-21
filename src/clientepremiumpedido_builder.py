from src.pedido import Pedido
from src.pedido_builder import PedidoBuilder


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