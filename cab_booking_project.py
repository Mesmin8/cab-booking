from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3

Item4 = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()


# main Class
class user:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="green")
            self.head.pack(fill=X)
            self.head.configure(background="#FED049")
            application = travel(root)

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Already Taken!')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('Times new roman', 35), pady=10, fg="purple")
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('Times new roman', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, borderwidth=2,  relief=SOLID,  font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('Times new roman', 20), pady=5, padx=8).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, relief=SOLID, borderwidth=2,  font=('', 15), show='*').grid(row=1, column=1, padx=8)
        Button(self.logf, text=' Login ', bd=3, font=('Times new roman', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('Times new roman', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('Times new roman', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('Times new roman', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('Times new roman', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('Times new roman', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


class travel:

    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry(geometry)
        self.root.configure(background='black')

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        varl1 = StringVar()
        varl2 = StringVar()
        varl3 = StringVar()
        reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Mobile = StringVar()
        Telephone = StringVar()
        Email = StringVar()

        TaxiTax = StringVar()
        Km = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        PrimeSedan = StringVar()
        PremiumSedan = StringVar()

        TaxiTax.set("0")
        Km.set("0")
        Travel_Ins.set("0")
       

        # ==========================================Define Functiom==================================================

        def iExit():
            iExit = ms.askyesno("Prompt!", "Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Travel_Ins.set("0")
          

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
        
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)
            self.cboPooling.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtTravel_Ins.configure(state=DISABLED)
        
            self.reset_counter = 1

        def Receiptt():
            if reset_counter is 0 and Firstname.get() != "" and Surname.get() != "" and Address.get() != "" and Postcode.get() != ""  and Telephone.get() != "" and Email.get() != "":
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                x = random.randint(10853, 500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END, "Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END, 'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END, 'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END, 'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END, 'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END, 'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END, 'Postal Code:\n')
                self.txtReceipt2.insert(END, Postcode.get() + "\n")
                self.txtReceipt1.insert(END, 'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
          
                self.txtReceipt1.insert(END, 'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END, 'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END, 'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END, 'Pooling:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
              
                self.txtReceipt1.insert(END, 'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END, 'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END, 'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))

            else:
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                self.txtReceipt1.insert(END, "\nNo Input")

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state=NORMAL)
                Item1 = float(50)
                TaxiTax.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1 = 0

        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Ludhiana":
                    switch = {"Amritsar": 140, "Sangrur": 78, "Pathankot": 171, "Ludhiana": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Amritsar":
                    switch = {"Amritsar": 0, "Ludhiana": 140, "Pathankot": 115, "Sangrur": 214}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Pathankot":
                    switch = {"Ludhiana": 171, "Pathankot": 0, "Sangrur": 250, "Amritsar": 115}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Sangrur":
                    switch = {"Ludhiana": 78, "Sangrur": 0, "Pathankot": 250, "Amritsar": 214}
                    Km.set(switch[varl2.get()])

        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravel_Ins.configure(state=NORMAL)
                Item3 = float(10)
                Travel_Ins.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtTravel_Ins.configure(state=DISABLED)
                Travel_Ins.set("0")
                Item3 = 0

        def Total_Paid():
            if ((
                    var1.get() == 1 and var2.get() == 1 and var3.get() == 1 ) and (
                    varl1.get() != "" and varl2.get() != "")):

                Item2 = Km.get()
                Cost_of_fare = (Item1 + (float(Item2) ) + Item3 )

                Tax = "Rs " + str('%.2f' % ((Cost_of_fare) * 0.09))
                ST = "Rs " + str('%.2f' % ((Cost_of_fare)))
                TT = "Rs " + str('%.2f' % (Cost_of_fare + ((Cost_of_fare) * 0.9)))
             

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !", "Invalid Input\nPlease try again !!!")

        # ================================================mainframe========================================================================

        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=True)

        Tops = Frame(MainFrame, bd=3, width=1350, relief=SOLID, background="#4E6C50")
        Tops.pack(side=TOP, expand=True)

        self.lblTitle = Label(Tops, font=('Times new roman', 70, 'bold'), text="  Taxi   Booking   System ", fg="#153462",bg="#FED049")
        self.lblTitle.grid()

        # ================================================customerframedetail=============================================================
        CustomerDetailsFrame = LabelFrame(MainFrame, width=1350, height=500, bd=3, pady=5, relief=RIDGE, background="#F2DEBA")
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        FrameDetails = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)

        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=3, font=('arial', 12, 'bold'), 
                                  text="Customer Name", relief=SOLID, borderwidth=3)
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(FrameDetails, bd=3, width=300, height=250, font=('arial', 12, 'bold'),
                                 text="Booking Detail", relief=SOLID, borderwidth=3)
        TravelFrame.grid(row=0, column=1)

        Book_Frame = LabelFrame(FrameDetails, width=300, height=150, relief=FLAT)
        Book_Frame.grid(row=1, column=0)

        CostFrame = LabelFrame(FrameDetails, width=150, height=150, bd=5, relief=FLAT)
        CostFrame.grid(row=1, column=1)

        # ===============================================recipt======================================================================
        Receipt_BottonFrame = LabelFrame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=SOLID, borderwidth=3)
        Receipt_BottonFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        ReceiptFrame = LabelFrame(Receipt_BottonFrame, width=350, height=300, font=('arial', 12, 'bold'),
                                  text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0)

        ButtonFrame = LabelFrame(Receipt_BottonFrame, width=350, height=100, relief=RIDGE)
        ButtonFrame.grid(row=1, column=0)
        # =========================================================CustomerName====================================================

        self.lblFirstname = Label(CustomerName, font=('arial', 14, ), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                                  justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1, padx=5)

        self.lblSurname = Label(CustomerName, font=('arial', 14 ), text="Surname", bd=7)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                                justify=RIGHT)
        self.txtSurname.grid(row=1, column=1, sticky=W, padx=5)

        self.lblAddress = Label(CustomerName, font=('arial', 14), text="Address", bd=7)
        self.lblAddress.grid(row=2, column=0, sticky=W)
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Address, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                                justify=RIGHT)
        self.txtAddress.grid(row=2, column=1, padx=5)

        self.lblPostcode = Label(CustomerName, font=('arial', 14), text="Postcode", bd=7)
        self.lblPostcode.grid(row=3, column=0, sticky=W)
        self.txtPostcode = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Postcode, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                                 justify=RIGHT)
        self.txtPostcode.grid(row=3, column=1, padx=5)

      
        self.lblTelephone = Label(CustomerName, font=('arial', 14), text="Mobile no.", bd=7)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Telephone, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                                  justify=RIGHT)
        self.txtTelephone.grid(row=5, column=1, padx=5)

        self.lblEmail = Label(CustomerName, font=('arial', 14), text="Email", bd=7)
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Email, bd=7, insertwidth=2, relief=SOLID, borderwidth=1,
                              justify=RIGHT)
        self.txtEmail.grid(row=6, column=1, padx=5)

        # ===============================================Taxi Information==============================================================
        self.lblPickup = Label(TravelFrame, font=('arial', 14), text="Pickup", bd=7)
        self.lblPickup.grid(row=0, column=0, sticky=W)

        self.cboPickup = ttk.Combobox(TravelFrame, textvariable=varl1, state='readonly', font=('arial', 20),
                                      width=14)
        self.cboPickup['value'] = ('', 'Amritsar', 'Ludhiana', 'Pathankot', 'Sangrur')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0, column=1)

        self.lblDrop = Label(TravelFrame, font=('arial', 14), text="Drop", bd=7)
        self.lblDrop.grid(row=1, column=0, sticky=W)

        self.cboDrop = ttk.Combobox(TravelFrame, textvariable=varl2, state='readonly', font=('arial', 20),
                                    width=14)
        self.cboDrop['value'] = ('', 'Amritsar', 'Ludhiana', 'Pathankot', 'Sangrur')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1, column=1)

        self.lblPooling = Label(TravelFrame, font=('arial', 14), text="Pooling", bd=7)
        self.lblPooling.grid(row=2, column=0, sticky=W)

        self.cboPooling = ttk.Combobox(TravelFrame, textvariable=varl3, state='readonly', font=('arial', 20),
                                       width=14)
        self.cboPooling['value'] = ('', '1', '2', '3', '4')
        self.cboPooling.current(1)
        self.cboPooling.grid(row=2, column=1)

        # ===============================================Taxi Information==============================================================

        self.chkTaxiTax = Checkbutton(TravelFrame, text="Taxi Tax(Base Charge) *", variable=var1, onvalue=1, offvalue=0,
                                      font=('arial', 14), command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=TaxiTax, bd=6, width=18,
                                bg="white", state=DISABLED, justify=RIGHT, relief=GROOVE)
        self.txtTaxiTax.grid(row=3, column=1, padx=5)

        self.chkKm = Checkbutton(TravelFrame, text="Distance(KMs) *", variable=var2, onvalue=1, offvalue=0,
                                 font=('arial', 14), command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Km, bd=6, width=18, bg="white",
                           state=DISABLED, justify=RIGHT, relief=SUNKEN, highlightthickness=0)
        self.txtKm.grid(row=4, column=1, padx=5)

        self.chkTravel_Ins = Checkbutton(TravelFrame, text="Travelling Insurance *", variable=var3, onvalue=1,
                                         offvalue=0, font=('arial', 14), command=Travelling).grid(row=5,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.txtTravel_Ins = Label(TravelFrame, font=('arial', 16), textvariable=Travel_Ins, bd=6, width=18,
                                   bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTravel_Ins.grid(row=5, column=1, padx=5, pady=5)


        # =================================payment information ===========================================================================

        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Paid Tax\t\t", bd=7)
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, width=26,
                                justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPaidTax.grid(row=0, column=3, padx=5)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Sub Total", bd=7)
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, width=26,
                                 justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1, column=3, padx=5)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, width=26,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2, column=3, padx=5)

        # ==========================================================taxiselect=======================================================================

        # =======================================Recipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)

        # ======================================Button========================================================================================

        self.btnTotal = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Total',
                               command=Total_Paid).grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Receipt',
                                 command=Receiptt).grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Reset',
                               command=Reset).grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Exit',
                              command=iExit).grid(row=0, column=3)

    # ====================================================================================================================================


if __name__ == '__main__':
    root = Tk()

    # =========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = "%dx%d+%d+%d" % (w, h, 0, 0)

    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()


