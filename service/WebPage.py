import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as popup
from api_data import catchTracker as buscar
from PIL import ImageTk, Image

def cuentaTrackers():
  t = buscar()
  cantidad = len(t)
  popup.showinfo("DuckDuckBot Anti-Tracking", "Se bloquearon {} rastreadores al realizar la busqueda.\n\n----------Rastreadores----------\n{}".format(cantidad,t))

def PagWeb():

  ventana = tk.Tk()

  ventana.title("Demo DuckDuckGo")
  ventana.config(bg="#1C1C1C", width=1024, height=600)
  ventana.resizable(0,0)

  frame = tk.Frame(ventana, width=100, height=100)
  frame.pack()
  frame.place(anchor='center', relx=0.5, rely=0.4)

  superior = ttk.Label(text="La privacidad es lo más importante :)", background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 14))
  superior.place(x=700, y=10)

  logo = ImageTk.PhotoImage(Image.open("Trabajo2-InfraTI\service\LogoPag.jpg").resize((300,260), Image.Resampling.LANCZOS))
  foto = tk.Label(frame, image=logo)
  foto.pack()

  busqueda = ttk.Entry()
  busqueda.place(in_=ventana, relx=0.25, rely=0.65, width=500, height=48)

  go = ttk.Button(text="GO", command=cuentaTrackers)
  go.place(in_=ventana, relx=0.74, rely=0.65, height=48)

  inferior = ttk.Label(text="La privacidad es lo más importante. ¡Ayudanos a difundirlo!", background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 14))
  inferior.place(in_=ventana, relx=0.25, rely=0.75)

  fin = ventana.mainloop()
  return fin