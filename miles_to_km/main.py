from tkinter import *


def convert():
    mile = mile_value.get()
    km = round(float(mile)*1.609,2)
    value.config(text=str(km))






window = Tk()
window.title("Miles to kms converter")

mile_value = Entry(width= 7)
mile_value.grid(row=0,column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)

l = Label(text="is equal to")
l.grid(row=1,column=0)

value = Label(text="0")
value.grid(row=1,column=1)

km_label = Label(text="Km")
km_label.grid(row=1,column=2)

calc = Button(text="Calculate", command=convert)
calc.grid(row=2,column=1)



window.mainloop()