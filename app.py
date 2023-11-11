from encryption.caesar import Caeser
import tkinter as tk

c1=Caeser(key=3)

def linker():
    a=o_win.get()
    o_win.delete(first=0,last='end')
    o_win2.delete(first=0,last='end')
    encrypted_text=c1.encrypet(text=a)
    output=(encrypted_text)
    o_win2.insert(string=output,index=0)

def linker2():
    b=o_win2.get()
    o_win.delete(first=0,last='end')
    o_win2.delete(first=0,last='end')
    decrypted_text=c1.decrypt(text=b)
    output=(decrypted_text)
    o_win.insert(string=output,index=0)

def linker3():
    o_win.delete(first=0,last='end')
    o_win2.delete(first=0,last='end')

gui=tk.Tk()
gui.title('Caeser')
gui.geometry("470x250")
gui.resizable(0,0)

o_win=tk.Entry(gui,font=('arial', '15'),width=40,borderwidth=4)
o_win.place(x=5,y=40)
o_win2=tk.Entry(gui,font=('arial', '15'),width=40,borderwidth=4)
o_win2.place(x=5,y=130)

l1=tk.Label(gui,text='origonal:',font=('Times New Roman', 20, 'bold'))
l1.place(x=5,y=0)
l2=tk.Label(gui,text='encrypted:',font=('Times New Roman', 20, 'bold'))
l2.place(x=5,y=80)

b0=tk.Button(gui,text='encrypt',bg='grey',borderwidth=3,font=('Times New Roman', 20, 'bold'),width=10,height=1,command=linker)
b0.place(x=5,y=180)
b1=tk.Button(gui,text='decrypt',bg='grey',borderwidth=3,font=('Times New Roman', 20, 'bold'),width=10,height=1,command=linker2)
b1.place(x=265,y=180)
b2=tk.Button(gui,text='clc',bg='grey',borderwidth=3,font=('Times New Roman', 20, 'bold'),width=5,height=1,command=linker3)
b2.place(x=175,y=180)

gui.mainloop()