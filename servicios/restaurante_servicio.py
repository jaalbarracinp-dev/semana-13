from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio, ruta_productos, ruta_usuarios):
        self.archivo_servicio = archivo_servicio
        self.productos = [
            Producto(**item)
            for item in archivo_servicio.leer_json(ruta_productos)
        ]
        self.usuarios = [
            Usuario(**item)
            for item in archivo_servicio.leer_json(ruta_usuarios)
        ]

    def validar_acceso(self, usuario, contrasena):
        return any(
            u.usuario == usuario and u.contrasena == contrasena
            for u in self.usuarios
        )

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def consultar_cantidades(self):
        return {p.nombre: p.cantidad for p in self.productos}
