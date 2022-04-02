
class Padre():
    def drive(self):
        print("Padre lleva a su hijo a la escuela")

class Madre():
    def cook(self):
        print("A la madre le encanta cocinar para su hijo.")

class Hijo(Padre, Madre):
    def love(self):
        print("Amo a mis Padres")
    
c=Hijo()
c.drive()
c.cook()
c.love()
