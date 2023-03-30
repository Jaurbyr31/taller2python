from reto_1 import Persona

class Empleado(Persona):
    def __init__(self, tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo, cargo, valorhora, horastrabajadas, departamento):
        super().__init__(tipoDoc, documento, nombre, apellido, peso, estatura, edad, sexo)
        self.cargo = cargo
        self.valorhora = valorhora
        self.horastrabajadas = horastrabajadas
        self.departamento = departamento
    
    def pedirDatosEmpleado(self):
        self.cargo = input("Ingrese el cargo del empleado: ")
        self.valorhora = float(input("Ingrese el valor por hora: "))
        self.horastrabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
        self.departamento = input("Ingrese el departamento del empleado: ")
        
    def calcularHonorarios(self):
        honorarios = self.valorhora * self.horastrabajadas
        retencion = honorarios * 0.00966
        return honorarios - retencion
    
    def imprimirEmpleado(self):
        print("Tipo de documento:", self.tipoDoc)
        print("Número de documento:", self.documento)
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Cargo:", self.cargo)
        print("Horas trabajadas:", self.horastrabajadas)
        print("Valor por hora:", self.valorhora)
        print("Total a pagar:", self.calcularHonorarios())

    
    

empleado_nuevo = Empleado("CC", "1234567890", "Juan", "Perez", 70, 175, 30, "M", "Gerente", 50000, 40, "Ventas")
empleado_nuevo.pedirDatosEmpleado()
empleado_nuevo.imprimirEmpleado()
