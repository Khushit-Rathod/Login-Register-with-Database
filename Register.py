from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END) 
    confirm_passEntry.delete(0,END)


def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirm_passEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif emailEntry.get().__contains__('@')==FALSE:
        messagebox.showerror('Error','Invalid Email Id')
    elif passwordEntry.get()!=confirm_passEntry.get():
        messagebox.showerror('Error','Passwords do not match')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue')
            return
        
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error','Username already exists')
            clear()
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))

            con.commit()
            con.close()
            messagebox.showinfo('Success','Registered Successfully')
            clear()
            register_window.destroy()
            import Login

def login_page():
    register_window.destroy()
    import Login

register_window = Tk()

register_window.title("Register")
register_window.resizable(0,0)
register_window.geometry("990x660+50+50")
bgImage=ImageTk.PhotoImage(file="Login-Register\images\\bg.jpg")

bgLabel=Label(register_window,image=bgImage)
bgLabel.place(x=0,y=0)

frame=Frame(register_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text="Create an Account",font=('Microsoft Yahei UI Light',22,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

email=Label(frame,text="Email",font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='firebrick1')
email.grid(row=1,column=0,padx=20,sticky='w')

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='IndianRed1',fg='white')
emailEntry.grid(row=2,column=0,padx=20,sticky='w')

username=Label(frame,text="Username",font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='firebrick1')
username.grid(row=3,column=0,padx=20,sticky='w',pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='IndianRed1',fg='white')
usernameEntry.grid(row=4,column=0,padx=20,sticky='w')

password=Label(frame,text="Password",font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='firebrick1')
password.grid(row=5,column=0,padx=20,sticky='w',pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='IndianRed1',fg='white')
passwordEntry.grid(row=6,column=0,padx=20,sticky='w')

confirm_pass=Label(frame,text="Confirm Password",font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='firebrick1')
confirm_pass.grid(row=7,column=0,padx=20,sticky='w',pady=(10,0))

confirm_passEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='IndianRed1',fg='white')
confirm_passEntry.grid(row=8,column=0,padx=20,sticky='w')

registerButton=Button(frame,text="REGISTER",width=13,font=('Open Sans',18,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',cursor='hand2',command=connect_database)
registerButton.grid(row=9,column=0,pady=25)

loginLabel=Label(frame,text="Already have an account?",font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
loginLabel.grid(row=10,column=0,padx=(40,0),pady=10,sticky='w')

loginButton=Button(frame,text='Login',bd=0,bg='white',font=('Open Sans',9,'bold underline'),fg='blue',activeforeground='blue',activebackground='white',cursor='hand2',command=login_page)
loginButton.place(x=205,y=409)


register_window.mainloop()