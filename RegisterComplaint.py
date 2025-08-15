from tkinter import *
from tkinter import messagebox
import mysql.connector

import Clientdashboard


class Registercomplaint:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.configure(bg='grey')

        self.db1 = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="details23")
        self.cursor1 = self.db1.cursor()

        self.root.configure(bg='grey')
        self.menu = StringVar(self.root)
        self.menu.set("Select")
        self.options = ["Laptop","Washing machine","Oven","Television","Monitor","Refrigerator"]

        self.l3 = Label(self.root, text="Mobile Number:", font=('Ubuntu', 12, 'bold', 'italic'), bg='grey', fg='white')
        self.e3 = Entry(self.root, width=30, font=("Times new roman", 12))
        self.l1 = Label(self.root, text="Machines:", font=('Ubuntu', 12, 'bold', 'italic'), bg='grey', fg='white')
        self.drop = OptionMenu(self.root, self.menu, *self.options)
        self.drop.config(font=('Ubuntu', 10, 'bold', 'italic'))

        self.l1.place(x=50, y=70)
        self.l3.place(x=30, y=20)
        self.e3.place(x=170, y=20, height=30)
        self.drop.place(x=200, y=70)

        next1 = Button(self.root, text="Next", command=self.issue1, font=('Roboto', 10, 'bold'), overrelief='solid')
        next1.place(x=430, y=20)

        def back():
            self.root.withdraw()
            Clientdashboard.Clientdash()

        b2 = Button(self.root, text='Back', command=back, overrelief='solid', font=('Ubuntu', 10, 'bold', 'italic'))
        b2.place(x=500, y=20)

        self.root.mainloop()

    def issue1(self):
        l2 = Label(self.root, text="Issue", font=('Ubuntu', 12, 'bold', 'italic'), bg='grey', fg='white')
        e1 = Entry(self.root, width=30, font=("Times new roman", 10))
        l2.place(x=80, y=130)
        e1.place(x=80, y=160, height=100, width=400)

        def insert_issue():
            issue = "UPDATE CLIENT10 SET ISSUE =  (%s), MACHINE = (%s) WHERE CONTACTNO = (%s) "
            insert_data = (e1.get(), self.menu.get(), self.e3.get(),)

            self.cursor1.execute(issue, insert_data)
            self.db1.commit()
            self.cursor1.close()
            self.mes()

        submit = Button(self.root, text="Submit", command=insert_issue, overrelief='solid',
                        font=('Ubuntu', 10, 'bold', 'italic'))
        submit.place(x=210, y=270)

    def mes(self):
        messagebox.showinfo("", "Information submitted Successfully")


if __name__ == "__main__":
    app = Registercomplaint()
