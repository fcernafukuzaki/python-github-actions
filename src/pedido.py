# Clase Pedido pedido.py
class Pedido():
    def __init__(self):
        self.destinatario = None
        self.productos = []
        self.costo_envio = None

    def __str__(self):
        return f'El destinatario {self.destinatario} ha pedido los productos: {self.productos}. El costo de envío es: {self.costo_envio}'
