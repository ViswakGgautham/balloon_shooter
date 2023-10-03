# tkinter login
import tkinter as tkin
import customtkinter as tk
from tkinter.constants import *
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os
import csv
from balloon import *
import mysql.connector as sql
import pygame as py


class end():
    user = ''
    end = True


class window():
    def __init__(self):
        with open("highscore.csv", "a+") as w:
            print("Created Highscore")
        self.main = tkin.Tk()
        self.l = False
        self.image = Image.open('tkproj.png')
        self.copy_of_image = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.CTkLabel(self.main, image = self.photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=BOTH, expand = YES)
        self.main.title('LOGIN')
        self.main.geometry('900x650')
        tk.CTkLabel(self.main, text='Username',
                    text_color='black').place(x=180, y=40)
        tk.CTkLabel(self.main, text='Password',
                    text_color='black').place(x=180, y=80)
        tk.CTkLabel(self.main, text='Dont have an account? Sign in Now',
                    text_color='black', width=300).place(x=300, y=470)
        self.user = tk.CTkEntry(self.main)
        self.user.place(x=280, y=40)
        self.pswd = tk.CTkEntry(self.main, show='*')
        self.pswd.place(x=280, y=80)
        tk.CTkButton(master=self.main, text='Login', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.login).place(x=280, y=110)
        tk.CTkButton(master=self.main, text='Sign Up', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.signup).place(x=375, y=500)
        tk.CTkButton(master=self.main, text='Update', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.update).place(x=280, y=140)
        tk.CTkButton(master=self.main, text='Admin', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.chkadmin).place(x=375, y=200)
        tk.CTkButton(master=self.main, text='Instructions', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.sample).place(x=500, y=400)
        self.tgbutton = tk.CTkButton(master=self.main, text='Show Password', text_color='black',
                                     width=200, fg_color='grey', bg='white', command=self.togglepas)
        tk.CTkButton(master=self.main, text='VIEW', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.view).place(x=375, y=400)
        self.tgbutton.place(x=500, y=80)
        tk.CTkButton(master=self.main, text='highscore', width=100, text_color='black',
                     fg_color='grey', bg='white', command=self.open1).place(x=375, y=400)
        self.main.mainloop()

    def open1(self):
        os.system('highscore.csv')

    def view(self):
        f = os.system(r'view.csv')
        f = open('view.csv', 'a+', newline='')
        r = csv.reader(f)
        w = csv.writer(f)
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute('select username from login;')
        user = cursor.fetchall()
        w.writerow(user)
        db.commit()
        db.close()

    def sample(self):
        f = os.system(r'instructions.txt')

    def togglepas(self):
        if self.l:
            self.l = not self.l
            self.pswd.configure(show='')
            self.tgbutton.configure(text='Hide Password')
        else:
            self.l = not self.l
            self.pswd.configure(show='*')
            self.tgbutton.configure(text='Show Password')

    def insert(self, user, pswd, email):
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute(
            'insert into login values("%s","%s","%s");' % (email, user, pswd))
        readstat(name=user, mode='w')
        db.commit()
        db.close()

    def recupdate(self, user, pswd, email):
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute(
            'update login set username="%s" where email_id="%s";' % (user, email))
        cursor.execute(
            'update high set username="%s" where email_id="%s";' % (user, email))
        cursor.execute(
            'update login set password="%s" where email_id="%s";' % (pswd, email))
        db.commit()
        db.close()

    def admin(self):
        global trv
        self.adm = Toplevel()
        self.adm.geometry('800x500')
        self.adm.title('ADMIN')
        Label(self.adm, text=' ADMIN - changes can be done').place(x=100, y=20)

        # upd=tk.CTkButton(self.adm,text='Update',width='10',fg='blue',text_color='black',bg='white',command=self.uprec).place(x=200,y=150)
        tk.CTkLabel(self.adm, text=' User Deletion ',
                    text_color='black').place(x=70, y=250)
        tk.CTkLabel(self.adm, text=' User Search ',
                    text_color='black').place(x=70, y=350)
        dele = tk.CTkButton(self.adm, text='Delete', width=10, fg_color='blue',
                            bg_color='white', command=self.delrec).place(x=200, y=250)
        ser = tk.CTkButton(self.adm, text=' Search', width=10,
                           fg_color='blue', bg_color='white').place(x=200, y=350)
        add = tk.CTkButton(self.adm, text='Add', width=10, fg_color='blue',
                           bg_color='white', text_color='black', command=self.addrec).place(x=200, y=85)
        tk.CTkLabel(self.adm, text=' Username').place(x=300, y=85)
        tk.CTkLabel(self.adm, text=' Email').place(x=400, y=85)
        tk.CTkLabel(self.adm, text=' Password').place(x=450, y=85)
        self.nuser = tkin.Entry(self.adm)
        self.nuser.place(x=300, y=100)
        self.nemail = tkin.Entry(self.adm)
        self.nemail.place(x=400, y=100)
        self.npswd = tkin.Entry(self.adm)
        self.npswd.place(x=450, y=100)

    # tree function

        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute('SELECT*FROM LOGIN;')
        al = cursor.fetchall()
        trv = ttk.Treeview(self.adm, selectmode='browse')

        trv.place(x=300, y=200)
        verbar = ttk.Scrollbar(self.adm, orient="vertical", command=trv.yview)
        # verbar.pack(side ='right', fill ='x')
        verbar.place(x=570, y=200)

        trv.configure(xscrollcommand=verbar.set)

        trv["columns"] = ("1", "2", "3")

        trv['show'] = 'headings'

        trv.column("1", width=80, anchor='c')
        trv.column("2", width=105, anchor='c')
        trv.column("3", width=80, anchor='c')

        trv.heading("1", text="username")
        trv.heading("2", text="Email")
        trv.heading("3", text="Password")
        for i in al:
            trv.insert("", 'end', iid=i[0],
                       text=i[0], values=(i[1], i[0], i[2]))

    def delrec(self):
        sel = trv.selection()
        for i in sel:
            trv.delete(sel)
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute(f"delete from login where username='{sel[0]}'")

        db.commit()
        db.close()

    def chkadmin(self):
        if self.user.get() == 'admin' and self.pswd.get() == '12345':
            self.admin()
        else:
            Label(self.main, text=' not admin ').place(x=200, y=250)

    def addrec(self):
       trv.insert("", 'end', iid=0, text='', values=(
           self.nuser.get(), self.nemail.get(), self.npswd.get()))

       db = sql.connect(host='localhost', user='root',
                        database='project', password='password')
       cursor = db.cursor()
       cursor.execute('insert into login values("%s","%s","%s");' %
                      (self.nuser.get(), self.nemail.get(), self.npswd.get()))
       db.commit()
       db.close()

    def uprec(self):
        '''sel=trv.selection()
        db=sql.connect(host='localhost',user='root',database='project',password='password')
        cursor=db.cursor()
        cursor.execute('update login set ("%s","%s","%s");'%(self.nuser.get(),self.nemail.get(),self.npswd.get()))
        db.commit()
        db.close()'''

        self.uprec = Toplevel()
        self.uprec.geometry('800x500')
        self.uprec.title('ADMIN')
        Label(self.uprec, text='UPDATE RECORD').place(x=100, y=20)
        Label(self.uprec, text='user').place(x=100, y=200)
        Label(self.uprec, text='email').place(x=100, y=300)
        Label(self.uprec, text='pswd').place(x=100, y=400)
        self.user1 = tkin.Entry(self.uprec)
        self.user1.place(x=100, y=300)
        self.email1 = tkin.Entry(self.uprec)
        self.pswd1 = tkin.Entry(self.uprec)
        self.email1.place(x=100, y=400)
        self.pswd1.place(x=100, y=500)

    def login(self):
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        cursor.execute('SELECT*FROM LOGIN;')
        u = self.user.get()
        p = self.pswd.get()
        w = cursor.fetchall()

        def check():
            for i in w:
                if i[1] == u and i[2] == p:
                    end.end = True
                    end.user = i[1]
                    self.main.destroy()
                    game(u)

        tk.CTkButton(master=self.main, text='Login', width=100,
                     fg_color='grey', bg='white', command=check).place(x=280, y=110)
        db.close()

    def update(self):
        db = sql.connect(host='localhost', user='root',
                         database='project', password='password')
        cursor = db.cursor()
        user1 = self.user.get()
        pswd1 = self.pswd.get()
        cursor.execute('SELECT*FROM LOGIN;')
        w = cursor.fetchall()
        db.close()
        new1 = Toplevel()
        new1.geometry('1000x800')
        new1.title('Update')
        tk.CTkLabel(new1, text='UPDATE YOUR CREDENTIALS').place(x=100, y=10)
        tk.CTkLabel(new1, text='Username').place(x=180, y=40)
        tk.CTkLabel(new1, text='Email').place(x=180, y=70)
        tk.CTkLabel(new1, text='Password').place(x=180, y=100)
        tk.CTkLabel(new1, text='confirm Password').place(x=180, y=130)
        g1 = tk.CTkEntry(new1)
        g2 = tk.CTkEntry(new1)
        g3 = tk.CTkEntry(new1)
        g4 = tk.CTkEntry(new1)
        g1.place(x=500, y=40)
        g2.place(x=500, y=70)
        g3.place(x=500, y=100)

        g4.place(x=500, y=130)

        print(g3)
        # def check1():

        def rec():
            if g3.get() == g4.get():
                print('y')
                self.recupdate(g1.get(), g3.get(), g2.get())
                new1.destroy()
            elif g3.get() != g4.get():
                tk.CTkLabel(self.new, text='Your password doesnt match').place(
                    x=200, y=250)
            elif g3.get() == '' or g4.get == '':
                tk.CTkLabel(self.new, text='No password').place(x=200, y=250)
        tk.CTkButton(new1, text='Update', width=10, fg_color='blue',
                     bg='white', command=rec).place(x=250, y=160)

    def signup(self):
        new = Toplevel()
        new.geometry('1000x800')
        new.title('Sign Up')
        tk.CTkLabel(new, text='SIGN IN NOW WITH YOUR CREDENTIALS',
                    text_color='black').place(x=100, y=10)
        tk.CTkLabel(new, text='Username',
                    text_color='black').place(x=180, y=40)
        tk.CTkLabel(new, text='Email', text_color='black').place(x=180, y=70)
        tk.CTkLabel(new, text='Password',
                    text_color='black').place(x=180, y=100)
        tk.CTkLabel(new, text='Confirm Password',
                    text_color='black').place(x=150, y=130)
        e1 = tk.CTkEntry(new)
        e2 = tk.CTkEntry(new)
        e3 = tk.CTkEntry(new)
        e4 = tk.CTkEntry(new)
        e1.place(x=300, y=40)
        e2.place(x=300, y=70)
        e3.place(x=300, y=100)
        e4.place(x=300, y=130)

        def validate():
            global l
            pswd = e3.get()
            conf = e4.get()
            user = e1.get()
            email = e2.get()
            if pswd != conf:
                tk.CTkLabel(new, text='Your password doesnt match').place(
                    x=200, y=250)
            elif pswd == '' or conf == '':
                tk.CTkLabel(new, text='SOMETHING IS MISSING').place(
                    x=200, y=300)
            elif len(e1.get()) > 15:
                tk.CTkLabel(new, text='Exceeded Limit').place(x=200, y=400)
            else:
                self.insert(user, pswd, email)
                new.destroy()

        tk.CTkButton(master=new, text='Sign Up', width=100, fg_color='grey',
                     bg='white', command=validate).place(x=375, y=200)

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo


a = window()

