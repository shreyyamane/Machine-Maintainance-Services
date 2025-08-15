from tkinter import *
from tkinter import messagebox
import Adminlogin
import Clientlogin
import Supervisorlogin


class dashboard:
    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Engineering Language LLP")
        self.root.resizable(False, False)
        self.root.configure(bg='#6a6a6a')
        '''self.img1 = PhotoImage(file="grey23.png")
        self.img_l1 = Label(self.root, image=self.img1)
        self.img_l1.pack()'''


        self.l2 = Label(self.root, text='Welcome To Machine Maintenance And Services', font=('ubuntu', 22, 'bold', 'italic'), fg='white', bg='#6a6a6a')

        self.l2.place(x=60, y=140)

        self.b1 = Button(self.root, text='Admin', width=10, height=2, command=self.button1, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        self.b2 = Button(self.root, text="Supervisor", command=self.button2, width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        self.b3 = Button(self.root, text="Client", command=self.button3, width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        self.b4 = Button(self.root, text="Exit", command=self.button5, width=10, height=2, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        self.b1.place(x=250, y=250)
        self.b2.place(x=350, y=250)
        self.b3.place(x=450, y=250)
        self.b4.place(x=350, y=350)

        self.root.mainloop()

    def button1(self):
        self.root.withdraw()
        Adminlogin.LoginPage()

    def button2(self):
        self.root.withdraw()
        Supervisorlogin.LoginPage2()

    def button3(self):
        self.root.withdraw()
        Clientlogin.LoginPage3()

    def button5(self):
        messagebox.showinfo("", "Thank You")
        self.root.destroy()

if __name__ == "__main__":
    app = dashboard()
