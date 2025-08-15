import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

import Admindashboard


class CreateSupervisor:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.configure(bg='grey')

        self.db1 = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="User_Details")
        self.cursor1 = self.db1.cursor()

        self.root.title("Engineering Language LLP")
        label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 12, 'bold', 'italic')}
        l1 = Label(self.root, text="Name:", **label_style)
        l2 = Label(self.root, text="Email:", **label_style)
        l4 = Label(self.root, text="Contact:", **label_style)
        e1 = Entry(self.root)
        e2 = Entry(self.root)
        e4 = Entry(self.root)

        l1.place(x=250, y=20, height=30)
        l2.place(x=250, y=60, height=30)
        l4.place(x=250, y=100, height=30)

        e1.place(x=350, y=20, width=200, height=30)
        e2.place(x=350, y=60, width=200, height=30)
        e4.place(x=350, y=100, width=200, height=30)

        def back():
            self.root.withdraw()
            Admindashboard.Admindash()
        def insert_data():
            Name = e1.get()
            Email = e2.get()
            contactno = e4.get()

            submit_query = "INSERT INTO USER VALUES(%s,%s,%s)"
            vals = (Name, Email, contactno)
            self.cursor1.execute(submit_query, vals)
            self.db1.commit()
            self.cursor1.close()
            messagebox.showinfo("", "Successfully created")

        submit = Button(self.root, text='Submit', width=10, height=2, command=insert_data, overrelief='solid',
                        font=('Roboto', 10, 'bold', 'italic'))
        back1 = Button(self.root, text='Back', width=10, height=2, command=back, overrelief='solid',
                       font=('Roboto', 10, 'bold', 'italic'))
        submit.place(x=280, y=150)
        back1.place(x=390, y=150)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CreateSupervisor()
    app.run()
