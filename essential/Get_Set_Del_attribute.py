class MyObject:
    def __init__(self):
        self.password = None

    def  __getattr__(self, item):
        if item == "login" and self.password == "password1234":
            return "login succeed"
        else:
            return object.__getattribute__(self, item)


user1 = MyObject()
print(user1)
user1.password = "password1234"
print(user1.login)
