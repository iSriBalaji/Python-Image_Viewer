from PIL import ImageTk
import PIL.Image as pl     
from tkinter import *
root=Tk()



def fun(n):
    global forward      
    global back                      
    global img_label
    
    pass

def bac(n):
    global forward  
    global back                      
    global img_label
    




i1=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img1.png"))
i2=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img2.png"))
i3=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img3.png"))
i4=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img4.png"))
i5=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img5.png"))
i6=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img6.png"))
i7=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img7.png"))
i8=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img8.png"))
i9=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img9.png"))
i10=ImageTk.PhotoImage(pl.open(r"C:\Users\Sri Balaji\Desktop\Sri Tut\Baju_Tkinter\Image Viewer\img10.png"))

ls=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]

img_label=Label(root,image=ls[0],padx=5,pady=5)
img_label.grid(row=1,column=0,columnspan=3)

forward=Button(root,text=">>",command=lambda:fun(1))
back=Button(root,text="<<",state=DISABLED)
exbutton=Button(root,text="Exit",command=root.quit)

img_no=Label(root,text="1/10")
img_no.grid(row=2,column=1)

forward.grid(row=2,column=2)
back.grid(row=2,column=0)
exbutton.grid(row=3,column=1)






root.mainloop()
