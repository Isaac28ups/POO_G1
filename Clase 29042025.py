import tkinter as tk

ventana = tk.Tk()

ventana.geometry("500x400")

ventana.title("Venatana tkinter")

boton= tk.Button( ventana , text="haz click aquí")
boton.pack()

marco= tk.Frame(ventana)
marco.pack()

boton1= tk.Button(marco,text="Botón 1")
boton1.pack(side=tk.LEFT)

boton2= tk.Button(marco, text="Botón 2")
boton2.pack(side=tk.RIGHT)
def click():
    
    print("POR QUÉ HACES TOCAS EL BOTÓN!?")
boton= tk.Button(ventana, text="NO PRESIONES ESTE BOTÓN", command=click)
boton.pack()

elementos= ["carro", "mesa", "gato"]
lista=tk.Listbox(ventana)
for elemento in elementos:
    lista.insert(tk.END, elemento)
lista.pack()

ventana.mainloop()
