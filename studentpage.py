if self.var_mobile.get() == "":
    messagebox.showerror("Error", "Please Enter the Mobile Number", parent=self.root)
else:
    conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                   database="banking_managementdb")
    my_cursor = conn.cursor()
    my_cursor.execute(
        "update new_acc set Name=%s,Father=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s,TypeOfAcc=%s,Gender=%s where AccountNumber=%s",
        (

            self.var_cust_name.get(), self.var_father.get(), self.var_postal.get(),
            self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(),
            self.var_id_number.get(), self.var_address.get(), self.var_type_of_Acc.get(), self.var_gender.get(),
            self.var_acc.get()
        ))
    conn.commit()
    self.fetch_data()
    conn.close()
    messagebox.showinfo("Update", "Your Details has been Updated", parent=self.root)



from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql

class AccOpenPageClass:
    def __init__(self,hp_window):
        # self.window = Tk()   #To create independent window
        # self.window = hp_window  # now self.window(studentpage) is same as hp_window(homepage)

        self.window=Toplevel(hp_window) #now hp_window(homepage) will acts as parent window to self.window(studentpage)

        self.window.title("Institute Manager/Student")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()

        w1 = self.w -100
        h1 = self.h -150

        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
        self.window.minsize(w1, h1)

        #---------------------widgets ----------------
        mycolor1 = "#E7E6FC"
        mycolor2 = "#2C22FE"
        mycolor3 = "white"
        myfont1 = ("Cambria",15)

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="Student",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")



        self.L1 =Label(self.window,text="Name",background=mycolor1,font=myfont1)
        self.L2 =Label(self.window,text="Pan",background=mycolor1,font=myfont1)
        self.L3 =Label(self.window,text="Aadhar",background=mycolor1,font=myfont1)
        self.L4 =Label(self.window,text="Gender",background=mycolor1,font=myfont1)
        self.L5 =Label(self.window,text="DOB",background=mycolor1,font=myfont1)
        self.L6 =Label(self.window,text="Address",background=mycolor1,font=myfont1)
        self.L7 =Label(self.window,text="Type of Acc.",background=mycolor1,font=myfont1)
        self.L8 =Label(self.window,text="phone",background=mycolor1,font=myfont1)


        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1)
        self.t3 = Entry(self.window,font=myfont1)
        self.t8 = Entry(self.window, font=myfont1)
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window,text="Male",value="Male",variable=self.v1,font=myfont1,background=mycolor1)
        self.r2 = Radiobutton(self.window,text="Female",value="Female",variable=self.v1,font=myfont1,background=mycolor1)

        self.t5 = Entry(self.window,font=myfont1)
        self.t6 = Text(self.window,font=myfont1,width=20,height=3)
        self.v2=StringVar()
        self.c1 = Combobox(self.window,values=["Saving","Current"],textvariable=self.v2,state="readonly",font=myfont1)


        #----------- buttons -----------------------
        self.b1 = Button(self.window,text="Save",foreground=mycolor3,background=mycolor2,font=myfont1,command=self.saveData)
        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L4.place(x=x1,y=y1)
        self.r1.place(x=x1+h_diff,y=y1)
        self.r2.place(x=x1+h_diff+h_diff,y=y1)
        y1+=v_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        y1+=v_diff
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L8.place(x=x1,y=y1)
        self.t8.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1)

        self.databaseconnection()
        self.window.mainloop()

    def databaseconnection(self):
        myhost="localhost"
        mydb="bankingdb"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ","Error in Database Connection: \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            qry = "insert into Acc_open values(%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get(),self.t6.get('1.0',END), self.v2.get(),self.t8.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Acc Added Successfully",parent=self.window)


        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)





if __name__ == '__main__':
    dummyHomepage=Tk()
    AccOpenPageClass(dummyHomepage)
    dummyHomepage.mainloop()