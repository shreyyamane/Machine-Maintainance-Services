from tkinter import *
from tkinter import messagebox
import mysql.connector

import Dashboard
import Supervisordashboard


class LoginPage2:
    def __init__(self):
        super().__init__()

        self.root =Tk()
        self.root.geometry("400x200")
        self.root.configure(bg='grey')
        self.root.title("Login Page")

        label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 12, 'bold', 'italic')}
        self.l1 = Label(self.root, text="Username", **label_style)
        self.l2 = Label(self.root, text="Password", **label_style)

        self.e1 = Entry(self.root, bg='white', font=('Ubuntu', 10))
        self.e2 = Entry(self.root, show="*", font=('Ubuntu', 10, 'bold'))

        self.l1.place(x=50, y=30, height=30)
        self.l2.place(x=50, y=80, height=30)

        self.e1.place(x=150, y=30, width=150, height=30)
        self.e2.place(x=150, y=80, width=150, height=30)

        self.login = Button(self.root, text="Login", command=self.insert_data, font=('Roboto', 10, 'bold', 'italic'), overrelief='solid')
        self.login.place(x=150, y=130, height=30, width=50)

        self.b2 = Button(self.root, text='Back', command=self.back, overrelief='solid', font=('Ubuntu', 10, 'bold', 'italic'))
        self.b2.place(x=250, y=130, height=30, width=50)

        '''self.db1 = mysql.connector.connect(host="localhost", user="root", password="Piyush@12", database="client_details")
        self.cursor1 = self.db1.cursor()'''

    def insert_data(self):
        Username = self.e1.get()
        Password = self.e2.get()

        if Username == "Sharad" and Password == "12345":
            self.root.withdraw()
            Supervisordashboard.Supervisor()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def back(self):
        self.root.withdraw()
        Dashboard.dashboard().mainloop()

if __name__ == "__main__":
    app = LoginPage2()
    app.root.mainloop()
