from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import messagebox

window1 = Tk()
window1.geometry("600x600+40+40")
window1.title('LOGIN PAGE ')
window1.config(background="white")
# ======variable======
un = StringVar()
psw = StringVar()
nam = StringVar()
branchval = StringVar()
regidval = StringVar()
sb1 = StringVar()
sb2 = StringVar()
sb3 = StringVar()


# =======variable========
# ========validte checking function ========


def validate():
    if un.get() == "" or psw.get() == "":
        messagebox.showerror("ERROR", "Invalid UserName or Password ")

    else:
        # messagebox.showinfo("Welcome", f"{un.get()}")
        open1()


# =======================================
# ======== newWindow 1 ===========

def open1():
    window2 = Tk()
    window2.geometry('600x600+40+40')
    window2.title("Detail of student ")
    window2.config(background="white")
    Name = Label(window2, text="Name", font=("Times new roman", 16, "bold"), bg='white')
    Name.grid(row=0, column=0, padx=10, pady=10)
    Name1 = Entry(window2, textvar=nam)
    Name1.grid(row=0, column=1, padx=10, pady=10)
    Branch = Label(window2, text="Branch", font=("Times new roman", 16, "bold"), bg='white')
    Branch.grid(row=1, column=0, padx=10, pady=10)
    Branch1 = Entry(window2, textvar=branchval)
    Branch1.grid(row=1, column=1, padx=10, pady=10)
    Regid = Label(window2, text="RegID", font=("Times new roman", 16, "bold"), bg='white')
    Regid.grid(row=2, column=0, padx=10, pady=10)
    Regid1 = Entry(window2, textvar=regidval)
    Regid1.grid(row=2, column=1, padx=10, pady=10)
    submit2 = Button(window2, text="SUBMIT", width=12, bg='red', fg='black', command=database1)
    submit2.grid(row=3, column=1, padx=20, pady=20)


def database2():
    open3()


def open2():
    window3 = Tk()
    window3.geometry('600x600+40+40')
    window3.title("Subject And Mark Entry ")
    window3.config(background="black")
    subject1 = Button(window3, text="Subject1", width=12, bg='red', fg='black', command=lambda: subj1.grid(row=0, column=1, padx=10, pady=10))
    subject1.grid(row=0, column=0, padx=20, pady=20)
    subj1 = Entry(window3, textvar=sb1,)
#   subject1.grid(row=0, column=1, padx=10, pady=10)
    subject2 = Button(window3, text="Subject2", width=12, bg='red', fg='black', command=lambda: subj2.grid(row=1, column=1, padx=10, pady=10))
    subject2.grid(row=1, column=0, padx=20, pady=20)
    subj2 = Entry(window3, textvar=sb2)
#   subject2.grid(row=1, column=1, padx=10, pady=10)
    subject3 = Button(window3, text="Subject3", width=12, bg='red', fg='black', command=lambda: subj3.grid(row=2, column=1, padx=10, pady=10))
    subject3.grid(row=2, column=0, padx=20, pady=20)
    subj3 = Entry(window3, textvar=sb3)
#  subject3.grid(row=2, column=1, padx=10, pady=10)
    submit3 = Button(window3, text="SUBMIT", width=12, bg='red', fg='black', command=database2)
    submit3.grid(row=3, column=1, padx=20, pady=20)


def database1():
    name_store = nam.get()
    branch_store = branchval.get()
    regid_store = regidval.get()
    conn = sqlite3.connect("Form.db")
    open2()


def quit1():
    quit()


def open3():
    window4 = Tk()
    window4.geometry('600x600+40+40')
    window4.title("CGPA and Value ")
    CGPA1 = Button(window4, text="CGPA", width=12, bg='red', fg='black', )
    CGPA1.grid(row=0, column=0, padx=20, pady=20)
    GRADE1 = Button(window4, text="GRADE", width=12, bg='red', fg='black', )
    GRADE1.grid(row=1, column=0, padx=20, pady=20)
    NEWINPUT1 = Button(window4, text="NEWINPUT", width=12, bg='red', fg='black', command=validate)
    NEWINPUT1.grid(row=2, column=0, padx=20, pady=20)
    submit3 = Button(window4, text="QUIT", width=12, bg='red', fg='black', command=quit1)
    submit3.grid(row=3, column=1, padx=20, pady=20)


# ==============end=========


# ======mainloop====

user = Label(window1, text="UserName", font=("Times new roman", 16, "bold"), bg='white')
user.grid(row=0, column=0, padx=10, pady=10)
password = Label(window1, text="Password", font=("Times new roman", 16, "bold"), bg='white')
password.grid(row=1, column=0, padx=10, pady=10)
user1 = Entry(window1, textvar=un)
user1.grid(row=0, column=1, padx=10, pady=10)
password1 = Entry(window1, textvar=psw)
password1.grid(row=1, column=1, padx=10, pady=10)
submit1 = Button(window1, text="SUBMIT", width=12, bg='red', fg='black', command=validate)
submit1.grid(row=2, column=1, padx=20, pady=20)
# submit1.bind("<Button-1>", open1)


window1.mainloop()
