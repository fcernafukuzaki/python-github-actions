from src.clientepremiumpedido_builder import ClientePremiumPedidoBuilder
from src.pedido_director import PedidoDirector


if __name__ == "__main__":
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
