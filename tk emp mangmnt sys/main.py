from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")
ems=Tk()
ems.title("Employee Management System")
ems.geometry("800x580+0+0")
ems.config(bg="red")
ems.state("zoomed")

name=StringVar()
age=StringVar()
dob=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

entries_frame=Frame(ems,bg="black")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="EMPLOYMENT    MANAGEMENT   SYSTEM",font=("calibri",22,"bold"),bg="gray",bd=2,relief="groove",fg="black")
title.grid(row=0, columnspan=2,padx=10,pady=20)

lblName=Label(entries_frame,text="NAME",font=("calibri",16,"bold"),bg="black",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entries_frame,text="AGE",font=("calibri",16,"bold"),bg="black",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lbldob=Label(entries_frame,text="DOB",font=("calibri",16,"bold"),bg="black",fg="white")
lbldob.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdob=Entry(entries_frame,textvariable=dob,font=("calibri",16),width=30)
txtdob.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblemail=Label(entries_frame,text="EMAIL",font=("calibri",16,"bold"),bg="black",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtemail=Entry(entries_frame,textvariable=email,font=("calibri",16),width=30)
txtemail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblgender=Label(entries_frame,text="GENDER",font=("calibri",16,"bold"),bg="black",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable=gender,state="readonly")
comboGender['values']=("Male","Female")
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lblcontact=Label(entries_frame,text="CONTACT NO",font=("calibri",16,"bold"),bg="black",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

lbladdress=Label(entries_frame,text="ADDRESS",font=("calibri",16,"bold"),bg="black",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtaddress=Text(entries_frame,width=85,height=5,font=("calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_items():
    if txtName.get()=="" or txtAge.get()=="" or txtdob.get()=="" or txtemail.get()=="" or comboGender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please fill all the details")
        return
    db.insert(txtName.get(),txtAge.get(),txtdob.get(),txtemail.get(),comboGender.get(), txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()

def update_items():
    if txtName.get()=="" or txtAge.get()=="" or txtdob.get()=="" or txtemail.get()=="" or comboGender.get()=="" or txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please fill all the details")
        return
    db.update(row[0],txtName.get(),txtAge.get(),txtdob.get(),txtemail.get(),comboGender.get(), txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Success","Record Updated")
    clearAll()
    displayAll()

def delete_items():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age .set("")
    dob .set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="black")
btn_frame.grid(row=6,column=0,columnspan=4,padx=7,pady=7,sticky="w")
btnAdd=Button(btn_frame,command=add_items,text="Add Details",width=15,font=("calibri",14,"bold"),fg="black",
              bg="#2980b9",bd=0).grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_items,text="Update Details",width=15,font=("calibri",14,"bold"),fg="black",
              bg="#16a085",bd=0).grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_items,text="Delete Details",width=15,font=("calibri",14,"bold"),fg="black",
              bg="#f39c12",bd=0).grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",width=15,font=("calibri",14,"bold"),fg="black",
              bg="#c0392b",bd=0).grid(row=0,column=3,padx=10)

tree_frame=Frame(ems,bg="blue")
tree_frame.place(x=0, y=460, width=1450, height=450)
Style=ttk.Style()
Style.configure("myStyle.Treeview", font=('calibri',18),rowheight=50)
Style.configure("myStyle.Treeview", font=('calibri',18),rowheight=50)

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="myStyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=4)
tv.heading("2",text="NAME")
tv.column("2",width=20)
tv.heading("3",text="AGE")
tv.column("3",width=4)
tv.heading("4",text="DOB")
tv.column("4",width=12)
tv.heading("5",text="EMAIL")
tv.column("5",width=20)
tv.heading("6",text="GENDER")
tv.column("6",width=8)
tv.heading("7",text="CONTACT")
tv.column("7",width=12)
tv.heading("8",text="ADDRESS")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()
ems.mainloop()