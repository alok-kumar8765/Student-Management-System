from cProfile import label
from tkinter import messagebox, ttk
from tkinter import *
import pymysql

class Student():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry('1350x700')

        title = Label(self.root,text='Student Management System',
        font=('arial',40,'bold'),bg="blue",fg="white")
        title.pack(side=TOP,fill=X)

        self.Roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        # self.address_var = StringVar()
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

        m_title = Label(Manage_Frame,text='Manage Students',
        font=("arial",20,'bold'),bg='crimson',fg='white')
        m_title.grid(row=0,columnspan=2,pady=20)

        roll_lbl = Label(Manage_Frame,text='Roll Number',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        roll_lbl.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txtroll = Entry(Manage_Frame,
        font=("arial",15,'bold'),bd=5,relief=GROOVE,textvariable=self.Roll_no_var)
        txtroll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        name_lbl = Label(Manage_Frame,text='Name',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        name_lbl.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txtname = Entry(Manage_Frame,
        font=("arial",15,'bold'),bd=5,relief=GROOVE,textvariable=self.name_var)
        txtname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        email_lbl = Label(Manage_Frame,text='Email',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        email_lbl.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txtemail = Entry(Manage_Frame,
        font=("arial",15,'bold'),bd=5,relief=GROOVE,textvariable=self.email_var)
        txtemail.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        gender_lbl = Label(Manage_Frame,text='Gender',font=("arial",15,'bold'),bg='crimson',fg='white')
        gender_lbl.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gen = ttk.Combobox(Manage_Frame,font=('arial',14,'bold'),state='readonly',textvariable=self.gender_var)
        combo_gen['values'] = ("male","female","other")
        combo_gen.grid(row=4,column=1,padx=20,pady=10)

        contact_lbl = Label(Manage_Frame,text='Contact',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        contact_lbl.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txtcontact = Entry(Manage_Frame,
        font=("arial",15,'bold'),bd=5,relief=GROOVE,textvariable=self.contact_var)
        txtcontact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        dob_lbl = Label(Manage_Frame,text='D.O.B',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        dob_lbl.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txtdob = Entry(Manage_Frame,
        font=("arial",15,'bold'),bd=5,relief=GROOVE,textvariable=self.dob_var)
        txtdob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        address_lbl = Label(Manage_Frame,text='Address',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        address_lbl.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txtadd = Text(Manage_Frame,
        font=("arial",15,'bold'),width=20,height=3,)
        self.txtadd.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        Button_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        Button_Frame.place(x=15,y=500,width=430)

        addbtn = Button(Button_Frame,text='Add',width=10,command=self.add_students)
        addbtn.grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(Button_Frame,text='Update',width=10,command=self.update_data)
        updatebtn.grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(Button_Frame,text='Delete',width=10,command=self.delete_data)
        deletebtn.grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(Button_Frame,text='Clear',width=10,command=self.clear)
        clearbtn.grid(row=0,column=3,padx=10,pady=10)

        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=590)

        search_lbl = Label(Detail_Frame,text='Search By',
        font=("arial",15,'bold'),bg='crimson',fg='white')
        search_lbl.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by_var,font=('arial',13,'bold'),state='readonly')
        combo_search['values'] = ("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txtsearch = Entry(Detail_Frame,textvariable=self.search_txt_var,
        font=("arial",14,'bold'),bd=4,relief=GROOVE,width=15)
        txtsearch.grid(row=0,column=2,pady=10,padx=15,sticky="w")

        searchbtn = Button(Detail_Frame,text='Search',width=10,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=10,pady=10)
        showbtn = Button(Detail_Frame,text='Show All',width=10,command=self.fetch_data)
        showbtn.grid(row=0,column=4,padx=10,pady=10)

        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scrool_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scrool_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=('roll',
        'name','email','gender','contact','D.O.B','Address'),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_y.config(command=self.Student_table.xview)
        scrool_y.config(command=self.Student_table.yview)
        self.Student_table.heading('roll',text='Roll No.')
        self.Student_table.heading('name',text='Name')
        self.Student_table.heading('email',text='Email')
        self.Student_table.heading('gender',text='Gender')
        self.Student_table.heading('contact',text='Contact')
        self.Student_table.heading('D.O.B',text='D.O.B')
        self.Student_table.heading('Address',text='Address')
        self.Student_table['show']='headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('gender',width=50)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('D.O.B',width=100)
        self.Student_table.column('Address',width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    from tkinter import messagebox
    def add_students(self):
        if self.Roll_no_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
            self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txtadd.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo('Successfull','Record Inserted Successfully')
    
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("select * form students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row) 
            con.commit()
        con.close()       

    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.txtadd.delete('1.0',END)
    
    def get_cursor(self):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        # con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        # cur = con.cursor()
        # cur.execute("select * form students where roll_no=%s",)
        # rows = cur.fetchall()
        # if len(rows)!=0:
        #     self.Student_table.delete(*self.Student_table.get_children())
        #     for row in rows:
        #         self.Student_table.insert('',END,values=row) 
        #     con.commit()
        # con.close()   
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txtadd.delete('1.0',END)
        self.txtadd.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
        self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txtadd.get('1.0',END),self.Roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
          
    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("delete form students where roll_no=%s",self.Student_table.get())
        con.commit()
        con.close()

    def search_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur = con.cursor()
        cur.execute("select * form students where"+str(self.search_by_var.get())+"LIKE %"+str(self.search_txt_var.get())+"%")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row) 
            con.commit()
        con.close()       
    

root = Tk()
ob=Student(root)
root.mainloop()