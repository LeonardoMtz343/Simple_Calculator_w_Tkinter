import math
from tkinter import *

root=Tk()
root.title("Simple calculator by Leonardo Martinez")

e = Entry(root, width=65,borderwidth=5)
e.grid(row=0,column=0, columnspan=4, padx=10, pady=10)


#Create a function that run inside the button
def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global first_num
    global math
    math = 'addition'
    first_num = float(first_number)
    e.delete(0, END)
    
def button_substract():
    first_number = e.get()
    global first_num
    global math
    math = 'substraction'
    first_num = float(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()
    global first_num
    global math
    math = 'multiplication'
    first_num = float(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global first_num
    global math
    math = 'division'
    first_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == 'addition':
        e.insert(0, first_num + float(second_number))

    elif math == 'substraction':
        e.insert(0, first_num - float(second_number))

    elif math == 'multiplication':
        e.insert(0, first_num * float(second_number))

    elif math == 'division':
        e.insert(0, float(first_num) / float(second_number))




#create buttons numbers
button_9 = Button(root, text = '9', padx=40,pady=20, command=lambda: button_click(9)).grid(row=1,column=2, columnspan=1, padx=10, pady=10)
button_8 = Button(root, text = '8', padx=40,pady=20, command=lambda: button_click(8)).grid(row=1,column=1, columnspan=1, padx=10, pady=10)
button_7 = Button(root, text = '7', padx=40,pady=20, command=lambda: button_click(7)).grid(row=1,column=0, columnspan=1, padx=10, pady=10)
button_6 = Button(root, text = '6', padx=40,pady=20, command=lambda: button_click(6)).grid(row=2,column=2, columnspan=1, padx=10, pady=10)
button_5 = Button(root, text = '5', padx=40,pady=20, command=lambda: button_click(5)).grid(row=2,column=1, columnspan=1, padx=10, pady=10)
button_4 = Button(root, text = '4', padx=40,pady=20, command=lambda: button_click(4)).grid(row=2,column=0, columnspan=1, padx=10, pady=10)
button_3 = Button(root, text = '3', padx=40,pady=20, command=lambda: button_click(3)).grid(row=3,column=2, columnspan=1, padx=10, pady=10)
button_2 = Button(root, text = '2', padx=40,pady=20, command=lambda: button_click(2)).grid(row=3,column=1, columnspan=1, padx=10, pady=10)
button_1 = Button(root, text = '1', padx=40,pady=20, command=lambda: button_click(1)).grid(row=3,column=0, columnspan=1, padx=10, pady=10)
button_0 = Button(root, text = '0', padx=40,pady=20, command=lambda: button_click(0)).grid(row=4,column=1, columnspan=1, padx=10, pady=10)
button_point = Button(root, text = '.', padx=40,pady=20, command=lambda: button_click('.')).grid(row=4,column=2, columnspan=1, padx=10, pady=10)
button_Clear = Button(root, text = 'Clear', padx=40,pady=20, command=button_clear).grid(row=4,column=0, columnspan=1, padx=10, pady=10)


# Create basic math operation button
button_ad = Button(root, text = '+', padx=40,pady=20, command=button_add).grid(row=4,column=3, columnspan=1, padx=10, pady=10)
button_sub = Button(root, text = '-', padx=40,pady=20, command=button_substract).grid(row=3,column=3, columnspan=1, padx=10, pady=10)
button_multi = Button(root, text = 'x', padx=40,pady=20, command=button_multiplication).grid(row=2,column=3, columnspan=1, padx=10, pady=10)
button_div = Button(root, text = '/', padx=40,pady=20, command=button_division).grid(row=1,column=3, columnspan=1, padx=10, pady=10)
button_eqqual = Button(root, text = '=', padx=200,pady=20, command= button_equal).grid(row=5, columnspan=4, padx=10, pady=10)
root.mainloop()
