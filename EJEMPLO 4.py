
class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        
    def display_user(self):
        print("User name is: ", self.name)
        print("User age is : ", self._age)

user1 = User("Jhon Doe", 35)

# Llamando al metodo de la clase
user1.display_user()

# Accediendo directamente a las variables
user1.name
user1._age 
