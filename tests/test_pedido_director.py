from src.clientepremiumpedido_builder import ClientePremiumPedidoBuilder
from src.pedido_director import PedidoDirector


def test_pedido_francisco():
    builder = ClientePremiumPedidoBuilder()
    director = PedidoDirector(builder)

    # Construcción de un carro con un conjunto específico de características
    pedido1 = director.make(destinatario='Francisco', productos=['Mouse', 'Mochila'], costo_envio=9.5)

    # Imprimir el resultado
    print(pedido1)
    assert pedido1.destinatario == 'Francisco'

def test_pedido_francisco_cerna():
    builder = ClientePremiumPedidoBuilder()
    director = PedidoDirector(builder)

    # Construcción de un carro con un conjunto específico de características
    pedido1 = director.make(destinatario='Francisco Cerna', productos=['Mouse', 'Mochila'], costo_envio=9.5)

    # Imprimir el resultado
    print(pedido1)
    assert pedido1.destinatario == 'Francisco Cerna'