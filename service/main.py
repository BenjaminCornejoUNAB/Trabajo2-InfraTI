import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as popup
from api_data import catchTracker as buscar
from PIL import ImageTk, Image
import random

def cuentaTrackers():
  t = buscar()
  cantidad = len(t)
  popup.showinfo("DuckDuckBot Anti-Tracking", "Se bloquearon {} rastreadores al realizar la busqueda.\n\n----------Rastreadores----------\n{}".format(cantidad,t))

class WebPage(tk.Tk):
  
  def __init__(self):
    tk.Tk.__init__(self)
    self._frame = None
    self.title("Demo DuckDuckGo")
    self.config(bg="#1C1C1C", width=1024, height=600)
    self.resizable(0,0)
    self.cambiaPag(Inicio, None)
    

  def cambiaPag(self, frame_class, busqueda):
    nuevo_frame = frame_class(self, busqueda)
    if self._frame is not None:
      self._frame.destroy()
    self._frame = nuevo_frame
    self._frame.pack()

#---Página Principal---#
class Inicio(tk.Frame):

  def __init__(self, master, _):
    tk.Frame.__init__(self, master)
    self.logo = ImageTk.PhotoImage(Image.open("LogoPag.jpg").resize((300,260), Image.Resampling.LANCZOS))
    self.config(bg="#1C1C1C", width=1024, height=600)

    superior = ttk.Label(self, text="La privacidad es lo más importante :)", background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 14))
    superior.place(x=700, y=10)

    
    foto = tk.Label(self, text="", image=self.logo, compound="top")
    foto.config(height=255, width=250)
    foto.place(relx=0.39, rely=0.2)


    texto_busqueda = tk.StringVar(self)
    buscar = ttk.Entry(textvariable=texto_busqueda)
    buscar.place(in_=self, relx=0.25, rely=0.65, width=500, height=48)
    

    go = tk.Button(self, text="GO", command= lambda: master.cambiaPag(Resultados, texto_busqueda.get()))
    go.config(bg="#B81919", foreground="#FFFFFF")
    go.place(relx=0.74, rely=0.65, height=48)

    inferior = ttk.Label(self, text="La privacidad es lo más importante. ¡Ayudanos a difundirlo!", background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 14))
    inferior.place(in_=self, relx=0.25, rely=0.75)

#---Pagina para mostrar resultados---#
class Resultados(tk.Frame):
  def __init__(self, master, busqueda):
    tk.Frame.__init__(self, master)
    self.config(bg="#1C1C1C", width=1024, height=600)
    self.logo = ImageTk.PhotoImage(Image.open("LogoPag.jpg").resize((70,70), Image.Resampling.LANCZOS))
    self.molesto = random.randint(1,30)

    scroll = tk.Scrollbar(self)
    scroll.place(relx=0.9825, relheight=1)

    foto = tk.Label(self, text="", image=self.logo, compound="top")
    foto.config(height=66, width=66)
    foto.place(relx=0.08, rely=0.008)

    tk.Label(self, text="Resultados de busqueda", background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 12)).place(relx=0.15, rely=0.1)
    tk.Label(self, text="* {} páginas/publicidades molestas bloqueadas.".format(self.molesto), background="#1C1C1C", foreground="#FFFFFF", font=('Aileron', 8)).place(relx=0.73, rely=0.02)

    texto_busqueda = tk.StringVar(self)
    buscar = ttk.Entry(textvariable=texto_busqueda)
    buscar.insert(0,busqueda)
    buscar.place(in_=self, relx=0.15, rely=0.01, width=550, height=44)
    
    go = tk.Button(self, text="GO", command= lambda: master.cambiaPag(Resultados, texto_busqueda.get()))
    go.config(bg="#B81919", foreground="#FFFFFF")
    go.place(relx=0.69, rely=0.01, height=45)

    volver = tk.Button(self, text="Volver", command= lambda: master.cambiaPag(Inicio, None))
    volver.config(bg="#B81919", foreground="#FFFFFF")
    volver.place(relx=0.025, rely=0.03)

    encontrados = tk.Frame(self, background="#1C1C1C", width=800, height=500)
    encontrados.place(relx=0.1, rely=0.15)

    texto_relleno = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lectus nulla at volutpat diam. Porttitor massa id neque aliquam vestibulum morbi. Lacus viverra vitae congue eu consequat ac felis. Mauris augue neque gravida in fermentum et sollicitudin ac orci. Porta nibh venenatis cras sed felis eget velit aliquet. Nunc mattis enim ut tellus. Et netus et malesuada fames ac turpis. Quis enim lobortis scelerisque."
    link1 = "Página encontrada para {} 1".format(busqueda)
    resultado = tk.Label(encontrados, text=link1, bg="#1C1C1C", foreground="#FFFFFF", cursor="hand2", font=('Aileron', 14))
    resultado.grid(row=0,column=0, sticky="N"+"W")
    resultado.bind("<Button-1>", lambda e: cuentaTrackers())
    info1 = tk.Text(encontrados, height=5, width=80, font=('Aileron', 10), bg="#1C1C1C", foreground="#C1C1C1", border=0)
    info1.insert(tk.END, texto_relleno)
    info1.grid(row=1,column=0)

    link2 = "Otra página encontrada para {} 2".format(busqueda)
    resultado = tk.Label(encontrados, text=link2, bg="#1C1C1C", foreground="#FFFFFF", cursor="hand2", font=('Aileron', 14))
    resultado.grid(row=2,column=0, sticky="N"+"W")
    resultado.bind("<Button-1>", lambda e: cuentaTrackers())
    info2 = tk.Text(encontrados, height=5, width=80, font=('Aileron', 10), bg="#1C1C1C", foreground="#C1C1C1", border=0)
    info2.insert(tk.END, texto_relleno)
    info2.grid(row=3,column=0)

    link3 = "Página de {} N°3".format(busqueda)
    resultado = tk.Label(encontrados, text=link3, bg="#1C1C1C", foreground="#FFFFFF", cursor="hand2", font=('Aileron', 14))
    resultado.grid(row=4,column=0, sticky="N"+"W")
    resultado.bind("<Button-1>", lambda e: cuentaTrackers())
    info3 = tk.Text(encontrados, height=5, width=80, font=('Aileron', 10), bg="#1C1C1C", foreground="#C1C1C1", border=0)
    info3.insert(tk.END, texto_relleno)
    info3.grid(row=5,column=0)

    link4 = "{} - Página de noticias 4".format(busqueda)
    resultado = tk.Label(encontrados, text=link4, bg="#1C1C1C", foreground="#FFFFFF", cursor="hand2", font=('Aileron', 14))
    resultado.grid(row=6,column=0, sticky="N"+"W")
    resultado.bind("<Button-1>", lambda e: cuentaTrackers())
    info4 = tk.Text(encontrados, height=5, width=80, font=('Aileron', 10), bg="#1C1C1C", foreground="#C1C1C1", border=0)
    info4.insert(tk.END, texto_relleno)
    info4.grid(row=7,column=0)
if __name__ == "__main__":
  app = WebPage()
  app.mainloop()