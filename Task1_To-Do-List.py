from tkinter import *

win=Tk()
win.geometry("500x550+0+0")
win.resizable(False,False)
win.title("TO DO APPLICAION")
ico = PhotoImage(file='todo-list.png')

win.iconphoto(False,ico)

def additem(event):
    global val 
    val=inputvar.get()
    if (val==""):
        pass
    else:
        lbx.insert(END,f"{val}")
    inputvar.set("")
    inputfield.update()

def updateitem(event):
    update_index=lbx.curselection()
    if update_index:
        edit_item=inputvar.get()
        lbx.delete(update_index[0])
        lbx.insert(update_index[0],edit_item)
    inputvar.set("")
    inputfield.update()

def deleteitem(event):
    delete_item=lbx.curselection()
    if delete_item:
        lbx.delete(ACTIVE)
    inputvar.set("")
    inputfield.update()

inputvar=StringVar()

inputfield=Entry(width=40,textvariable=inputvar,font=("times new roman",12),relief=RIDGE,borderwidth=2)
inputfield.place(x=70,y=40,height=40)

add=Button(text="ADD",font=("times new roman",13,"bold"),relief=RAISED,
           borderwidth=5,bg="green",fg="white")
add.place(x=25,y=110)
add.bind("<Button-1>",additem)

delete=Button(text="DELETE",font=("times new roman",13,"bold"),relief=RAISED,
           borderwidth=5,bg="navy blue",fg="white")
delete.place(x=205,y=110)
delete.bind("<Button-1>",deleteitem)

update=Button(text="UPDATE",font=("times new roman",13,"bold"),relief=RAISED,
           borderwidth=5,bg="purple",fg="white")
update.place(x=385,y=110)
update.bind("<Button-1>",updateitem)

scroll=Scrollbar(win)
scroll.pack(side=RIGHT,fill=Y)

lbx=Listbox(win,borderwidth=2,yscrollcommand=scroll.set)
lbx.place(x=0,y=200,width=480,height=330)

scroll.config(command=lbx.yview)




win.mainloop()

