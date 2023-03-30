competidores = {}
num_competidores = int(input("Ingrese el número de competidores: "))

# Registro de competidores
for i in range(num_competidores):
    nombre = input("Ingrese el nombre del competidor {}: ".format(i+1))
    competidores[nombre] = 0

# Registro de tiempos de competidores
for nombre in competidores:
    tiempo = float(input("Ingrese el tiempo de {} (en segundos): ".format(nombre)))
    competidores[nombre] = tiempo

# Mostrar en pantalla los tiempos de cada competidor
print("\nTiempo de cada competidor:")
for nombre, tiempo in competidores.items():
    print(nombre, "-", tiempo, "segundos")

# Determinar el ganador
ganador = min(competidores, key=competidores.get)
print("\nEl ganador es:", ganador, "con un tiempo de", competidores[ganador], "segundos.")
