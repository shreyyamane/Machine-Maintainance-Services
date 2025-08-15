import subprocess
import mysql.connector
import tkinter.messagebox as messagebox
from tkinter import *

import Dashboard


class Supervisor:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.configure(bg='grey')

        self.db1 = mysql.connector.connect(host="localhost", user="root", password="", database="details23")
        self.cursor1 = self.db1.cursor()
        self.cursor3 = self.db1.cursor()
        self.cursor2 = self.db1.cursor()

        label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 11, 'bold', 'italic')}
        l1 = Label(self.root, text='Name', **label_style, padx=10)
        l2 = Label(self.root, text='Email', **label_style, padx=10)
        l3 = Label(self.root, text='Contact No', **label_style, padx=10)
        l4 = Label(self.root, text='Address', **label_style, padx=10)
        l5 = Label(self.root, text='Date', **label_style, padx=10)
        l6 = Label(self.root, text='Issue', **label_style, padx=10)
        l7 = Label(self.root, text='Machine', **label_style, padx=10)
        l8 = Label(self.root, text='Technician', **label_style, padx=10)

        l1.grid(row=0, column=0)
        l2.grid(row=0, column=1)
        l3.grid(row=0, column=2)
        l4.grid(row=0, column=3)
        l5.grid(row=0, column=4)
        l6.grid(row=0, column=5)
        l7.grid(row=0, column=6)
        l8.grid(row=0, column=7)

        def submit_data(row):
            i = info[row]
            name = i[0]
            email = i[1]
            contactno = i[2]
            address = i[3]
            date = i[4]
            machine = i[5]
            issue = i[6]
            technician1 = option_l[row].get()
            self.cursor2.execute("INSERT INTO RECOMP (name, email, contactno, address, date, machine_name, issue, technician) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, email, contactno, address, date, machine, issue, technician1))
            self.db1.commit()
            messagebox.showinfo("Success", "Data submitted successfully!")

        self.cursor1.execute("SELECT * FROM client10")
        client = self.cursor1.fetchall()

        self.cursor3.execute("SELECT name FROM technician")
        technician = self.cursor3.fetchall()
        name_list = [name[0] for name in technician]

        info = []
        option_l = []
        num = 1

        for row, i in enumerate(client):
            info.append(i)

            name_label = Label(self.root, text=i[0], **label_style, padx=10, pady=10)
            Email = Label(self.root, text=i[1], **label_style, padx=10, pady=10)
            Contac_no = Label(self.root, text=i[2], **label_style, padx=10, pady=10)
            address = Label(self.root, text=i[3], **label_style, padx=10, pady=10)
            date = Label(self.root, text=i[4], **label_style, padx=10, pady=10)
            machine = Label(self.root, text=i[5], **label_style, padx=10, pady=10)
            issue = Label(self.root, text=i[6], **label_style, padx=10, pady=10)

            option_var = StringVar(self.root)
            option_var.set("Select Name")

            option_menu = OptionMenu(self.root, option_var, *name_list)
            option_menu.grid(row=num, column=7)
            option_menu.configure(bg='grey', fg='white', font=('Ubuntu', 12, 'bold', 'italic'))

            submit_button = Button(self.root, text="Submit", command=lambda row=row: submit_data(row), overrelief='solid', font=('Ubuntu', 11, 'bold', 'italic'))
            submit_button.grid(row=num, column=8, padx=10)

            name_label.grid(row=num, column=0)
            Email.grid(row=num, column=1)
            Contac_no.grid(row=num, column=2)
            address.grid(row=num, column=3)
            date.grid(row=num, column=4)
            machine.grid(row=num, column=5)
            issue.grid(row=num, column=6)

            option_l.append(option_var)
            num += 1

        def back():
            self.root.withdraw()
            Dashboard.dashboard()

        b2 = Button(self.root, text='Back', command=back, overrelief='solid', font=('Ubuntu', 13, 'bold', 'italic'))
        b2.grid(row=0, column=8)
        self.root.mainloop()

        self.cursor1.close()
        self.cursor2.close()
        self.cursor3.close()
        self.db1.close()

if __name__ == "__main__":
    app = Supervisor()
