class Persona:
    def __init__(self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo):
        self.tipoDoc = tipoDoc
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.estatura = estatura
        self.edad = edad
        self.sexo = sexo
    
    def pedirDatos(self):
        self.tipoDoc = input("Ingrese el tipo de documento: ")
        self.documento = input("Ingrese el número de documento: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.peso = float(input("Ingrese el peso en kg: "))
        self.estatura = float(input("Ingrese la estatura en metros: "))
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo (M/F): ")
    
    def mostrarPersona(self):
        print("Tipo de documento:", self.tipoDoc)
        print("Número de documento:", self.documento)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Peso en kg:", self.peso)
        print("Estatura en metros:", self.estatura)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
    
    def calcularImc(self):
        pesoActual = self.peso / (self.estatura ** 2)
        if pesoActual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayorEdad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")
