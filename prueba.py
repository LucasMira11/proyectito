import tkinter as tk
from tkinter import messagebox
import webbrowser

# -------------------------------------------------
# Función para abrir WhatsApp con mensaje listo
# -------------------------------------------------
def enviar_mensaje(numero, mensaje):
    mensaje_url = mensaje.replace(" ", "%20")
    url = f"https://wa.me/{numero}?text={mensaje_url}"
    webbrowser.open(url)

# -------------------------------------------------
# Enviar mensaje al contacto elegido
# -------------------------------------------------
def enviar_individual():
    seleccionado = lista_contactos.curselection()
    if not seleccionado:
        messagebox.showerror("Error", "Selecciona un contacto")
        return

    nombre = lista_contactos.get(seleccionado)
    numero = contactos[nombre]

    mensaje = caja_mensaje.get("1.0", tk.END).strip()
    if not mensaje:
        messagebox.showerror("Error", "El mensaje está vacío")
        return

    enviar_mensaje(numero, mensaje)
    messagebox.showinfo("Listo", f"Se abrió WhatsApp para enviar mensaje a {nombre}.")

# -------------------------------------------------
# Enviar mensaje a TODOS los contactos
# -------------------------------------------------
def enviar_todos():
    mensaje = caja_mensaje.get("1.0", tk.END).strip()
    if not mensaje:
        messagebox.showerror("Error", "El mensaje está vacío")
        return

    for nombre, numero in contactos.items():
        enviar_mensaje(numero, mensaje)

    messagebox.showinfo("Listo", "Se abrió WhatsApp para todos los contactos.")

# -------------------------------------------------
# Copiar mensaje al portapapeles
# -------------------------------------------------
def copiar_mensaje():
    mensaje = caja_mensaje.get("1.0", tk.END).strip()
    ventana.clipboard_clear()
    ventana.clipboard_append(mensaje)
    messagebox.showinfo("Copiado", "Mensaje copiado al portapapeles.")

# -------------------------------------------------
# Insertar mensajes rápidos
# -------------------------------------------------
def insertar_mensaje_rapido(texto):
    caja_mensaje.delete("1.0", tk.END)
    caja_mensaje.insert(tk.END, texto)

# -------------------------------------------------
# Lista de contactos
# (Podés agregar más)
# -------------------------------------------------
contactos = {
    "lucas": "5491122607124"
    
}

# -------------------------------------------------
# Interfaz gráfica
# -------------------------------------------------
ventana = tk.Tk()
ventana.title("WhatsApp Sender PRO")
ventana.geometry("600x400")
ventana.config(bg="#222222")

# ---- Listbox de contactos ----
tk.Label(ventana, text="Contactos:", fg="white", bg="#222222").place(x=20, y=10)
lista_contactos = tk.Listbox(ventana, height=8, width=25)
lista_contactos.place(x=20, y=40)

for nombre in contactos:
    lista_contactos.insert(tk.END, nombre)

# ---- Caja de mensaje ----
tk.Label(ventana, text="Mensaje:", fg="white", bg="#222222").place(x=250, y=10)
caja_mensaje = tk.Text(ventana, width=40, height=8)
caja_mensaje.place(x=250, y=40)

# ---- Botones de acción ----
btn_enviar = tk.Button(ventana, text="Enviar al contacto", width=20, command=enviar_individual)
btn_enviar.place(x=20, y=220)

btn_todos = tk.Button(ventana, text="Enviar a TODOS", width=20, command=enviar_todos)
btn_todos.place(x=20, y=260)

btn_copiar = tk.Button(ventana, text="Copiar mensaje", width=20, command=copiar_mensaje)
btn_copiar.place(x=20, y=300)

# ---- Mensajes predefinidos ----
tk.Label(ventana, text="Mensajes rápidos:", fg="white", bg="#222222").place(x=250, y=220)

btn_m1 = tk.Button(ventana, text="Hola, ¿cómo estás?", width=20,
                   command=lambda: insertar_mensaje_rapido("Hola, ¿cómo estás?"))
btn_m1.place(x=250, y=250)

btn_m2 = tk.Button(ventana, text="¿Podemos hablar?", width=20,
                   command=lambda: insertar_mensaje_rapido("¿Podemos hablar?"))
btn_m2.place(x=250, y=280)

btn_m3 = tk.Button(ventana, text="¡Buenas! Te quiero comentar algo...", width=25,
                   command=lambda: insertar_mensaje_rapido("¡Buenas! Te quiero comentar algo..."))
btn_m3.place(x=250, y=310)

ventana.mainloop()

# Ejecutar app
root = tk.Tk()
app = AppEnvioMasivo(root)
root.mainloop()
