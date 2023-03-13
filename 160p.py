from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root=Tk()
root.minsize(650,650)
root.maxsize(1000,1000)
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
root.configure(background="violet")
l=Label(root,text="file name")
def Openfile():
    print("hello")
l.place(relx=0.28,rely=0.03,anchor=CENTER)
e=Entry(root)
e.place(relx=0.48,rely=0.03,anchor=CENTER)
mt=Text(root,height=35,width=80)
mt.place(relx=.5,rely=0.55,anchor=CENTER)
def openfile():
    global name
    mt.delete(1.0,END)
    e.delete(0,END)
    tf=filedialog.askopenfilename(title="Text Open File",filetypes=(("Text Files","*.txt"),))
    print(tf)
    name=os.path.basename(tf)
    fn=name.split('.')[0]
    ifn.insert(END,fn)
    root.title(fn)
    tf=open(name,'r')
    paragraph=tf.read()
    mt.insert(END,paragraph)
    tf.close()
ob=Button(root,image=open_img,text="openfile",command=openfile)
ob.place(relx=0.05,rely=0.03,anchor=CENTER)

root.mainloop()

