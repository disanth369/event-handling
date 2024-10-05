from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('date handling')
root.geometry("300x400")
def msg():
    messagebox.showwarning('Alert',"virus found")
def to():
    messagebox.askokcancel('login','do you real want to login')
def a():
    messagebox.askretrycancel('changepassword','do you real want to change')
b1=Button(root,text="Scan for viruses",command=msg)
login=Button(root,text="login",command=to)
changepassword=Button(root,text="change password",command=a)
b1.pack()
login.pack()
changepassword.pack()
root.mainloop()