from tkinter import *
import mysql.connector
from tkinter import messagebox

import ClientComplaint
import Dashboard
import RegisterComplaint


class Clientdash:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Engineering Language LLP")
        self.root.configure(bg='#6a6a6a')



        l2 = Label(self.root, text='Welcome To Machine Maintainance And Services', font=('ubuntu', 22, 'bold', 'italic'), bg='#6a6a6a', fg='white')

        l2.place(x=60, y=140)
        b1 = Button(self.root, text='Register Complaint', command=self.b1,width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b2 = Button(self.root, text="Complaints", command=self.b2, width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b3 = Button(self.root, text="Back", command=self.b3, width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        b1.place(x=250, y=250, width=130)
        b2.place(x=400, y=250, width=120)
        b3.place(x=330, y=350, width=120)

        self.root.mainloop()

    def b1(self):
        self.root.withdraw()
        RegisterComplaint.Registercomplaint()
    def b2(self):
        self.root.withdraw()
        ClientComplaint.clientcomplaint()

    def b3(self):
        self.root.withdraw()
        Dashboard.dashboard()

if __name__ == "__main__":
    app = Clientdash()
