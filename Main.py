# -*- coding: utf-8 -*-


from tkinter import ttk, StringVar, messagebox
from ttkthemes import ThemedTk, ThemedStyle
import sqlite3

class restaurant_management_login_signup:
    STYLE = 'aqua'
    user_info = None
    id=''

    def __init__(self):
        # create user table
        conn = sqlite3.connect('user.db')
        query = "CREATE TABLE IF NOT EXISTS user_accounts (uid integer primary key autoincrement, name string, password string)"
        conn.execute(query)
        conn.commit()
        conn.close()

        self.show_login_window()
    
#Login Window Starts
    def show_login_window(self):
        root = ThemedTk(theme=self.STYLE)
        root.geometry("400x250")
        root.title('Login')
        root.resizable(0,0)

        # title
        ttk.Label(root, font=('default', 19, 'bold'), text='*******DTU CAFE******').grid(row=0, column=0, sticky='w', padx=15)
        ttk.Separator(root, orient='horizontal').grid(row=1, columnspan=2, sticky='ew')

        # sub title
        ttk.Label(root, font=('default', 14, 'bold'), text='Admin Login').grid(row=2, column=0, sticky='w', padx=5, pady=10)
        #Jumps to Sign-Up Window
        def show_signup():
            root.destroy()
            self.show_signup_window()
        #Tries to login by checking credentials
        def login_db():
            try:
                conn = sqlite3.connect('user.db')
                p=var_user.get()
                query =conn.execute("SELECT password FROM user_accounts WHERE name='"+p+"'")
                for row in query:
                       id = row[0]
                if id==int(var_pass.get()):
                    m=messagebox.askyesno('Success!', 'User logged in! Continue to make your orders')
                    if m>0:
                        root.destroy()
                        import restaurantmangement

                else:
                    messagebox.showerror('Error!', 'Username or password does not match!')
            except:
                messagebox.showerror('Error!', 'Username or password does not match!')
                
    #GUI for Login
        PADX,PADY=5,5
        # login form
        ttk.Label(root, text='Username:').grid(row=3, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Password:').grid(row=4, column=0, sticky='w', padx=PADX, pady=PADY)

        var_user, var_pass = StringVar(), StringVar()
        ttk.Entry(root, textvariable=var_user, width=25).grid(row=3, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_pass, width=25).grid(row=4, column=0, sticky='e', padx=PADX, pady=PADY)

        #ttk.Button(root, text='Signup', command=show_signup).grid(row=5, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Button(root, text='Login', command=login_db).grid(row=5, column=0, sticky='e', padx=PADX, pady=PADY)
        root.mainloop()
    #SignUp Window Starts
    def show_signup_window(self):
        root = ThemedTk(theme=self.STYLE)
        root.geometry("400x250")
        root.title('Signup')
        root.resizable(0,0)

        # title
        ttk.Label(root, font=('default', 19, 'bold'), text='******DTU CAFE******').grid(row=0, column=0, sticky='w', padx=15)
        ttk.Separator(root, orient='horizontal').grid(row=1, columnspan=2, sticky='ew')

        # sub title
        ttk.Label(root, font=('default', 14, 'bold'), text='Add a new employee').grid(row=2, column=0, sticky='w', padx=5, pady=10)
        
        # defs
        def show_login():
            root.destroy()
            self.show_login_window()
        #Registers New User with database
        def signup_db():
            conn = sqlite3.connect('user.db')
            if not var_pass.get()==var_repass.get():
                messagebox.showwarning('Warning!', 'Passwords do not match.')
                return
            try:
                query = "INSERT INTO user_accounts(name, password) VALUES ( '{var_user.get()}', '{var_pass.get()}' )"
                
                conn.execute(query)
                conn.commit()
                messagebox.showinfo('Success!', 'User account for %s successfuly created!'%var_user.get())
                show_login()
            except:
                messagebox.showerror('Error!', 'There was an unexpected error!')

        PADX, PADY = 5, 5
        # signup form
        ttk.Label(root, text='Username:').grid(row=3, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Password:').grid(row=4, column=0, sticky='w', padx=PADX, pady=PADY)
        ttk.Label(root, text='Re-Password:').grid(row=5, column=0, sticky='w', padx=PADX, pady=PADY)
        

        var_user, var_pass, var_repass = StringVar(), StringVar(), StringVar()
        ttk.Entry(root, textvariable=var_user, width=25).grid(row=3, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_pass, width=25).grid(row=4, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Entry(root, textvariable=var_repass, width=25).grid(row=5, column=0, sticky='e', padx=PADX, pady=PADY)
        

        #ttk.Button(root, text='Signup', command=signup_db).grid(row=8, column=0, sticky='e', padx=PADX, pady=PADY)
        ttk.Button(root, text='Login', command=show_login).grid(row=8, column=0, sticky='w', padx=PADX, pady=PADY)

        root.mainloop()
restaurant_management_login_signup()

