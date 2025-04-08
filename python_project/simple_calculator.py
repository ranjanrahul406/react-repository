from tkinter import*

root = Tk()

e = Entry(root, width= 50)
e.grid(row= 0, column= 0, columnspan= 4, padx= 10, pady= 10)

def button_click(number):
   current = e.get()
   e.delete(0,END)
   e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0,END)
    
def button_add():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
    
def button_equal():
    second_num = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_num))
    
# I'm defining buttons of digits below-

button_1 = Button(root, text="1", padx= 25, pady= 15, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx= 25, pady= 15, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx= 25, pady= 15, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx= 25, pady= 15, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx= 25, pady= 15, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx= 25, pady= 15, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx= 25, pady= 15, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx= 25, pady= 15, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx= 25, pady= 15, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx= 25, pady= 15, command= lambda: button_click(0))

# Defining buttons of arithmetic symbols and other functions -

button_add = Button(root, text="+", padx= 30, pady= 20, command= button_add)
button_sub = Button(root, text="-", padx= 30, pady= 20, command= button_click)
button_mul = Button(root, text="X", padx= 25, pady= 20, command= button_click)
button_div = Button(root, text="/", padx= 25, pady= 20, command= button_click)

button_per = Button(root, text="%", padx= 23, pady= 15, command= button_click)
button_dot = Button(root, text=".", padx= 27, pady= 15, command= button_click)

button_equal = Button(root, text="=", padx= 25, pady= 40, fg="white", bg="#6699cc", command= button_equal)
button_clear = Button(root, text="Clear", padx= 15, pady= 18, bg="#ff6a00", command= button_clear)
button_backspace = Button(root, text="<-", padx= 25, pady= 20, command= button_click)

# to put the buttons on the screen-

button_clear.grid(row=1, column=0)
button_div.grid(row=1, column=1)
button_mul.grid(row=1, column=2)
button_backspace.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_per.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)

button_equal.grid(row=4, column=3, rowspan= 2)


root.mainloop()