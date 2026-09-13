import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, root, servicio, on_login):
        self.root = root
        self.servicio = servicio
        self.on_login = on_login
        self.frame = tk.Frame(root, padx=30, pady=30)
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="RESTAURANTE APP", font=("Arial", 20, "bold")).pack(pady=(0, 20))
        tk.Label(self.frame, text="Usuario").pack(anchor="w")
        self.usuario_entry = tk.Entry(self.frame, width=30)
        self.usuario_entry.pack(pady=(0, 10))

        tk.Label(self.frame, text="Contraseña").pack(anchor="w")
        self.contrasena_entry = tk.Entry(self.frame, width=30, show="*")
        self.contrasena_entry.pack(pady=(0, 15))

        tk.Button(self.frame, text="Ingresar", width=20, command=self.ingresar).pack()
        self.contrasena_entry.bind("<Return>", lambda event: self.ingresar())

    def ingresar(self):
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get()

        if not usuario or not contrasena:
            messagebox.showwarning("Acceso", "Ingrese usuario y contraseña.")
            return

        if self.servicio.validar_acceso(usuario, contrasena):
            self.on_login()
        else:
            messagebox.showerror("Acceso", "Usuario o contraseña incorrectos.")

    def destruir(self):
        self.frame.destroy()
