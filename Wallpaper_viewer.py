from tkinter import *
from PIL import Image, ImageTk
import os

root=Tk()
root.title("Wallpaper Viewer")
root.configure(background="black")
root.geometry("200x350")

files=os.listdir(r"c:\Users\Welcome\Desktop\photo wallpaper")
img_arry=[]
for file in files:
    img=Image.open(os.path.join(r"c:\Users\Welcome\Desktop\photo wallpaper",file))
    resized_img=img.resize((200,300))
    img_arry.append(ImageTk.PhotoImage(resized_img))

image_label=Label(root,image=img_arry[0])
image_label.pack(pady=20)

next_btn=Button(root,text="NEXT",bg="white",fg="white")

next_btn.pack()


root.mainloop()
