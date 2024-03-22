# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=100)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root,width=700,height=200,padding=100)
frm.grid()
ttk.Label(frm,text="hello").grid(row=0,column=4)
ttk.Button(frm,text="exit",command=root.destroy).grid(row=1,column=0)
ttk.Entry(frm).grid(row=2,column=2)
ttk.Scale(frm,from_=0,to=10).grid(row=3,column=3)
# print(Button.configure().keys())


root.mainloop()