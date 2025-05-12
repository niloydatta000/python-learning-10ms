#Object-Oriented Programming: Introduction of Constructor

#Let's make a Program about how to log in.

class User:
    isLoggedIn = False # Setting by-default log in information False

    def __init__(self, name, email, password): # def __init__() is a built-in function called a constructor
        self.name = name
        self.email = email
        self.password = password

    def logIn(self, inEmail, inPassword): # self is a python keyword for calling class
        if inEmail == self.email and inPassword == self.password:
            self.isLoggedIn = True
            print("Log In Successful")
            print(f"Name : {self.name}")
            print(f"E-mail : {self.email}")
            print(f"Log In Status : {self.isLoggedIn}")
        else:
            print("Log In Failed")
            print(f"Log In Status : {self.isLoggedIn}")




userEmail = input("Enter your E-mail: ").lower()
userPassword = input("Enter your Password: ")

'''
We can store data for multiple users in this process.
Calling User() function each time will store data for individuals.
An example is given below:
'''

user1 = User("Niloy Datta", "niloydatta000@gmail.com", "*****")
user1.logIn(userEmail, userPassword)

'''
To create another profile just copy the below syntax and set its values.

user2 = User()
user2.logIn(userEmail, userPassword)

'''