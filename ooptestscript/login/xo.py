import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

window = tk.Tk()
window.geometry('240x258')
window.title(" ")

y = 0
count = 0 
win = False

def  disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"
    button4["state"] = "disable"
    button5["state"] = "disable"
    button6["state"] = "disable"
    button7["state"] = "disable"
    button8["state"] = "disable"
    button9["state"] = "disable"

def check():
    global win
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" :
        messagebox.showinfo("winner", "X win!!")
        win = True
        disable()
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" :
        messagebox.showinfo("winner", "O win!!")
        win = True
        disable()


def clicked(x):
    global count
    global y
    global win
    if y == 0:
        x.configure(state = 'disable',text = "X")
        y += 1
    else:
        x.configure(state = 'disable',text = "O")
        y -= 1
    if count >= 4:
        check()
    if count == 8 and win == False:
        messagebox.showinfo(" ", "TIE")
    count = count + 1

button1 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button1)
    )  
button2 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button2)
    )
button3 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button3)
    )  
button4 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button4)
    )  
button5 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button5)
    )  
button6 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button6)
    )  
button7 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button7)
    )  
button8 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button8)
    )  
button9 = tk.Button(
    width=10,
    height=5,
    command= lambda :clicked(button9)
    )  

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=2, row=0)
button4.grid(column=0, row=1)
button5.grid(column=1, row=1)
button6.grid(column=2, row=1)
button7.grid(column=0, row=2)
button8.grid(column=1, row=2)
button9.grid(column=2, row=2)

window.mainloop()