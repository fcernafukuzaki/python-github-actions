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