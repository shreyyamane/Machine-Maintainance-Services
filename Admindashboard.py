from tkinter import *
import mysql.connector
from tkinter import messagebox

import AddTechnician
import AdminComplaints
import Clientcreate
import CreateSupervisor
import Dashboard


class Admindash:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Engineering Language LLP")
        self.root.configure(bg='#6a6a6a')



        l2 = Label(self.root, text='Welcome To Machine Maintenance And Services', font=('ubuntu', 22, 'bold', 'italic'), fg='white',bg='#6a6a6a')

        l2.place(x=60, y=140)

        b1 = Button(self.root, text="Create Client", command=self.button1, height=2, width=10, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b2 = Button(self.root, text="Create User", command=self.button2, height=2, width=10, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b3 = Button(self.root, text="Add Technician", command=self.button3, height=2, width=14, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b4 = Button(self.root, text="Complaint", command=self.button4, height=2, width=10, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b5 = Button(self.root, text="Back", command=self.back, height=2, width=10, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b6 = Button(self.root, text="Exit", command=self.exit, height=2, width=10, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))

        b1.place(x=150, y=250)
        b2.place(x=250, y=250)
        b3.place(x=350, y=250)
        b4.place(x=480, y=250)
        b5.place(x=270, y=350)
        b6.place(x=370, y=350)

        self.db = mysql.connector.connect(host="localhost", user="root", password="", database="details23")
        self.cursor = self.db.cursor()

    def button1(self):
        self.root.withdraw()
        Clientcreate.ClientCreate()

    def button2(self):
        self.root.withdraw()
        CreateSupervisor.CreateSupervisor()

    def button3(self):
        self.root.withdraw()
        AddTechnician.Addtech()

    def button4(self):
        self.root.withdraw()
        AdminComplaints.AdminComplaints()

    def back(self):
        self.root.withdraw()
        Dashboard.dashboard()

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    app = Admindash()
    app.root.mainloop()
