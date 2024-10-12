from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('denomination calculator')
root.geometry("500x500")
root.configure(bg="blue")
label1=Label(root,text='welcome to denamination counter calculator',bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    print('hi')
    MsBox= messagebox.showinfo("alert","do you want to calculate the denomination count")
    if MsBox =="ok":
        topwin()
button1 =Button(root,text="let's get started",command=msg,bg='brown',fg='white')
button1.place(x=500,y=650)
def topwin():
    top=Toplevel()
    top.title('denomination calculator')
    top.geometry("600x350+50+50")
    top.configure(bg="blue")
    label =Label(top,text="enter total amount",bg='light grey')
    entry=Entry(top)
    lbl =Label(top,text='here are number of notes for each denomination')
    l1 =Label(top,text="2000",bg='light grey')
    l2 =Label(top,text="500",bg='light grey')
    l3 =Label(top,text="100",bg='light grey')
    t1=Entry(top)
    t2=Entry(top) 
    t3=Entry(top)
    def calculation():
        try:
            global amount
            amount=int(entry.get())
            note2000 =amount // 2000
            amount %= 2000
            note500 =amount // 500
            amount %= 500
            note100 =amount // 100
            amount %= 100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror('error','Please enter a valid number')
        btn = Button(top, text='calculate',command=calculation,bg='brown',fg='blue')
        label.place(x=230,y=50)
        entry.place(x=200,y=80) 
        btn.place(x=240,y=120)
        lbl.place(x=140,y=170)
        l1.place(x=180,y=200) 
        l2.place(x=180,y=230)
        l3.place(x=180,y=260)
        t1.place(x=270,y=200) 
        t2.place(x=270,y=230)
        t3.place(x=270,y=260)
    top.mainloop()        

                   
root.mainloop()