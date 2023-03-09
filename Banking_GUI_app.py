# banking system using OOP

# Parent class : User
    # Holds details about an User
    # Has a function to show user details

# child class : Bank
    # stores details about the account balance
    # stores details about the amount
    # allows for deposits, withdraw, view_balance

# Parent Class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details\n")
        print("Name: ", self.name) 
        print("Age: ", self.age)
        print("Gender: ", self.gender, "\n") 

user1 = User("Siddhi", 30, "Female")
user1.show_details()

# child class:

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated : ", self.balance)

    def withdraw(self, amount):
        if (amount > self.balance):
            print("Insufficient funds, Balance available:  ", self.balance)
        else:
            self.balance = self.balance - amount
            print("Available balance:", self.balance) 

    def view_balance(self):
        self.show_details()
        print("Available balance:", self.balance, "\n")  


user2 = Bank("Perpetual", 25, "Female") 
user2.show_details()
user2.deposit(200)
user2.deposit(500)
user2.deposit(1000)
user2.withdraw(200)
user1 = Bank("lulian", 30, "Male")
user1.withdraw(500) 
user2.withdraw(2000) 

user1.view_balance()
user2.view_balance()
