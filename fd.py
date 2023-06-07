from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from PIL import Image, ImageTk
from tkinter import messagebox


class FD:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x600+230+220")
        self.root.title("FD")

        # -----Variables------
        self.var_Ref_Id = StringVar()
        x = random.randint(980020, 980999)
        self.var_Ref_Id.set(str(x))


        self.var_Name = StringVar()
        self.var_Age = StringVar()
        self.var_DOB = StringVar()
        self.var_Address = StringVar()
        self.var_Mobile = StringVar()
        self.var_Email = StringVar()
        self.var_IdProof = StringVar()
        self.var_IdNumber = StringVar()
        self.var_Tenure = StringVar()
        self.var_Amount = StringVar()
        self.var_Date_Of_Issuing = StringVar()
        self.var_Date_Of_Returning = StringVar()
        self.var_ROI = StringVar()


        #-----title----------
        lbl_title = Label(self.root, text="FIXED DEPOSIT", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=70)

        # ---------Logo--------------------
        img2 = Image.open('E:\\python project\\images\\kc.jpg')
        img2 = img2.resize((150, 70), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.bg1, bd=4, relief=RIDGE)
        label.place(x=0, y=0, width=150, height=70)

        # ---------Label Frame----------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("times new roman", 9, "bold"), padx=3)
        labelframeleft.place(x=5, y=70, width=370, height=525)

        # -------Labels and Entry-----------
        # RefId
        lbl_Ref_Id = Label(labelframeleft, text="Ref Id", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Ref_Id.grid(row=0, column=0, sticky=W)

        enty_Ref_Id = ttk.Entry(labelframeleft,textvariable=self.var_Ref_Id, width=20, font=("arial", 9, "bold"),
                            state="readonly")
        enty_Ref_Id.grid(row=0, column=1,sticky=W)
        # Name
        lbl_name = Label(labelframeleft, text="Name :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_name.grid(row=1, column=0, sticky=W)

        enty_name = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Name,font=("arial", 9, "bold"))
        enty_name.grid(row=1, column=1,sticky=W)

        # Age
        lbl_Age = Label(labelframeleft, text="Age :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Age.grid(row=2, column=0, sticky=W)

        enty_Age = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Age, font=("arial", 9, "bold"))
        enty_Age.grid(row=2, column=1)

        # DOB
        lbl_DOB = Label(labelframeleft, text="DOB :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_DOB.grid(row=3, column=0, sticky=W)

        enty_DOB = ttk.Entry(labelframeleft, width=29,textvariable=self.var_DOB, font=("arial", 9, "bold"))
        enty_DOB.grid(row=3, column=1)

        # Address
        lbls_Address = Label(labelframeleft, text="Address :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbls_Address.grid(row=4, column=0, sticky=W)

        entys_Address = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Address, font=("arial", 9, "bold"))
        entys_Address.grid(row=4, column=1)

        # Mobile Number
        lbl_Mobile = Label(labelframeleft, text="Mobile Number :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Mobile.grid(row=5, column=0, sticky=W)

        txt_Mobile = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Mobile, font=("arial", 9, "bold"))
        txt_Mobile.grid(row=5, column=1)

        # Email
        lbl_Email = Label(labelframeleft, text="Email :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Email.grid(row=6, column=0, sticky=W)

        txt_Email = ttk.Entry(labelframeleft,textvariable=self.var_Email, width=29, font=("arial", 9, "bold"))
        txt_Email.grid(row=6, column=1)


        # id proof
        lbl_IdProof = Label(labelframeleft, text="Id Proof Type :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_IdProof.grid(row=7, column=0, sticky=W)

        combos_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_IdProof, font=("arial",9, "bold"),
                                     width=27, state="readonly")
        combos_IdProof["value"] = ("Aadhar Card", "Pan Card", "Driving Licence", "Passport", "Ration Card", "Voter Id")
        combos_IdProof.current(1)
        combos_IdProof.grid(row=7, column=1)

        # id number
        lbl_IdNumber = Label(labelframeleft, text="Id Number :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_IdNumber.grid(row=8, column=0, sticky=W)

        txt_IdNumber = ttk.Entry(labelframeleft,textvariable=self.var_IdNumber, width=29, font=("arial", 9, "bold"))
        txt_IdNumber.grid(row=8, column=1)

        # TENURE
        lbl_Tenure = Label(labelframeleft, text="Tenure :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Tenure.grid(row=9, column=0, sticky=W)

        combos_Tenure = ttk.Combobox(labelframeleft,textvariable=self.var_Tenure, font=("arial", 9, "bold"), width=27,
                                       state="readonly")
        combos_Tenure["value"] = (
        "2 years", "3 years", "4 years", "5 years")
        combos_Tenure.current(2)
        combos_Tenure.grid(row=9, column=1)


        #Amount
        lbl_Amount = Label(labelframeleft, text="Amount :", font=("arial", 8, "bold"), padx=2, pady=6)
        lbl_Amount.grid(row=10, column=0, sticky=W)

        txt_Amount = ttk.Entry(labelframeleft,textvariable=self.var_Amount, width=29, font=("arial", 9, "bold"))
        txt_Amount.grid(row=10, column=1)


        # Date Of Issuing
        lbl_Date_Of_Issuing = Label(labelframeleft, text="Date Of Issuing :", font=("arial", 8, "bold"), padx=2,
                                      pady=6)
        lbl_Date_Of_Issuing.grid(row=13, column=0, sticky=W)

        txt_Date_Of_Issuing = ttk.Entry(labelframeleft,textvariable=self.var_Date_Of_Issuing,width=29, font=("arial", 9, "bold"))
        txt_Date_Of_Issuing.grid(row=13, column=1)

        # Date Of Returning
        lbl_Date_Of_Returning = Label(labelframeleft, text="Date Of Returning :", font=("arial", 8, "bold"), padx=2,
                                    pady=6)
        lbl_Date_Of_Returning.grid(row=14, column=0, sticky=W)

        txt_Date_Of_Returning = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Date_Of_Returning, font=("arial", 9, "bold"))
        txt_Date_Of_Returning.grid(row=14, column=1)

        # Interest
        lbl_ROI = Label(labelframeleft, text="Rate Of Interest  :", font=("arial", 8, "bold"), padx=2,
                                      pady=6)
        lbl_ROI.grid(row=15, column=0, sticky=W)

        txt_ROI = ttk.Entry(labelframeleft, width=20,textvariable=self.var_ROI, font=("arial", 9, "bold"),state="readonly")
        txt_ROI.grid(row=15, column=1,sticky=W)


        #------Fetch Data Button-----
        # Fetch
        btnFetch = Button(labelframeleft, text="Fetch", font=("arial", 9, "bold"), bg="black",
                         fg="gold", width=6)
        btnFetch.place(x=300,y=3)

        # ------ROI Button-----
        # ROI
        btnROI = Button(labelframeleft, text="Calculate", font=("arial", 9, "bold"),command=self.ROIs ,bg="black",
                          fg="gold", width=7)
        btnROI.place(x=290, y=400)

        # ---------Button---------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=480, width=412, height=30)

        # Save
        btnSave = Button(btn_frame, text="Save",font=("arial", 9, "bold"),command=self.save_data, bg="black",
                         fg="gold", width=8)
        btnSave.grid(row=0, column=0, padx=1)

        # update
        btnUpdate = Button(btn_frame, text="Update",font=("arial", 9, "bold"),command=self.update, bg="black",
                           fg="gold", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        # Delete
        btnDelete = Button(btn_frame, text="Delete",font=("arial", 9, "bold"),command=self.mDelete, bg="black",
                           fg="gold", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        # reset
        btnReset = Button(btn_frame, text="Reset",font=("arial", 9, "bold"),command=self.reset, bg="black",
                          fg="gold", width=8)
        btnReset.grid(row=0, column=3, padx=1)

        # -----------Right Side Image------------------
        img3 = Image.open('E:\\python project\\images\\fd.jpg')
        img3 = img3.resize((500,270))
        self.bg2 = ImageTk.PhotoImage(img3)
        label = Label(self.root, image=self.bg2, bd=4, relief=RIDGE)
        label.place(x=760, y=70, width=500, height=270)

        # -----------Right Side Image------------------
        img4 = Image.open('E:\\python project\\images\\fd.jpg')
        img4 = img4.resize((150, 150))
        self.bg3 = ImageTk.PhotoImage(img4)
        label = Label(self.root, image=self.bg3, bd=4, relief=RIDGE)
        label.place(x=460, y=70, width=150, height=150)

        # -------tabel frame----------

        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                 font=("times new roman", 12, "bold"), padx=3)
        Table_frame.place(x=420, y=280, width=860, height=290)

        lblSearchBy = Label(Table_frame, text="Search By :", font=("arial", 8, "bold"), bg="red", fg="white", padx=2,
                            pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=3)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_frame, textvariable=self.search_var, font=("arial", 9, "bold"), width=27,
                                    state="readonly")
        combo_Search["value"] = ("Ref_Id", "Mobile", "IdNumber","Tenure")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=3)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(Table_frame, textvariable=self.txt_search, width=24, font=("arial", 9, "bold"))
        txtSearch.grid(row=0, column=2, padx=3)

        btnSearch = Button(Table_frame, text="Search",command=self.search, font=("arial", 10, "bold"), bg="black",
                           fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=3)

        btnShowAll = Button(Table_frame, text="Show All",command=self.fetch_data, font=("arial", 10, "bold"),
                            bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=3)

        # -----SHOW DATA--------
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=860, height=210)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_Details_Table = ttk.Treeview(details_table, columns=("Ref_Id", "Name", "Age", "DOB","Address",
                                                                       "Income", "Mobile", "Email", "IdProof",
                                                                       "IdNumber", "Tenure", "Amount",
                                                                       "Date_Of_Issuing","Date_Of_Returning",
                                                                       "ROI")
                                               , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("Ref_Id", text="Ref. Number")
        self.cust_Details_Table.heading("Name", text="Name")
        self.cust_Details_Table.heading("Age", text="Age")
        self.cust_Details_Table.heading("DOB", text="D.O.B")
        self.cust_Details_Table.heading("Address", text="Address")
        self.cust_Details_Table.heading("Income", text="Income")
        self.cust_Details_Table.heading("Mobile", text="Mobile No.")
        self.cust_Details_Table.heading("Email", text="Email")
        self.cust_Details_Table.heading("IdProof", text="Id Proof")
        self.cust_Details_Table.heading("IdNumber", text="Id Number")
        self.cust_Details_Table.heading("Tenure", text="Tenure")
        self.cust_Details_Table.heading("Amount", text="Amount")
        self.cust_Details_Table.heading("Date_Of_Issuing", text="Date Of Issuing")
        self.cust_Details_Table.heading("Date_Of_Returning", text="Date Of Returning")
        self.cust_Details_Table.heading("ROI", text="Rate Of Interest")

        self.cust_Details_Table["show"] = "headings"

        self.cust_Details_Table.column("Name", width=100)
        self.cust_Details_Table.column("Ref_Id",width=100)
        self.cust_Details_Table.column("Age",width=100)
        self.cust_Details_Table.column("DOB", width=100)
        self.cust_Details_Table.column("Address", width=100)
        self.cust_Details_Table.column("Income",width=100)
        self.cust_Details_Table.column("Mobile", width=100)
        self.cust_Details_Table.column("Email", width=100)
        self.cust_Details_Table.column("IdProof", width=100)
        self.cust_Details_Table.column("IdNumber", width=100)
        self.cust_Details_Table.column("Tenure", width=100)
        self.cust_Details_Table.column("Amount", width=100)
        self.cust_Details_Table.column("Date_Of_Issuing", width=100)
        self.cust_Details_Table.column("Date_Of_Returning",width=100)
        self.cust_Details_Table.column("ROI", width=100)

        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def save_data(self):
        if self.var_Tenure.get()=="" or self.var_Amount.get()==""or self.var_Mobile.get()==""or self.var_IdNumber.get()==""or self.var_Date_Of_Returning.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HardikJain@090104",database="banking_managementdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into new_fd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_Ref_Id.get(),self.var_Name.get(),self.var_Age.get(),self.var_DOB.get(),
                    self.var_Address.get(),self.var_Mobile.get(),self.var_Email.get(),
                    self.var_IdProof.get(),self.var_IdNumber.get(),self.var_Tenure.get(),self.var_Amount.get(),
                    self.var_Date_Of_Issuing.get(),self.var_Date_Of_Returning.get(),self.var_ROI.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Account Successfully Created","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some Thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                       database="banking_managementdb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from new_fd")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Ref_Id.set(row[0])
        self.var_Name.set(row[1])
        self.var_Age.set(row[2])
        self.var_DOB.set(row[3])
        self.var_Address.set(row[4])
        self.var_Mobile.set(row[5])
        self.var_Email.set(row[6])
        self.var_IdProof.set(row[7])
        self.var_IdNumber.set(row[8])
        self.var_Tenure.set(row[9])
        self.var_Amount.set(row[10])
        self.var_Date_Of_Issuing.set(row[11])
        self.var_Date_Of_Returning.set(row[12])
        self.var_ROI.set(row[13])

    def update(self):
        if self.var_IdNumber.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                               database="banking_managementdb")
                my_cursor = conn.cursor()
                my_cursor.execute("update new_fd set Name=%s,Age=%s,DOB=%s,Address=%sMobile=%s,Email=%s,"
                                  "IdProof=%s,IdNumber=%s,Tenure=%s,Amount=%s,"
                                  "Date_Of_Issuing=%s,Date_Of_Returning=%s,ROI=%s where Ref_Id=%s",(
                    self.var_Name.get(), self.var_Age.get(), self.var_DOB.get(),
                    self.var_Address.get(), self.var_Mobile.get(), self.var_Email.get(),
                    self.var_IdProof.get(), self.var_IdNumber.get(), self.var_Tenure.get(), self.var_Amount.get(),
                    self.var_Date_Of_Issuing.get(), self.var_Date_Of_Returning.get(), self.var_ROI.get(),self.var_Ref_Id.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Customer Details has been Updated Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some Thing went wrong:{str(es)}", parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Deletetion","Do You Want to Delete This Customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            query="delete from new_fd where Ref_Id=%s"
            value=(self.var_Ref_Id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_Ref_Id.set(""),
        self.var_Name.set(""),
        self.var_Age.set(""),
        self.var_DOB.set(""),
        self.var_Address.set(""),
        self.var_Mobile.set(""),
        self.var_Email.set(""),
        self.var_IdNumber.set(""),
        self.var_Amount.set(""),
        self.var_Date_Of_Issuing.set(""),
        self.var_Date_Of_Returning.set(""),
        self.var_ROI.set("")

        x = random.randint(980020, 980999)
        self.var_Ref_Id.set(str(x))



    def search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                               database="banking_managementdb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from new_fd where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len (rows)!=0:
                    self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
                    for i in rows:
                        self.cust_Details_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Some Thing went wrong:{str(es)}", parent=self.root)

    def ROIs(self):
        if (self.var_Tenure.get()=="2 years"):
            q1="6%"
            self.var_ROI.set(str(q1))


        elif(self.var_Tenure.get()=="3 years"):
            q1 = "6.5%"
            self.var_ROI.set(str(q1))

        elif (self.var_Tenure.get() == "4 years"):
            q1 = "7%"
            self.var_ROI.set(str(q1))

        elif (self.var_Tenure.get() == "5 years"):
            q1 = "8%"
            self.var_ROI.set(str(q1))

        elif (self.var_Tenure.get() == "more"):
            q1 = "9%"
            self.var_ROI.set(str(q1))





if __name__ == '__main__':
    root=Tk()
    obj=FD(root)
    root.mainloop()
