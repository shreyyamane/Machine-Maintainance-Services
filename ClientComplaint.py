from tkinter import *
import mysql.connector
from tkinter import messagebox

import Clientdashboard

label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 11, 'bold', 'italic')}
class clientcomplaint:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x600')
        self.root.configure(bg='grey')

        self.db1 = mysql.connector.connect(host="localhost", user="root", password="", database="details23")
        self.cursor1 = self.db1.cursor()


        self.l0 = Label(self.root, text='Mobile Number', **label_style)
        self.l1 = Label(self.root, text='Name', **label_style)
        self.l2 = Label(self.root, text='Email', **label_style)
        self.l3 = Label(self.root, text='Address', **label_style)
        self.l4 = Label(self.root, text='Date', **label_style)

        self.l6 = Label(self.root, text='Machine Name', **label_style)
        self.l5 = Label(self.root, text='Issue', **label_style)
        self.l7 = Label(self.root, text='Technician', **label_style)
        self.l8 = Label(self.root, text='Contact No', **label_style)
        self.b1 = Button(self.root, text='Back', command=self.back1, font=('Ubuntu', 12, 'bold', 'italic'), overrelief='solid')
        self.b2 = Button(self.root, text='Exit', command=self.exit, font=('Ubuntu', 12, 'bold', 'italic'), overrelief='solid')

        self.e0 = Entry(self.root)

        self.l0.grid(row=0, column=0, pady=10, padx=5)
        self.e0.grid(row=0, column=1, padx=5, pady=10)
        self.b1.grid(row=0, column=3, padx=5, pady=10)
        self.b2.grid(row=0, column=4, padx=5, pady=10)

        submit = Button(self.root, text="Submit", command=self.show, font=('Ubuntu', 12, 'bold', 'italic'), overrelief='solid')
        submit.grid(row=0, column=2)

        self.root.mainloop()

    def back1(self):
        self.root.withdraw()
        Clientdashboard.Clientdash()

    def exit(self):
        self.root.destroy()

    def show(self):
        mob = self.e0.get()
        query = "SELECT * FROM RECOMP WHERE CONTACTNO = %s"
        self.cursor1.execute(query, (mob,))
        result = self.cursor1.fetchall()
        self.l1.grid(row=1, column=0, padx=10, pady=10)
        self.l2.grid(row=1, column=1, padx=10, pady=10)
        self.l8.grid(row=1, column=2, padx=10, pady=10)
        self.l3.grid(row=1, column=3, padx=10, pady=10)
        self.l4.grid(row=1, column=4, padx=10, pady=10)
        self.l5.grid(row=1, column=6, padx=10, pady=10)
        self.l6.grid(row=1, column=5, padx=10, pady=10)
        self.l7.grid(row=1, column=7, padx=10, pady=10)

        if result:
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

        else:
            messagebox.showinfo("No Data", "Enter A valid Number.")

    def __del__(self):
        self.cursor1.close()
        self.db1.close()

if __name__ == "__main__":
    app = clientcomplaint()
