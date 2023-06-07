from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
from PIL import Image,ImageTk

class StudentPageClass:
    default_img_name = "default_user.png"
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

        #----------------- background image ----------------------------
        from PIL import Image,ImageTk
        self.bkimg1 = Image.open("my_images//blue_bg7_2.jpg").resize((w1,h1))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)

        # ---------------------------------------------------------------
        #---------------------widgets ----------------
        mycolor1 = "#E7E6FC"
        mycolor2 = "#2C22FE"
        mycolor3 = "white"
        myfont1 = ("Cambria",15)

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="Student",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="Roll no",background=mycolor1,font=myfont1)
        self.L2 =Label(self.window,text="Name",background=mycolor1,font=myfont1)
        self.L3 =Label(self.window,text="Phone",background=mycolor1,font=myfont1)
        self.L4 =Label(self.window,text="Gender",background=mycolor1,font=myfont1)
        self.L5 =Label(self.window,text="DOB",background=mycolor1,font=myfont1)
        self.L6 =Label(self.window,text="Address",background=mycolor1,font=myfont1)
        self.L7 =Label(self.window,text="Department",background=mycolor1,font=myfont1)
        self.L8 =Label(self.window,text="Course",background=mycolor1,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1)
        self.t3 = Entry(self.window,font=myfont1)
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window,text="Male",value="Male",variable=self.v1,font=myfont1,background=mycolor1)
        self.r2 = Radiobutton(self.window,text="Female",value="Female",variable=self.v1,font=myfont1,background=mycolor1)

        self.t5 = DateEntry(self.window,  background='darkblue',
                    foreground='white', borderwidth=2, year=2010,date_pattern='y-mm-dd',font=myfont1)
        self.t6 = Text(self.window,font=myfont1,width=20,height=3)
        self.v2=StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v2,state="readonly",font=myfont1)
        self.c1.bind("<<ComboboxSelected>>",lambda e: self.getAllCourse())
        self.v3=StringVar()
        self.c2 = Combobox(self.window,textvariable=self.v3,state="readonly",font=myfont1)

        #------------ table ---------------------------

        self.mytable1 = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8'],height=12)

        self.mytable1.heading("c1",text="Roll no")
        self.mytable1.heading("c2",text="Name")
        self.mytable1.heading("c3",text="Phone")
        self.mytable1.heading("c4",text="Gender")
        self.mytable1.heading("c5",text="DOB")
        self.mytable1.heading("c6",text="Address")
        self.mytable1.heading("c7",text="Department")
        self.mytable1.heading("c8",text="Course")

        self.mytable1['show']='headings'
        self.mytable1.column("#1",width=100,anchor="center")
        self.mytable1.column("#2",width=100,anchor="center")
        self.mytable1.column("#3",width=100,anchor="center")
        self.mytable1.column("#4",width=100,anchor="center")
        self.mytable1.column("#5",width=100,anchor="center")
        self.mytable1.column("#6",width=100,anchor="center")
        self.mytable1.column("#7",width=100,anchor="center")
        self.mytable1.column("#8",width=100,anchor="center")

        self.mytable1.bind("<ButtonRelease>",lambda e: self.getpkValue())

        #----------- buttons -----------------------
        self.b1 = Button(self.window,text="Save",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)
        self.b2 = Button(self.window,text="Fetch",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.fetchData)
        self.b3 = Button(self.window,text="update",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.updateData)
        self.b4 = Button(self.window,text="Delete",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.deleteData)
        self.b5 = Button(self.window,text="Search",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.searchData)
        self.b6 = Button(self.window,text="Upload",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.getImage)

        self.imglbl = Label(self.window,relief="groove",borderwidth=1)
        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
        self.b2.place(x=x1+h_diff+250,y=y1,height=30)
        self.mytable1.place(x=x1+h_diff+350,y=y1)
        y1+=v_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+h_diff,y=y1)
        self.b5.place(x=x1+h_diff+250,y=y1,height=30)
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
        self.c2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1,height=40,width=100)
        self.b3.place(x=x1+110,y=y1,height=40,width=100)
        self.b4.place(x=x1+220,y=y1,height=40,width=100)

        self.imglbl.place(x=x1+520,y=y1-150,height=150,width=150)
        self.b6.place(x=x1+520,y=y1,height=40,width=150)
        self.databaseconnection()
        self.clearPage()
        self.getAllDepartment()
        self.window.mainloop()

    def getImage(self):
        self.filename = askopenfilename(file=[("All Pictures","*.png;*.jpg;*.jpeg"),
                        ("PNG Images","*.png"),("JPG Images","*.jpg")],parent=self.window)
        print("Filename = ",self.filename)

        if self.filename!="":
            self.img1 = Image.open(self.filename).resize((150,150))
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)

            # make image name
            path = self.filename.split("/")
            # print("Path = ",path)
            name = path[-1]
            # print("Name = ",name)
            import time
            uniqness = str(int(time.time()))
            # print("uniqness = ",uniqness)
            self.actualname = uniqness+name
            # print("actual name = ",self.actualname)

    def databaseconnection(self):
        myhost="localhost"
        mydb="institutemanagerdb"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ","Error in Database Connection: \n"+str(e),parent=self.window)

    def saveData(self):
        if self.checkValidation()==False:
            return # end function now

        if self.actualname==self.default_img_name: # no new img is selected
            # nothing to save in folder
            pass
        else: # image is selected
            self.img1.save("student_images//"+self.actualname)

        try:
            qry = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get_date(),self.t6.get('1.0',END), self.v2.get(),
                                              self.v3.get(),self.actualname))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Student Added Successfully",parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def updateData(self):
        if self.checkValidation()==False:
            return # end function now

        if self.actualname==self.oldname: # no new image is selected
            # nothing to save or delete in folder
            pass
        else:
            self.img1.save("student_images//"+self.actualname)
            if self.oldname==self.default_img_name: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("student_images//"+self.oldname)
        try:
            qry = "update student set name=%s, phone=%s , gender=%s , dob=%s, address=%s, " \
                  "department=%s , course=%s , pic =%s where rollno=%s"
            rowcount = self.curr.execute(qry,(self.t2.get(),self.t3.get(),
                    self.v1.get(),self.t5.get_date(),self.t6.get('1.0',END),
                        self.v2.get(),self.v3.get(),self.actualname, self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Student Updated Successfully",parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you to delete ?",parent=self.window)
        if (ans=="yes"):

            if self.oldname==self.default_img_name: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("student_images//"+self.oldname)
            try:
                qry = "delete from student where rollno=%s"
                rowcount = self.curr.execute(qry,(self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","Student deleted Successfully",parent=self.window)
                    self.clearPage()

            except Exception as e:
                messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getpkValue(self):
        rowID = self.mytable1.focus()
        # print("row id = ",rowID)
        data = self.mytable1.item(rowID)
        # print("Data = ",data)
        mycontent = data['values']
        # print("mycontent = ",mycontent)
        pkValue = mycontent[0]
        # print("Rollno = ",pkValue)
        self.fetchData(pkValue)

    def fetchData(self,pk_value=None):
        if pk_value==None:
            rollno=self.t1.get()
        else:
            rollno=pk_value
        try:
            qry = "select * from student where rollno = %s"
            rowcount = self.curr.execute(qry,(rollno))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.t3.insert(0,data[2])
                self.v1.set(data[3])
                self.t5.set_date(data[4])
                self.t6.insert('1.0',data[5])
                self.v2.set(data[6])
                self.v3.set(data[7])
                self.actualname=data[8]
                self.oldname = data[8]

                self.img1 = Image.open("student_images//" + self.oldname).resize((150, 150))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

                self.b3['state'] = 'normal'
                self.b4['state'] = 'normal'
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)
        self.v1.set(None)
        self.t5.delete(0,END)
        self.t6.delete('1.0',END)
        self.c1.set("Choose Department")
        self.c2.set("Choose Course")
        self.b3['state']='disable'
        self.b4['state']='disable'
        self.actualname=self.default_img_name
        self.img1 = Image.open("student_images//"+self.default_img_name).resize((150, 150))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)
        self.searchData()

    def searchData(self):
        try:
            qry = "select * from student where name like %s"
            rowcount = self.curr.execute(qry,(self.t2.get()+"%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("",END,values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def checkValidation(self):
        if len(self.t1.get())<1 or not self.t1.get().isdigit():
            messagebox.showwarning("Validation Check","Enter Proper Roll no ",parent=self.window)
            return False
        elif len(self.t2.get())<1 :
            messagebox.showwarning("Validation Check","Enter Proper Name ",parent=self.window)
            return False
        elif len(self.t3.get())<7 or len(self.t3.get())>15 or not self.t3.get().isdigit():
            messagebox.showwarning("Validation Check","Enter Proper Phone no\n[7-15 digits] ",parent=self.window)
            return False
        elif not( self.v1.get()=="Male" or self.v1.get()=="Female"):
            messagebox.showwarning("Validation Check","Select Gender ",parent=self.window)
            return False
        elif self.t5.get()=="":
            messagebox.showwarning("Validation Check","Select DOB ",parent=self.window)
            return False
        elif len(self.t6.get('1.0',END))<2:
            messagebox.showwarning("Validation Check","Enter Address ",parent=self.window)
            return False
        elif self.v2.get()=="Choose Department" or self.v2.get()=="No Department":
            messagebox.showwarning("Validation Check","Select Department ",parent=self.window)
            return False
        elif self.v3.get()=="Choose Course" or self.v2.get()=="No Course":
            messagebox.showwarning("Validation Check","Select Course ",parent=self.window)
            return False
        return True

    def getAllDepartment(self):
        try:
            qry = "select * from department"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.deptList=[]
            if data:
                self.c1.set("Choose Department")
                for row in data:
                    self.deptList.append(row[0])
            else:
                self.c1.set("No Department")
            self.c1.config(values=self.deptList)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)


    def getAllCourse(self):
        try:
            qry = "select * from course where deptname=%s"
            rowcount = self.curr.execute(qry,(self.v2.get()))
            data = self.curr.fetchall()
            self.courseList=[]
            if data:
                self.c2.set("Choose Course")
                for row in data:
                    self.courseList.append(row[1])
            else:
                self.c2.set("No Department")
            self.c2.config(values=self.courseList)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyHomepage=Tk()
    StudentPageClass(dummyHomepage)
    dummyHomepage.mainloop()
