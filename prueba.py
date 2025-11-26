import tkinter as tk
from tkinter import messagebox, simpledialog

class AppEnvioMasivo:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Envío Masivo")
        self.root.geometry("450x420")
        
        self.destinatarios = []

        # Título
        tk.Label(root, text="Simulador de Envío Masivo", font=("Arial", 16, "bold")).pack(pady=10)

        # Campo mensaje
        tk.Label(root, text="Mensaje a enviar:").pack()
        self.texto_mensaje = tk.Text(root, height=5, width=50)
        self.texto_mensaje.pack()

        # Lista destinatarios
        tk.Label(root, text="Destinatarios:").pack(pady=5)
        self.lista = tk.Listbox(root, width=50, height=8)
        self.lista.pack()

        # Botones
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Agregar destinatario", command=self.agregar_destinatario).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Eliminar seleccionado", command=self.eliminar_destinatario).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Enviar a todos", command=self.enviar).grid(row=0, column=2, padx=5)

        tk.Button(root, text="Ver historial", command=self.ver_historial, width=20).pack(pady=5)

        self.historial = []

    def agregar_destinatario(self):
        nuevo = simpledialog.askstring("Nuevo destinatario", "Ingresa un nombre o usuario:")
        if nuevo:
            self.destinatarios.append(nuevo)
            self.lista.insert(tk.END, nuevo)

    def eliminar_destinatario(self):
        sel = self.lista.curselection()
        if sel:
            idx = sel[0]
            self.lista.delete(idx)
            del self.destinatarios[idx]

    def enviar(self):
        mensaje = self.texto_mensaje.get("1.0", tk.END).strip()
        if not mensaje:
            messagebox.showwarning("Advertencia", "El mensaje está vacío.")
            return
        
        if not self.destinatarios:
            messagebox.showwarning("Advertencia", "No hay destinatarios.")
            return

        resultado = "=== ENVÍO MASIVO SIMULADO ===\n"
        for d in self.destinatarios:
            resultado += f"Mensaje enviado a {d}\n"

        self.historial.append(resultado)

        messagebox.showinfo("Resultado", f"Se enviaron {len(self.destinatarios)} mensajes (simulación).")

    def ver_historial(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Historial de envíos")
        ventana.geometry("400x300")

        text = tk.Text(ventana)
        text.pack(expand=True, fill="both")

        for item in self.historial:
            text.insert(tk.END, item + "\n")


# Ejecutar app
root = tk.Tk()
app = AppEnvioMasivo(root)
root.mainloop()
