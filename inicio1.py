from reto_1  import Persona

class Inicio:
    def __init__(self):
        self.persona = Persona()

    def ejecutar(self):
        persona1 = Persona("", "", "", "", 0.0, 0.0, 0, "")
        persona1.pedirDatos()
        persona1.mostrarPersona()
        persona1.calcularImc()
        persona1.mayorEdad()

inicio = Inicio()
inicio.ejecutar()
