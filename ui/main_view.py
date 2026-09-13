import tkinter as tk
from tkinter import ttk, messagebox

class MainView:
    def __init__(self, root, servicio, on_logout):
        self.root = root
        self.servicio = servicio
        self.on_logout = on_logout

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="PANEL PRINCIPAL", font=("Arial", 20, "bold")).pack(pady=10)

        botones = tk.Frame(self.frame)
        botones.pack(pady=10)

        tk.Button(botones, text="Productos", width=18, command=self.mostrar_productos).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Usuarios", width=18, command=self.mostrar_usuarios).grid(row=0, column=1, padx=5)
        tk.Button(botones, text="Ventas (pendiente)", width=18, state="disabled").grid(row=0, column=2, padx=5)
        tk.Button(botones, text="Cerrar sesión", width=18, command=self.on_logout).grid(row=0, column=3, padx=5)

        self.contenido = tk.Frame(self.frame)
        self.contenido.pack(fill="both", expand=True, pady=15)

        self.mostrar_productos()

    def limpiar(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar()
        tk.Label(self.contenido, text="Productos registrados", font=("Arial", 14, "bold")).pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("id", "nombre", "categoria", "precio", "cantidad"),
            show="headings"
        )
        for col, titulo in [
            ("id", "ID"), ("nombre", "Nombre"), ("categoria", "Categoría"),
            ("precio", "Precio"), ("cantidad", "Cantidad")
        ]:
            tabla.heading(col, text=titulo)
            tabla.column(col, width=130)

        for p in self.servicio.listar_productos():
            tabla.insert("", "end", values=(p.id, p.nombre, p.categoria, f"${p.precio:.2f}", p.cantidad))

        tabla.pack(fill="both", expand=True)

    def mostrar_usuarios(self):
        self.limpiar()
        tk.Label(self.contenido, text="Usuarios registrados", font=("Arial", 14, "bold")).pack(pady=5)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("id", "usuario", "nombre"),
            show="headings"
        )
        for col, titulo in [("id", "ID"), ("usuario", "Usuario"), ("nombre", "Nombre")]:
            tabla.heading(col, text=titulo)
            tabla.column(col, width=180)

        for u in self.servicio.listar_usuarios():
            tabla.insert("", "end", values=(u.id, u.usuario, u.nombre))

        tabla.pack(fill="both", expand=True)

    def destruir(self):
        self.frame.destroy()
