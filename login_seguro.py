import tkinter as tk
from tkinter import messagebox
import sqlite3

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    conn = sqlite3.connect("C:/wamp64/www/Seuguridad/users.db")
    cursor = conn.cursor()

    # CONSULTA SEGURA: Parametrizada
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (user, pwd))

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", "¡Inicio de sesión exitoso!")
    else:
        messagebox.showerror("Login", "Credenciales inválidas")

    conn.close()

root = tk.Tk()
root.title("Login Seguro")

tk.Label(root, text="Usuario:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Contraseña:").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Iniciar Sesión", command=login).pack(pady=10)

root.mainloop()
