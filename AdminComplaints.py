import subprocess
import mysql.connector
from tkinter import *
from tkinter import messagebox

import Admindashboard


class AdminComplaints:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.configure(bg='grey')
        self.root.resizable(False, False)


        self.db1 = mysql.connector.connect(host="localhost", user="root", password="", database="details23")
        self.cursor1 = self.db1.cursor()

        def back():
            self.root.withdraw()
            Admindashboard.Admindash()

        def exit_app():
            self.root.destroy()

        label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 11, 'bold', 'italic')}

        l1 = Label(self.root, text='Name', **label_style)
        l2 = Label(self.root, text='Email', **label_style)
        l3 = Label(self.root, text='Address', **label_style)
        l4 = Label(self.root, text='Date', **label_style)
        l5 = Label(self.root, text='Issue', **label_style)
        l6 = Label(self.root, text='Machine Name', **label_style)
        l7 = Label(self.root, text='Technician', **label_style)
        l8 = Label(self.root, text='Contact No', **label_style)

        b1 = Button(self.root, text='Back', command=back, font=('Ubuntu', 14, 'bold', 'italic'), width=10)
        b2 = Button(self.root, text='Exit', command=exit_app, font=('Ubuntu', 14, 'bold', 'italic'), width=10)

        b1.grid(row=0, column=3, padx=5, pady=5)
        b2.grid(row=0, column=4, padx=5, pady=5)

        def show_complaints():
            query = "SELECT * FROM RECOMP"
            self.cursor1.execute(query)
            result = self.cursor1.fetchall()

            l1.grid(row=1, column=0, padx=10, pady=10)
            l2.grid(row=1, column=1, padx=10, pady=10)

            l3.grid(row=1, column=3, padx=10, pady=10)
            l4.grid(row=1, column=4, padx=10, pady=10)
            l5.grid(row=1, column=6, padx=10, pady=10)
            l6.grid(row=1, column=5, padx=10, pady=10)
            l7.grid(row=1, column=7, padx=10, pady=10)
            l8.grid(row=1, column=2, padx=10, pady=10)
            for i, data in enumerate(result):
                name = Label(self.root, text=data[0], **label_style)
                contact = Label(self.root, text=data[1], **label_style)
                email = Label(self.root, text=data[2], **label_style)
                address = Label(self.root, text=data[3], **label_style)
                date = Label(self.root, text=data[4], **label_style)
                machine = Label(self.root, text=data[5], **label_style)
                issue = Label(self.root, text=data[6], **label_style)
                technician = Label(self.root, text=data[7], **label_style)

                name.grid(row=i + 2, column=0, padx=10, pady=5)
                contact.grid(row=i + 2, column=1, padx=10, pady=5)
                email.grid(row=i + 2, column=2, padx=10, pady=5)
                address.grid(row=i + 2, column=3, padx=10, pady=5)
                date.grid(row=i + 2, column=4, padx=10, pady=5)
                machine.grid(row=i + 2, column=5, padx=10, pady=5)
                issue.grid(row=i + 2, column=6, padx=10, pady=5)
                technician.grid(row=i + 2, column=7, padx=10, pady=5)

        show_complaints()

        self.root.mainloop()

        self.cursor1.close()
        self.db1.close()

if __name__ == "__main__":
    app = AdminComplaints()
