class user:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name, email, password):
         self.name = name
         self.email = email
         self.password = password

    def login(self):
       
        email= input("enter email ")
        password=input("Enter Password ")

        if email == self.email and  password == self.password:
            login = True
            print("Login Successful")

        else:
            print("Login Failed")

    def logout(self):
        login = False
        print("Logged out!")

    def isLogin(self):
        if self.login:
            return True
        else :
            return False
        
    def profile(self):
        if self.isLogin():
           print(self.name,"\n",self.email)
        else:
            print("User is not logged in!")

user1 = user("Mithila", "mithila20@gmail.com", "123456")

# user1.name = "Mithila"
# user1.email = "mithila20@gmail.com"
# user1.password = "123456"

user1.login()
user1.profile()
         

        
