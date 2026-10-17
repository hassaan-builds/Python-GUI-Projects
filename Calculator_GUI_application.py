from tkinter import *

frst_num=sec_num=operator=None

def get_operator(op):
    global frst_num,operator

    frst_num=int(result_label["text"])
    operator=op
    result_label.configure(text="")


def get_degit(dijit):
    current=result_label["text"]
    new=current+str(dijit)
    result_label.configure(text=new)

def clear():
    result_label.configure(text="")

def get_result():
    global frst_num,sec_num,operator
    sec_num=int(result_label["text"])


    if operator=="+":
        result_label.configure(text=str(frst_num+sec_num))

    elif operator=="-":
        result_label.configure(text=str(frst_num-sec_num))

    elif operator=="*":
        result_label.configure(text=str(frst_num-sec_num))

    elif operator=="÷":
        result_label.configure(text=str(frst_num/sec_num))
    else:
        if sec_num==0:
            result_label.configure(text="Eror")
        else:
            result_label.configure(text=str(round(frst_num/sec_num,2)))





root=Tk()
root.title("Calculator")
root.geometry("280x380")
root.configure(background="black")
root.resizable(0,0)

result_label=Label(root,text="",bg="#101114",fg="white")
result_label.grid(row=0,column=0,columnspan=10,pady=(50,50),sticky="w")
result_label.configure(font=("Verdana",30,"bold"))

btn_7=Button(root,text="7",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(7))
btn_7.grid(row=1,column=0)
btn_7.configure(font=("verdana",13,"bold"))


btn_8=Button(root,text="8",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(8))
btn_8.grid(row=1,column=1)
btn_8.configure(font=("verdana",13,"bold"))



btn_9=Button(root,text="9",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(9))
btn_9.grid(row=1,column=2)
btn_9.configure(font=("verdana",13,"bold"))


btn_add=Button(root,text="+",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_operator("+"))
btn_add.grid(row=1,column=3)
btn_add.configure(font=("verdana",13,"bold"))


btn_6=Button(root,text="6",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(6))
btn_6.grid(row=2,column=0)
btn_6.configure(font=("verdana",13,"bold"))


btn_5=Button(root,text="5",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(5))
btn_5.grid(row=2,column=1)
btn_5.configure(font=("verdana",13,"bold"))


btn_4=Button(root,text="4",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(4))
btn_4.grid(row=2,column=2)
btn_4.configure(font=("verdana",13,"bold"))



btn_minus=Button(root,text="-",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_operator("-"))
btn_minus.grid(row=2,column=3)
btn_minus.configure(font=("verdana",13,"bold"))

btn_1=Button(root,text="1",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(1))
btn_1.grid(row=3,column=0)
btn_1.configure(font=("verdana",13,"bold"))


btn_2=Button(root,text="2",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(2))
btn_2.grid(row=3,column=1)
btn_2.configure(font=("verdana",13,"bold"))


btn_3=Button(root,text="3",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(3))
btn_3.grid(row=3,column=2)
btn_3.configure(font=("verdana",13,"bold"))

btn_multi=Button(root,text="*",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_operator("*"))
btn_multi.grid(row=3,column=3)
btn_multi.configure(font=("verdana",13,"bold"))

btn_0=Button(root,text="0",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_degit(0))
btn_0.grid(row=4,column=1)
btn_0.configure(font=("verdana",13,"bold"))

btn_divsion=Button(root,text="÷",bg="#292B31",fg="white",width=5,height=2,command=lambda:get_operator("÷"))
btn_divsion.grid(row=4,column=3)
btn_divsion.configure(font=("verdana",13,"bold"))

btn_equal=Button(root,text="=",bg="#292B31",fg="white",width=5,height=2,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.configure(font=("verdana",13,"bold"))

btn_del=Button(root,text="c",bg="#292B31",fg="white",width=5,height=2,command=lambda:clear())
btn_del.grid(row=4,column=0)
btn_del.configure(font=("verdana",13,"bold"))

root.mainloop()