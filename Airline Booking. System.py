import tkinter as tk

from tkinter import *

from tkinter import messagebox

import tkinter.font as font

from tkinter import ttk

from tkcalendar import Calendar, DateEntry


airline = {}


def menuScreen():
    
    def fndisplay():

        root = tk.Tk()

        root.geometry("500x500")

        root.title("MAYAN AIRLINES")

        root['background'] = '#1a90ff'

        tk.Label(root, text="MAYAN AIRLINES",bg='#1a90ff',fg='white', font=("Times New Roman Bold", 20)).pack()

        frame = Frame(root)

        frame.pack()

        columns = (1, 2, 3, 4)

        tree = ttk.Treeview(frame, columns=columns, height=300, show="headings")

        tree.pack(side='right')

        tree.heading(1, text="NAME")

        tree.heading(2, text="TO")

        tree.heading(3, text="FROM")

        tree.heading(4, text="DATE")

        tree.column(1, width=130)

        tree.column(2, width=130)

        tree.column(3, width=130)

        tree.column(4, width=130)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)

        scroll.pack(side='right', fill='y')

        for a in airline:
            val = airline[a]

            tree.insert('', 'end', values=(a, val[0], val[1], val[2]))

    def fninsert():

        name = txtname.get()

        to = txtto.get()

        fro = txtfro.get()

        day = txtday.get()

        airline[name] = [to, fro, day]

        messagebox.showinfo("Message ", "Ticket Booked")

    def fnclear():

        txtname.delete(0, END)

        txtto.delete(0, END)

        txtfro.delete(0, END)

        txtday.delete(0, END)

    def fnsearch():

        name = txtname.get()

        if name in airline:

            messagebox.showinfo("Message ", "Passenger Found")

            lst = airline[name]

            txtto.insert(END, lst[0])

            txtfro.insert(END, lst[1])

            txtday.insert(END, lst[2])

        else:

            messagebox.showinfo("Message ", "No such Passenger")

    def fndelete():

        x = messagebox.askyesno("Alert  ", "Are you sure you want to delete the ticket ")

        name = txtname.get()

        if x == True:
            del airline[name]

            messagebox.showinfo("Message ", " Ticket DELETED")

            fnclear()

    def fnupdate():

        x = messagebox.askyesno("Alert  ", "Are you sure you want to update the ticket")

        if x == True:
            name = txtname.get()

            to = txtto.get()

            fro = txtfro.get()

            day = txtday.get()

            airline[name] = [to, fro, day]

            messagebox.showinfo("ALERT ", "Ticket Updated")

    root = tk.Tk()

    root.geometry("650x650")

    root.title(" MAYAN AIRLINES")

    root.configure(bg='#F5F5DC')

    C = Canvas(root, bg="blue", height=1000, width=950)

    lblmenu = tk.Label(root, text="MAYAN AIRLINES", bg='#F5F5DC',fg='#003399', font=('Times New Roman', 28, 'bold'))

    lblmenu.place(x=220, y=20)

    lblname = tk.Label(root, text="Name", bg='#F5F5DC', fg='#b30000', font=("Times New Roman Bold", 20))

    lblname.place(x=50, y=100)

    txtname = tk.Entry(root, width=35, fg='blue', bg='White', font=("Times New Roman Bold", 10))

    txtname.place(x=150, y=100, width=100)

    lblto = tk.Label(root, text="To", fg='#b30000', bg='#F5F5DC', font=("Times New Roman Bold", 20))

    lblto.place(x=50, y=200)

    txtto = tk.Entry(root, width=35, fg='blue', bg='White', font=("Times New Roman Bold", 10))

    txtto.place(x=150, y=200, width=100)

    lblfro = tk.Label(root, text="From", fg='#b30000', bg='#F5F5DC', font=("Times New Roman Bold", 20))

    lblfro.place(x=50, y=300)

    txtfro = tk.Entry(root, width=35, fg='blue', bg='White', font=("Times New Roman Bold", 10))

    txtfro.place(x=150, y=300, width=100)

    lblday = tk.Label(root, text="Date", fg='#b30000', bg='#F5F5DC', font=("Times New Roman Bold", 20))

    lblday.place(x=50, y=400)

    txtday = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, month=2, day=3)

    txtday.pack(padx=10, pady=10)
    
    txtday.place(x=150, y=400, width=100)

   

    btninsert = tk.Button(root, text="Book", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10), command=fninsert)

    btninsert.place(x=60, y=500, width=60)

    btnclear = tk.Button(root, text="Clear", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10),
                         command=fnclear)

    btnclear.place(x=160, y=500, width=60)

    btndisplay = tk.Button(root, text="Display", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10),
                           command=fndisplay)

    btndisplay.place(x=260, y=500, width=60)

    btnsearch = tk.Button(root, text="Delete", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10),
                          command=fndelete)

    btnsearch.place(x=360, y=500, width=60)

    btnupdate = tk.Button(root, text="Update", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10),
                          command=fnupdate)

    btnupdate.place(x=460, y=500, width=60)

    btnsearch = tk.Button(root, text="Search", fg='#00008B', bg='light green', font=("Times New Roman Bold", 10),
                          command=fnsearch)

    btnsearch.place(x=560, y=500, width=60)


def WELCOMESCREEN():
    import turtle

    import math

    # import random

    wn = turtle.Screen()

    wn.bgcolor('black')

    A = turtle.Turtle()

    A.speed(0)

    A.color('white')

    rotate = int(360)

    color = ['red', 'blue', 'yellow', 'green', 'lightblue', 'orange', 'lightgreen']

    j = 0

    def drawCircles(t, size):

        for i in range(10):  # i=[0,1,2,3,4,5,6,7,8,9]

            t.color(color[i % 7])

            t.circle(size)

            size = size - 4

    def drawPattern(A, size, repeat):

        for i in range(repeat):
            drawCircles(A, size)

            A.right(360 / repeat)

    drawPattern(A, 100, 10)

    turtle.color('white')

    style = ('GEORGIA', 20, 'bold')

    turtle.write('WELCOME TO MAYAN AIRLINES!', font=style, align='center')

    turtle.hideturtle()

    turtle.exitonclick()


def loginscreen():
    def funclear():

        txtUser.delete(0, END)

        txtpass.delete(0, END)

        txtUser.focus()

    def funlogin():

        user = txtUser.get()

        passw = txtpass.get()

        if user == "Aditya A" and passw == "ADI123":

            messagebox.showinfo("Login ", "Login Successful")

            root.destroy()

            menuScreen()

        else:

            messagebox.showinfo("Login ", "Login Denied")

    root = tk.Tk()

    root.geometry("500x500")

    root.title("MA Login Page")
    
    root['background'] = '#F5F5DC'

    C = Canvas(root, bg="Red", height=250, width=300)

    lbluser = tk.Label(root, text="Username ", fg="black",bg='#F5F5DC', font=("Times New Roman Bold", 20))

    lbluser.place(x=50, y=130)

    txtUser = tk.Entry(root, width=35, fg="black",bg='white', font=("Times New Roman Bold", 15))

    txtUser.place(x=180, y=137, width=100)

    lblpass = tk.Label(root, text="Password ", fg="black",bg='#F5F5DC', font=("Times New Roman Bold", 20))

    lblpass.place(x=50, y=200)

    txtpass = tk.Entry(root, show="*", width=35, fg="black",bg='white', font=("Times New Roman Bold", 15))

    txtpass.place(x=180, y=207, width=100)

    loginbtn = tk.Button(root, text="Login", fg='#00008B', font=("Times New Roman Bold", 20), command=funlogin)

    loginbtn.place(x=100, y=350, width=55)

    clearbtn = tk.Button(root, text="Clear", fg='#00008B', font=("Times New Roman Bold", 20), command=funclear)

    clearbtn.place(x=350, y=350, width=55)

    root.mainloop()


# __main__

WELCOMESCREEN()

loginscreen()

airline = {}
