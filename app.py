import tkinter as tk
import json
import os

DB_PATH = os.environ.get("DB_PATH", "base_datos.json")

def cargar_respuestas():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def responder():
    mensaje = entrada.get().lower()
    respuestas = cargar_respuestas()
    respuesta = respuestas.get(mensaje, respuestas["default"])
    chat.insert(tk.END, f"Tú: {mensaje}\n")
    chat.insert(tk.END, f"Bot: {respuesta}\n\n")
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Chatbot en Tkinter")

chat = tk.Text(ventana, height=20, width=50)
chat.pack()

entrada = tk.Entry(ventana, width=40)
entrada.pack()

boton = tk.Button(ventana, text="Enviar", command=responder)
boton.pack()

ventana.mainloop()