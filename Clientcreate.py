import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import Admindashboard

class ClientCreate:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.configure(bg='grey')
        self.root.resizable(False, False)
        self.db1 = mysql.connector.connect(host="localhost", user="root", password="", database="details23")
        self.cursor1 = self.db1.cursor()

        label_style = {'bg': 'grey', 'fg': 'White', 'font': ('Ubuntu', 12, 'bold', 'italic')}
        self.root.title("Engineering Language LLP")
        l1 = tkinter.Label(self.root, text="Name", **label_style)
        l2 = tkinter.Label(self.root, text="Email", **label_style)
        l3 = tkinter.Label(self.root, text="Address", **label_style)
        l4 = tkinter.Label(self.root, text="ContactNo", **label_style)
        l5 = tkinter.Label(self.root, text="Date", **label_style)
        self.e1 = tkinter.Entry(self.root)
        self.e2 = tkinter.Entry(self.root)
        self.e3 = tkinter.Entry(self.root)
        self.e4 = tkinter.Entry(self.root)
        self.year_entry = ttk.Combobox(self.root, width=8, state='readonly')
        self.month_entry = ttk.Combobox(self.root, width=8, state='readonly')
        self.day_entry = ttk.Combobox(self.root, width=8, state='readonly')

        b1 = tkinter.Button(self.root, text='Back', width=10, height=2, command=self.b1, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))

        l1.place(x=250, y=20, height=30)
        l2.place(x=250, y=60, height=30)
        l3.place(x=250, y=100, height=30)
        l4.place(x=250, y=140, height=30)
        l5.place(x=250, y=180, height=30)

        self.e1.place(x=350, y=20, width=200, height=30)
        self.e2.place(x=350, y=60, width=200, height=30)
        self.e3.place(x=350, y=100, width=200, height=30)
        self.e4.place(x=350, y=140, width=200, height=30)
        self.year_entry.place(x=350, y=180, width=80)
        self.month_entry.place(x=440, y=180, width=80)
        self.day_entry.place(x=530, y=180, width=80)

        submit = tkinter.Button(self.root, text='Submit', width=10, height=2, command=self.insert_data, overrelief='solid', font=('Roboto', 10, 'bold', 'italic'))
        submit.place(x=280, y=220)
        b1.place(x=380, y=220)

        # Populate the date picker with years, months, and days
        years = [str(year) for year in range(1900, 2101)]
        self.year_entry['values'] = years

        months = [str(month).zfill(2) for month in range(1, 13)]
        self.month_entry['values'] = months

        days = [str(day).zfill(2) for day in range(1, 32)]
        self.day_entry['values'] = days

    def b1(self):
        self.root.withdraw()
        Admindashboard.Admindash()

    def insert_data(self):
        Name = self.e1.get()
        Email = self.e2.get()
        Address = self.e3.get()
        contact_info = self.e4.get()
        year = self.year_entry.get()
        month = self.month_entry.get()
        day = self.day_entry.get()

        if Name == "" or not year or not month or not day:
            messagebox.showinfo("", "Enter a Valid Information and Date")
            return

        date = f"{year}-{month}-{day}"

        submit_query = "INSERT INTO CLIENT10(NAME, EMAIL, CONTACTNO, ADDRESS, DATE) VALUES (%s, %s, %s, %s, %s)"
        vals = (Name, Email, contact_info, Address, date)
        self.cursor1.execute(submit_query, vals)
        self.db1.commit()
        self.cursor1.close()
        messagebox.showinfo("", "Client Registered Successfully")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ClientCreate()
    app.run()
