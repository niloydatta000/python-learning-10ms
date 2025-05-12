#Object-Oriented Programming: Learning to create object

#Let's make a Program about how to log in.

class User:
    name = ""
    email = ""
    password = ""
    isLoggedIn = False # Setting by-default log in information False

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

user1 = User()
user1.name = "Niloy Datta"
user1.email = "niloydatta000@gmail.com"
user1.password = "*****"
user1.logIn(userEmail, userPassword)

'''
To create another profile just copy the below syntax and set its values.

user2 = User()
user2.name = " "
user2.email = " "
user2.password = " "
user2.logIn(userEmail, userPassword)

'''