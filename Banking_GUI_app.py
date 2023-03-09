
# Allow the User to register an account
# Allow the user to login
# Allow the User to view balance and personal details

from tkinter import *
import os 
from PIL import ImageTk, Image
from tkinter import messagebox

# Main screen

master = Tk()
master.title('Banking App') 
master.geometry('400x600')
master.minsize(400,600) 
master.configure(background='#0096DC')

# Functions

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
 
    if name == "" or age == "" or gender == "" or password == "":
        # notif.config(fg="red", text= "All fields required * ")
        messagebox.showwarning(title = 'Warning',message="All fields required") 
        return

    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            # messagebox.showwarning(title='Warning', message='Account already exists')
            return
        else:
            new_file = open(name, "w")
            new_file.write(name+ '\n' + password + '\n' + age + '\n' + gender + '\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account is now successfully registered")

def register():
    #Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password 
    global notif 

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    # Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.configure(background='#0096DC')

    # Register Screen Labels

    Label(register_screen, text="Please enter your details below to register", font=('calibri', 16), bg='#0096DC').grid(row=0, sticky=N, pady=10)

    Label(register_screen, text="Name", font=('calibri', 14), bg = '#0096DC').grid(row=1, sticky=W)

    Label(register_screen, text="Age", font=('calibri', 14), bg='#0096DC').grid(row=2, sticky=W)

    Label(register_screen, text="Gender", font=('calibri', 14), bg='#0096DC').grid(row=3, sticky=W)

    Label(register_screen, text="Password", font=('calibri', 14), bg='#0096DC').grid(row=4, sticky=W)

    notif = Label(register_screen, font=('calibri', 12), bg='#0096DC')
    notif.grid(row=6, sticky=N, pady=10)

    # Register Screen Entries

    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)

    # Register Screen Buttons

    Button(register_screen, text='Register', command= finish_reg, font=('calibri', 14)).grid(row=5, sticky=N, pady=20)


def login_session():
    global login_name
    
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name, "r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            # Account dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                account_dashboard.minsize(400,600) 
                account_dashboard.configure(background='#0096DC')
                # Labels
                Label(account_dashboard, text= 'Account Dashboard', font=('calibri', 16), bg='#0096DC').grid(row=0,sticky=N, pady=10) 
                Label(account_dashboard, text = 'Welcome ' + name, font=('calibri', 14), bg ='#0096DC').grid(row=1, sticky=N, pady=5)

                #Buttons
                Button(account_dashboard, text="Personal details", font=('calibri', 14), width=30, command = personal_details).grid(row=2, sticky=N, pady=(10, 10))

                Button(account_dashboard, text="Deposit", font=('calibri', 14), width=30, command= deposit).grid(row=3, sticky=N, pady=(10,10))

                Button(account_dashboard, text="Withdraw", font=('calibri', 14), width=30, command = withdraw).grid(row=4, sticky=N, pady=(10,10)) 

                # Label(account_dashboard).grid(row=5, sticky=N,pady=10)

                return
            else:
                login_notif.config(fg='red', text='incorrect password')
                return
        
    login_notif.config(fg='red', text= 'No account found !!')


def deposit():

    # Variables
    global amount
    global deposit_notif 
    global current_balance_label

    amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]  

    # deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    deposit_screen.configure(background="white")
    deposit_screen.minsize(400,600)

    # Labels deposit

    Label(deposit_screen, text="Deposit", font=('calibri', 16), bg="white").grid(row=0,sticky=N, pady=10)

    current_balance_label = Label(deposit_screen, text="Current Balance : Rs." + details_balance, font=('calibri', 14), bg="white")
    current_balance_label.grid(row=1, sticky=N, pady=10) 

    Label(deposit_screen, text='Amount : ', font=('calibri', 14), bg="white").grid(row=2, sticky=N, pady=10)

    deposit_notif = Label(deposit_screen, font=('calibri', 14), bg="white")
    deposit_notif.grid(row=4, sticky=N, pady=10) 

    # Entry deposit
    Entry(deposit_screen, textvariable = amount).grid(row=2, column=1)

    # Button deposit
    Button(deposit_screen, text='Finish', font=('calibri', 14), command = finish_deposit).grid(row=3, sticky=N, pady=10)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text= 'Amount is required!', fg='red')
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text='Negative currency is not accepted', fg='red')
        return
    
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())

    file_data = file_data.replace(current_balance, str(updated_balance)) 
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance : Rs." + str(updated_balance), fg="green")

    deposit_notif.config(text='Balance updated', fg="green") 

def withdraw():
    # Withdraw screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("withdraw")
    withdraw_screen.configure(background="#0096DC")
    withdraw_screen.minsize(400,600)

    # Variables
    global withdraw_amount
    global withdraw_notif 
    global current_balance_label

    withdraw_amount = StringVar()
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]  

    # Labels deposit

    Label(withdraw_screen, text="Withdraw", font=('calibri', 16), bg="white").grid(row=0,sticky=N, pady=10)

    current_balance_label = Label(withdraw_screen, text="Current Balance : Rs." + details_balance, font=('calibri', 14), bg="white")
    current_balance_label.grid(row=1, sticky=N, pady=10) 

    Label(withdraw_screen, text='Amount : ', font=('calibri', 14), bg="white").grid(row=2, sticky=N, pady=10)

    withdraw_notif = Label(withdraw_screen, font=('calibri', 14), bg="white")
    withdraw_notif.grid(row=4, sticky=N, pady=10) 

    # Entry deposit
    Entry(withdraw_screen, textvariable = withdraw_amount).grid(row=2, column=1)

    # Button deposit
    Button(withdraw_screen, text='Finish', font=('calibri', 14), command = finish_withdraw).grid(row=3, sticky=N, pady=10) 


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="Amount is required", fg="red")
        return
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text = "Negative currency is not accepted", fg= "red")
        return
    
    file = open(login_name, "r+")
    file_data = file.read()
    details = file_data.split("\n")
    current_balance = details[4]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text="Insufficient funds", fg="red")
        return
    
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get()) 

    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance: Rs. " + str(updated_balance), fg="green")
    withdraw_notif.config(text="Balance updated", fg = "green") 


def personal_details():
    #variables
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4] 

    # personal_details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.configure(background="#0096DC")
    personal_details_screen.minsize(400,600)

    # Labels personal details screen
    Label(personal_details_screen, text="Personal Details", font=('calibri', 16)).grid(row=0, sticky=N, pady=10)

    Label(personal_details_screen, text="Name : " + details_name, font=('calibri', 14)).grid(row=1, sticky=N, pady=10)

    Label(personal_details_screen, text ="Age : " + details_age, font =('calibri', 14)).grid(row=2, sticky=N, pady=10)

    Label(personal_details_screen, text='Gender : ' + details_gender, font=('calibri', 14)).grid(row=3,sticky=N, pady=10)

    Label(personal_details_screen, text='Account balance : Rs.' + details_balance, font = ('calibri', 14)).grid(row=4, sticky=N, pady=10) 


def login():
    # Variables

    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Login Screen

    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen.configure(background='#0096DC')
    login_screen.minsize(400,600) 

    # Login screen Labels

    Label(login_screen, text = "Login to your Account", font = ("calibri", 16), bg='#0096DC').grid(row=0, sticky=N, pady=(20,5))

    Label(login_screen, text = "Username", font = ("calibri", 14), bg='#0096DC').grid(row=1, sticky=N, padx=5)

    Label(login_screen, text = "Password", font = ("calibri", 14), bg='#0096DC').grid(row=2, sticky=N, padx=5)  

    login_notif = Label(login_screen, font=("calibri", 12), bg="#0096DC")
    login_notif.grid(row=4, sticky=N)

    # Login Screen Entries

    Entry(login_screen, textvariable = temp_login_name).grid(row=1, column=1)
    Entry(login_screen, textvariable = temp_login_password, show="*").grid(row=2, column=1)

    # Login Screen Buttons

    Button(login_screen, text="login", command= login_session, width = 15, font=('calibri', 14)).grid(row=5, sticky=N, pady=5, padx=50) 

# Image import

img = Image.open('banking_img.png')
img = img.resize((300, 300))
img = ImageTk.PhotoImage(img) 


# Labels

Label(master, text = "Custom Banking Beta", font=('Calibri', 18), bg = '#0096DC').grid(row = 0, sticky=N, pady = (20,5))

Label(master, text = "The most secure and trusted Online Banking App", font=('Calibri', 14), bg='#0096DC').grid(row = 1, sticky=N, pady=5, padx=10)

Label(master, image=img).grid(row=2, sticky=N, pady = 15)


# Buttons

Button(master, text = "Register", font=('calibri', 14), width=20, command=register).grid(row=3, sticky=N)

Button(master, text = "Login", font=('calibri', 14), width=20, command = login).grid(row=4, sticky=N, pady=10) 

master.mainloop()