from tkinter import *
from PIL import ImageTk,Image
def blank(i):
    for j in range(0,8):
        if ((i + j) % 2 == 0):
            color = "white"
        else:
            color = "black"
        l=Label(root,bg=color,width=10,height=5)
        l.grid(row=i,column=j)
root=Tk()
root.geometry("740x740")
root.title("chess king")
king=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\gettyimages-154768874-612x612.jpg"))
queen=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\download.jpg"))
hourse=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\black-horse-chess-isolated-on-260nw-315210752.jpg"))
camel=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\istockphoto-877159788-170667a.jpg"))
elephant=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\images.jpg"))
pawn=ImageTk.PhotoImage(Image.open("C:\\Users\\Chetan\\Downloads\\white_pawn-512.png"))
for i in range(0,8):
    if(i==1 or i==6):
        img=pawn
    if(i>1 and i<6):
        blank(i)
        continue
    for j in range(0,8):
        if(i==0 or i==7):
            if(j==0 or j==7):
                img=elephant
            if(j==1 or j==6):
                img=camel
            if(j==2 or j==5):
                img=hourse
            if(j==3):
                img=king
            if(j==4):
                img=queen

        if((i+j)%2==0):
            color="white"
        else:
            color="black"
        e=Label(root,image=img,bg=color,width=80,height=80)
        e.grid(row=i,column=j,padx=1,pady=1)
root.mainloop()