from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()

    if email=="chhassaan599@gmail.com" and password=="Allahone@123":
        messagebox.showinfo("Login succesfull")
    else:
        messagebox.showerror("Error","login failled")


root=Tk()
root.iconbitmap(r"c:\Users\Welcome\Downloads\Secure-User-Login-Icon.ico")

root.title("Login Form")

root.geometry("350x500")

root.configure(background="#2A0F29")

img=Image.open("c:\\Users\\Welcome\\Downloads\\login.png")
resized_img=img.resize((150,150))
Img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=Img)
img_label.pack(pady=(20,5))

text_label=Label(root,text="Personal Use",fg="white",bg="#2A0F29")
text_label.pack()
text_label.configure(font=("Verdena",20))

email_label=Label(root,text="Enter Your Email",fg="white",bg="#2A0F29")
email_label.pack(pady=(20,5))
email_label.configure(font=("Bold",9))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text="Enter Your Password",fg="white",bg="#2A0F29")
password_label.pack(pady=(20,5))
password_label.configure(font=("Bold",9))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text="Login Here",fg="black",bg="white",width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.configure(font=("Bold",14))

root.mainloop() 