from tkinter import *

root = Tk()

'''#create a label widget
myLabel1 = Label(root, text = 'Hello world!').grid(row=0,column=0)
mylabel2 = Label(root, text = 'Secon hello world').grid(row=1,column=0)
mylabel3 = Label(root, text = 'Secon hello world').grid(row=2,column=0)
mylabel4 = Label(root, text = 'Secon hello world').grid(row=3,column=0)
mylabel5 = Label(root, text = 'Secon hello world').grid(row=4,column=0)
'''

'''#Create a function where you put whatever you want to do inside the button
def myClick():
    myLabel1 = Label(root, text = 'You Click the button!!').pack()

#Create a button
mybutton = Button(root, text='Click me!', padx=50,pady=50, command= myClick, fg= "blue", background= 'green').pack()
'''




root.mainloop()