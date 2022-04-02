
class Animales:
    def __init__(self, nombre_animal):
        print(nombre_animal, 'es un animal.');


class Mamifero(Animales):
    def __init__(self, nombre):
        print(nombre, 'es un Mamifero.')
        super().__init__(nombre)
    

class NoVuelan(Mamifero):
      def __init__(self, Nombre):
        print(Nombre, "NO puede volar.")
        super().__init__(Nombre)


class NoNadan(Mamifero):
    def __init__(self, Nombre):
        print(Nombre, "NO puede nadar.")
        super().__init__(Nombre)


class Gato(NoNadan, NoVuelan):
    def __init__(self):
        print('Un Gato.');
        super().__init__('Gat')

gato = Gato()
print('')
murcielago = NoNadan('Bat')
