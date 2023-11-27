from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_pass():
        if userEntry.get()=='' or newpassEntry.get()=='' or confirmpassEntry.get()=='':
            messagebox.showerror('Error','All Fields are Required',parent=window)
        elif newpassEntry.get()!=confirmpassEntry.get():
            messagebox.showerror('Error','Passwords do not match',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='root123',database='userdata')
            mycursor=con.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query,(userEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpassEntry.get(),userEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password updated successfully. Login with new password',parent=window)
                window.destroy()

    window=Toplevel()
    window.title('Change Password')
    bgpic=ImageTk.PhotoImage(file="Login-Register\images\\background.jpg")

    bgLabel=Label(window,image=bgpic)
    bgLabel.grid()

    heading_label=Label(window,text="Reset Password",font=('arial',20,'bold'),bg='white',fg='magenta2')
    heading_label.place(x=495,y=60)

    user_label=Label(window,text="Username",font=('arial',14,'bold'),bg='white',fg='orchid2')
    user_label.place(x=470,y=130)

    userEntry=Entry(window,width=25,font=('arial',13,'bold'),bd=0,fg='magenta2')
    userEntry.place(x=470,y=160)

    Frame(window,width=260,height=2,bg='orchid2').place(x=470,y=180)

    new_pass=Label(window,text="New Password",font=('arial',14,'bold'),bg='white',fg='orchid2')
    new_pass.place(x=470,y=220)

    newpassEntry=Entry(window,width=25,font=('arial',13,'bold'),bd=0,fg='magenta2')
    newpassEntry.place(x=470,y=250)

    Frame(window,width=260,height=2,bg='orchid2').place(x=470,y=270)

    confirm_pass=Label(window,text="Confirm Password",font=('arial',14,'bold'),bg='white',fg='orchid2')
    confirm_pass.place(x=470,y=310)

    confirmpassEntry=Entry(window,width=25,font=('arial',13,'bold'),bd=0,fg='magenta2')
    confirmpassEntry.place(x=470,y=340)

    Frame(window,width=260,height=2,bg='orchid2').place(x=470,y=360)

    submitButton=Button(window,text='Submit',width=19,font=('Open Sans',16,'bold'),bg='magenta2',fg='white',bd=0,activebackground='magenta2',activeforeground='white',cursor='hand2',command=change_pass)
    submitButton.place(x=470,y=410)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection not established')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Success','Login Successful')


def user_enter(event):  
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='Login-Register\images\closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='Login-Register\images\openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def register_page():
    login_window.destroy()
    import Register

login_window = Tk()

login_window.title("Login")
login_window.geometry("990x660+50+50")
login_window.resizable(0,0)
login_window.configure(bg="indian red")
bgImage=ImageTk.PhotoImage(file="Login-Register\images\\bg.jpg")

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text="User Login",font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=620,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)

frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file="Login-Register\images\openeye.png")
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgot_pass_Button=Button(login_window,text='Forgot Password?',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',command=forget_pass)
forgot_pass_Button.place(x=715,y=295)

loginButton=Button(login_window,text='LOGIN',bd=0,width='19',bg='firebrick1',font=('Open Sans',16,'bold'),fg='white',activeforeground='white',activebackground='firebrick1',cursor='hand2',command=login_user)
loginButton.place(x=578,y=350)

registerLabel=Label(login_window,text="Don't have an account?",font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
registerLabel.place(x=590,y=500)

registerButton=Button(login_window,text='Create new one',bd=0,bg='white',font=('Open Sans',9,'bold underline'),fg='blue',activeforeground='blue',activebackground='white',cursor='hand2',command=register_page)
registerButton.place(x=727,y=500)

login_window.mainloop()