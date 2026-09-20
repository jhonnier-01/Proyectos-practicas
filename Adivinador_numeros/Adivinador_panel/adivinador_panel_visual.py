import random
import tkinter as tk
from tkinter import messagebox

numero_secreto = random.randint(1, 20)
contador = 6
intentos = 0

def verificar_adivinanza():
  global contador, intentos

  try:
    texto_usuario = entrada_numero.get()
    adivinanza = int(texto_usuario)
    intentos += 1
    contador -= 1

    if adivinanza < numero_secreto:
      label_resultado.config(text="El numero es mayor")
    elif adivinanza > numero_secreto:
      label_resultado.config(text="El numero  es menor")
    else:
      messagebox.showinfo("Ganaste we :)", f"Felicidades, adivinaste el numero {numero_secreto} en {intentos} intentos")
      ventana.destroy()
      return

    label_intentos.config(text=f"Intentos restantes: {contador}")

    if contador == 0:
      messagebox.showerror(
          "Perdiste :(", f"Se acabaron los intentos. El número era {numero_secreto}"
      )
      ventana.destroy()

  except ValueError:
    messagebox.showwarning("Error", "Ingrese un numero dentro del rango permitido (1-20)")




#configuracion de la ventana
ventana = tk.Tk()
ventana.title("El juego de la adivinanza :v")
ventana.geometry("350x250")

label_titulo = tk.Label(
    ventana, text="Adivina un número del 1 al 20", font=("Arial", 12, "bold")
)
label_titulo.pack(pady=10)

label_intentos = tk.Label(ventana, text=f"Intentos restantes: {contador}")
label_intentos.pack(pady=5)

entrada_numero = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada_numero.pack(pady=10)
entrada_numero.focus()

btn_enviar = tk.Button(
    ventana,
    text="Adivinar",
    command=verificar_adivinanza,
    bg="orange",
    fg="black",
)
btn_enviar.pack(pady=5)

label_resultado = tk.Label(
    ventana, text="Escribe un número y presiona Adivinar", fg="brown"
)
label_resultado.pack(pady=15)

ventana.mainloop()
