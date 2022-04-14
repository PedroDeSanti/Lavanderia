from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    if (id=='' or name=='' or phone==''):
        
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')
        cursor = con.cursor()
        cursor.execute("insert into student values("+id+",'"+name+"',"+phone+")")
        cursor.execute("commit")

        MessageBox.showinfo("Insert Values", "inserted Successfully")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        cursor.close()

def delete():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    if (id==''):
        MessageBox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')
        cursor = con.cursor()
        cursor.execute("delete from student where id = "+id)
        cursor.execute("commit")

        MessageBox.showinfo("Delete Values", "Deleted Successfully")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        cursor.close()

def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    if (id=='' or name=='' or phone==''):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')
        cursor = con.cursor()
        cursor.execute("update student set name='"+name+"', phone="+phone+" where id=" +id)
        cursor.execute("commit")

        MessageBox.showinfo("Update Values", "updated Successfully")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        cursor.close()

def get():
    id = e_id.get()

    if (id==''):
        MessageBox.showinfo("Fetch Status", "ID is compulsory for fetch")
    else:
        con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')
        cursor = con.cursor()
        cursor.execute("select * from student where id="+id)
        rows = cursor.fetchall()
        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])

        cursor.close()


def show():
    con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()

    for row in rows:
        insertData = str(row[0])+"   "+row[1]+"   "+str(row[2])
        list.insert(list.size()+1, insertData)
    
    con.close()

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+MySQL")

id = Label(root, text='Enter ID', font=('bold',10))
id.place(x=20,y=30)

name = Label(root, text='Enter name', font=('bold',10))
name.place(x=20,y=60)

phone = Label(root, text='Enter phone', font=('bold',10))
phone.place(x=20,y=90)

e_id = Entry()
e_id.place(x=150, y=30)
e_name = Entry()
e_name.place(x=150, y=60)
e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text='insert', font=('italic',10), bg='white', command=insert)
insert.place(x=20,y=140)

delete = Button(root, text='delete', font=('italic',10), bg='white', command=delete)
delete.place(x=70,y=140)

update = Button(root, text='update', font=('italic',10), bg='white', command=update)
update.place(x=120,y=140)

get = Button(root, text='get', font=('italic',10), bg='white', command=get)
get.place(x=170,y=140)

list = Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()
