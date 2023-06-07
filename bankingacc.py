from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from PIL import Image, ImageTk
from tkinter import messagebox



class BankingAccount:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x600+230+220")
        self.root.title("Bank Account")

        #-----Variables------
        self.var_acc=StringVar()
        x=random.randint(40932000000,40932999999)
        self.var_acc.set(str(x))

        self.var_cust_name = StringVar()
        self.var_father = StringVar()
        self.var_postal = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_type_of_Acc = StringVar()
        self.var_gender = StringVar()



        #-----title----------
        lbl_title = Label(self.root, text="ACCOUNT OPENING", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=70)

        # ---------Logo--------------------
        img2 = Image.open('E:\\python project\\images\\kc.jpg')
        img2 = img2.resize((150, 70), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.bg1, bd=4, relief=RIDGE)
        label.place(x=0, y=0, width=150, height=70)


        #---------Label Frame----------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=3)
        labelframeleft.place(x=5,y=70,width=425,height=490)

        #-------Labels and Entry-----------
        # Account Number
        lbl_acc_no=Label(labelframeleft,text="Account Number",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_acc_no.grid(row=0,column=0,sticky=W)

        enty_no=ttk.Entry(labelframeleft,width=29,textvariable=self.var_acc,font=("arial",13,"bold"),state="readonly")
        enty_no.grid(row=0,column=1)

        # Cust Name
        cname = Label(labelframeleft, text="Customer Name :", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29,textvariable=self.var_cust_name, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Father Name
        lblmname = Label(labelframeleft, text="Father's Name :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, width=29,textvariable=self.var_father, font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        #Gender Combobox
        label_gender = Label(labelframeleft, text="Sex", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial", 13, "bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(2)
        combo_gender.grid(row=3,column=1)

        #Postal Code
        lblPostalCode = Label(labelframeleft, text="Postal Code :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostalCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, width=29,textvariable=self.var_postal, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        #Mobile Number
        lblMobile = Label(labelframeleft, text="Mobile Number :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, width=29,textvariable=self.var_mobile, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        #Email
        lblEmail = Label(labelframeleft, text="Email :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, width=29,textvariable=self.var_email, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, text="Nationality :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("Indian", "American", "British","French","African","Chinese")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # id proof
        lblIdProof = Label(labelframeleft, text="Id Proof Type :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_IdProof["value"] = ("Aadhar Card", "Pan Card", "Driving Licence","Passport","Ration Card","Voter Id")
        combo_IdProof.current(1)
        combo_IdProof.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, text="Id Number :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, width=29,textvariable=self.var_id_number, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text="Address :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft, width=29,textvariable=self.var_address, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)

        # Type of Acc
        lblTypeAcc = Label(labelframeleft, text="Type of Account :", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTypeAcc.grid(row=11, column=0, sticky=W)

        combo_TypeAcc = ttk.Combobox(labelframeleft,textvariable=self.var_type_of_Acc, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_TypeAcc["value"] = ("Saving Acc.","Current Acc.")
        combo_TypeAcc.current(0)
        combo_TypeAcc.grid(row=11, column=1)


        #---------Button---------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=37)

        #Save
        btnSave=Button(btn_frame,text="Save",command=self.save_data,font=("arial", 12, "bold"),bg="black",fg="gold",width=9)
        btnSave.grid(row=0,column=0,padx=1)

        #update
        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold",width=9)
        btnUpdate.grid(row=0, column=1,padx=1)

        #Delete
        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold",width=9)
        btnDelete.grid(row=0, column=2,padx=1)

        #reset
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold",width=9)
        btnReset.grid(row=0, column=3,padx=1)

        # -----------Right Side Image------------------
        img3 = Image.open('E:\\python project\\images\\account.jpg')
        img3 = img3.resize((500, 270))
        self.bg2 = ImageTk.PhotoImage(img3)
        label = Label(self.root, image=self.bg2, bd=4, relief=RIDGE)
        label.place(x=760, y=70, width=500, height=270)


        #-------tabel frame----------

        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                    font=("times new roman", 12, "bold"), padx=3)
        Table_frame.place(x=420, y=280, width=860, height=290)

        lblSearchBy = Label(Table_frame, text="Search By :", font=("arial", 13, "bold"),bg="red",fg="white", padx=2, pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=3)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_frame, textvariable=self.search_var,font=("arial", 13, "bold"), width=27, state="readonly")
        combo_Search["value"] = ("AccountNumber", "Mobile","IdNumber","Nationality","TypeOfAcc","Gender")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=3)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(Table_frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2,padx=3)

        btnSearch = Button(Table_frame, text="Search",command=self.search, font=("arial", 13, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=3)

        btnShowAll = Button(Table_frame, text="Show All",command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=3)


        #-----SHOW DATA--------
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=860, height=405)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_Details_Table=ttk.Treeview(details_table,columns=("AccountNumber","Name","Father","Postal",
                                                                    "Mobile","Email","Nationality","IdProof","IdNumber","Address","TypeOfAcc","Gender")
                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("AccountNumber", text="Account Number")
        self.cust_Details_Table.heading("Name", text="Customer Name")
        self.cust_Details_Table.heading("Father", text="father's Name")
        self.cust_Details_Table.heading("Postal", text="Postal Code")
        self.cust_Details_Table.heading("Mobile", text="Mobile No.")
        self.cust_Details_Table.heading("Email", text="Email")
        self.cust_Details_Table.heading("Nationality", text="Nationality")
        self.cust_Details_Table.heading("IdProof", text="Id Proof")
        self.cust_Details_Table.heading("IdNumber", text="Id Number")
        self.cust_Details_Table.heading("Address", text="Address")
        self.cust_Details_Table.heading("TypeOfAcc", text="Type Of Account")
        self.cust_Details_Table.heading("Gender", text="Gender")

        self.cust_Details_Table["show"] = "headings"

        self.cust_Details_Table.column("AccountNumber", width=100)
        self.cust_Details_Table.column("Name", width=100)
        self.cust_Details_Table.column("Father", width=100)
        self.cust_Details_Table.column("Postal", width=100)
        self.cust_Details_Table.column("Mobile", width=100)
        self.cust_Details_Table.column("Email", width=100)
        self.cust_Details_Table.column("Nationality", width=100)
        self.cust_Details_Table.column("IdProof", width=100)
        self.cust_Details_Table.column("IdNumber", width=100)
        self.cust_Details_Table.column("Address", width=100)
        self.cust_Details_Table.column("TypeOfAcc", width=100)
        self.cust_Details_Table.column("Gender", width=100)

        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def save_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()==""or self.var_id_number.get()==""or self.var_id_number.get()==""or self.var_postal.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HardikJain@090104",database="banking_managementdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into new_acc values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_acc.get(),self.var_cust_name.get(),self.var_father.get(),self.var_postal.get(),
                    self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),
                    self.var_id_number.get(),self.var_address.get(),self.var_type_of_Acc.get(),self.var_gender.get()
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
        my_cursor.execute("select * from new_acc")
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

        self.var_acc.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_postal.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])
        self.var_type_of_Acc.set(row[10])
        self.var_gender.set(row[11])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            my_cursor.execute("update new_acc set Name=%s,Father=%s,Postal=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s,TypeOfAcc=%s,Gender=%s where AccountNumber=%s",(
                                                                                            self.var_cust_name.get(),
                                                                                            self.var_father.get(),
                                                                                            self.var_postal.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_id_proof.get(),
                                                                                            self.var_id_number.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_type_of_Acc.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_acc.get()
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been Updated Sucessfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Deletetion","Do You Want to Delete This Customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="banking_managementdb")
            my_cursor = conn.cursor()
            query="delete from new_acc where AccountNumber=%s"
            value=(self.var_acc.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        #self.var_acc.set(""),
        self.var_cust_name.set(""),
        self.var_father.set(""),
        self.var_postal.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        #self.var_type_of_Acc.set(r""),
        #self.var_gender.set(r"")

        x = random.randint(40932000000, 40932999999)
        self.var_acc.set(str(x))



    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                       database="banking_managementdb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from new_acc where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()










if __name__ == '__main__':
    root=Tk()
    obj=BankingAccount(root)
    root.mainloop()
