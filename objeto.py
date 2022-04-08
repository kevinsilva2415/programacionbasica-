

class alumno:
    def __init__(self,nombre):
        
        self.nombre=nombre
    def saludar(self):
        print(f"hola,{self.nombre}")

objeto=alumno("kevin")
objeto.saludar()