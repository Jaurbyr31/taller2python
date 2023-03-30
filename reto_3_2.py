class Persona:
    def __init__(self):
        self.__tipoDoc = ""
        self.__documento = ""
        self.__nombre = ""
        self.__apellido = ""
        self.__peso = 0.0
        self.__estatura = 0.0
        self.__edad = 0
        self.__sexo = ""

    def pedirDatos(self):
        self.__tipoDoc = input("Ingrese Tipo de documento: ")
        self.__documento = input("Ingrese Número de documento: ")
        self.__nombre = input("Ingrese Nombre de la persona: ")
        self.__apellido = input("Ingrese Apellido de la persona: ")
        self.__peso = float(input("Ingrese Peso de la persona en kg: "))
        self.__estatura = float(input("Ingrese Estatura de la persona en mts: "))
        self.__edad = int(input("Ingrese la edad de la persona: "))
        self.__sexo = input("Escoja el Sexo de la persona (M/F): ").upper()

    def mostrarPersona(self):
        print("Tipo de documento:", self.__tipoDoc, "\n"
              "Número de documento:", self.__documento, "\n"
              "Nombre:", self.__nombre, "\n"
              "Apellido:", self.__apellido, "\n"
              "Peso:", self.__peso, "\n"
              "Estatura:", self.__estatura, "\n"
              "Edad:", self.__edad, "\n"
              "Sexo:", self.__sexo, "\n")
        
    def calcularImc(self):
        pesoActual = self.__peso / (self.__estatura ** 2)
        if pesoActual < 20:
            print("El peso de la persona está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso de la persona es ideal")
        else:
            print("La persona tiene sobrepeso")

    def mayorEdad(self):
        if self.__edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")
    
    # Métodos setters y getters
    def setTipoDoc(self, tipoDoc):
        self.__tipoDoc = tipoDoc
        
    def getTipoDoc(self):
        return self.__tipoDoc
    
    def setDocumento(self, documento):
        self.__documento = documento
        
    def getDocumento(self):
        return self.__documento
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
        
    def getApellido(self):
        return self.__apellido
    
    def setPeso(self, peso):
        self.__peso = peso
        
    def getPeso(self):
        return self.__peso
    
    def setEstatura(self, estatura):
        self.__estatura = estatura
        
    def getEstatura(self):
        return self.__estatura
    
    def setEdad(self, edad):
        self.__edad


persona = Persona()
persona.pedirDatos()
persona.mostrarPersona()
persona.calcularImc()
persona.mayorEdad()
