import math
from tkinter import *
import tkinter
from tkmacosx import Button
import tkinter.messagebox

def caluculate():
    if sample.get()== 1 and population.get()==1:
        c2.deselect()
    elif sample.get()==0 and population.get()==0 and E1.get():
        c1.select()
    if E1.get().count(",") > 0:
        data = E1.get().split(",")
    elif E1.get().count(" ") > 0:
        data = E1.get().split(" ")
    else:
        if E1.get() != "":
         tkinter.messagebox.showerror("Error","please seperate the numbers wih ','")
        else:
         tkinter.messagebox.showerror("Error!!","Need data to caluculate ex:1,2,3,4")
        return
    if sample.get() == 1:
      data = [int(num) for num in data]
      mean = sum(data)/len(data)
      variance = sum([(num-mean)**2 for num in data])/(len(data)-1)
      sd = math.sqrt(variance)
      variance_var.set("Variance:"+str(variance))
      std_var.set("Standard Deviation:"+str(sd))
    elif population.get() == 1:
      data = [int(num) for num in data]
      mean = sum(data)/len(data)
      variance = sum([(num-mean)**2 for num in data])/(len(data))
      sd = math.sqrt(variance)
      variance_var.set("Variance:"+str(variance))
      std_var.set("Standard Deviation:"+str(sd))

window = tkinter.Tk()
window.title("Variance Caluculator")
sample = IntVar()
population = IntVar()
E1 =Entry(window,bd=5)
L1 = Label(window,text="Enter Data-")
btn = Button(window,text="caluculate",command=caluculate,bg="black",fg="white")
c1 = Checkbutton(window,text="population",variable=population,onvalue=1,offvalue=0,height=5,width=10)
c2 = Checkbutton(window,text="sample",variable=sample,onvalue=1,offvalue=0,height=5,width=10)
variance_var = StringVar()
variance_var.set("Variance:0.0")
std_var = StringVar()
std_var.set("Standard Deviation:0.0")
res = Label(window,text="Result-")
var = Label(window,textvariable=variance_var,relief=RAISED)
std = Label(window,textvariable=std_var,relief=RAISED)
L1.pack()
E1.pack()
c1.pack(side=LEFT,pady=90,padx=30)
c2.pack(side=RIGHT,padx=30,pady=90)
btn.pack(side=BOTTOM,pady=30)
var.pack(side=BOTTOM,pady=20)
std.pack(side=BOTTOM)
window.mainloop()