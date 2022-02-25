from tkinter import *

root = Tk()

#Crear una caja para ingresar texto
e= Entry(root, width=50, background= "red", borderwidth= 6)
e.pack()
# Poner una leyenda dentro de la caja de ingreso de texto
e.insert(0, "Escribe lo que quieras")

#guardar lo que escribimos con e.get()
def myClick():
    myLabel1 = Label(root, text = f'HEllo {e.get()}').pack()

#Create a button
mybutton = Button(root, text='Click me!', padx=50,pady=50, command= myClick, fg= "blue", background= 'green').pack()



root.mainloop()