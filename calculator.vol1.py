from tkinter import *

base = Tk()
base.title("calculator.vol1")

entry = Entry(base,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#operations
def button_click(number):
    cur_num = entry.get()
    entry.delete(0,END) 
    entry.insert(0,str(cur_num) +str(number)) 
    
def clear():
    entry.delete(0,END)

def add():
    x = entry.get()
    global first_num # global just to avoid passing any variable to button_equal()
    global sign 
    sign = "+"
    first_num = int(x)
    entry.delete(0,END)
    
def subtract():
    x = entry.get()
    global first_num 
    global sign 
    sign = "-"
    first_num = int(x)
    entry.delete(0,END)
    
def divide():
    x = entry.get()
    global first_num 
    global sign 
    sign = "/"
    first_num = int(x)
    entry.delete(0,END)
    
def multiply():
    x = entry.get()
    global first_num 
    global sign 
    sign = "x"
    first_num = int(x)
    entry.delete(0,END)
    
def equal():
    second_num = entry.get()
    entry.delete(0,END)
    if(sign == "+"):
        entry.insert(0,f"result : {first_num+int(second_num)}") 
    elif(sign == "-"):
        entry.insert(0,f"result : {first_num-int(second_num)}")
    elif(sign == "x"):
        entry.insert(0,f"result : {first_num*int(second_num)}")
    elif(sign == "/"):
        entry.insert(0,f"result : {first_num//int(second_num)}")
        
#setting new buttons
button_1 =Button(base,text="1", padx=40,pady=20,command=lambda:button_click(1))    
button_2 =Button(base,text="2", padx=40,pady=20,command=lambda:button_click(2))    
button_3 =Button(base,text="3", padx=40,pady=20,command=lambda:button_click(3))    
button_4 =Button(base,text="4", padx=40,pady=20,command=lambda:button_click(4))    
button_5 =Button(base,text="5", padx=40,pady=20,command=lambda:button_click(5))    
button_6 =Button(base,text="6", padx=40,pady=20,command=lambda:button_click(6))    
button_7 =Button(base,text="7", padx=40,pady=20,command=lambda:button_click(7))    
button_8 =Button(base,text="8", padx=40,pady=20,command=lambda:button_click(8))    
button_9 =Button(base,text="9", padx=40,pady=20,command=lambda:button_click(9)) 
button_0 =Button(base,text="0", padx=40,pady=20,command=lambda:button_click(0))    
   

#filling the buttons in the window
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)

#special buttons
button_add = Button(base, text="+",padx=39,pady=20,command= add)
button_add.grid(row=5,column=0)

button_equal = Button(base, text="=",padx=86.49,pady=20,command=equal)
button_equal.grid(row=5,column=1,columnspan=2)

button_clear = Button(base, text="clear",padx=78.4,pady=20,command=clear)
button_clear.grid(row=4,column=1, columnspan=2)

button_div = Button(base, text="/",padx=40,pady=20,command=divide)
button_div.grid(row=6,column=0)

button_sub = Button(base, text="-",padx=40,pady=20,command=subtract)
button_sub.grid(row=6,column=1)

button_mul = Button(base, text="x",padx=40,pady=20,command=multiply)
button_mul.grid(row=6,column=2)

#starting the event
base.mainloop()