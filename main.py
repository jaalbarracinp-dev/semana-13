import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("850x550")
        self.root.minsize(700, 450)

        base = Path(__file__).resolve().parent
        datos = base / "datos"

        archivo_servicio = ArchivoServicio()
        self.servicio = RestauranteServicio(
            archivo_servicio,
            datos / "productos.json",
            datos / "usuarios.json"
        )

        self.mostrar_login()

    def limpiar_vista(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_vista()
        self.login_view = LoginView(
            self.root,
            self.servicio,
            self.mostrar_principal
        )

    def mostrar_principal(self):
        self.limpiar_vista()
        self.main_view = MainView(
            self.root,
            self.servicio,
            self.mostrar_login
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()
