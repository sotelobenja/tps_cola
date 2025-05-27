from collections import deque
from dataclasses import dataclass

@dataclass
class PersonajeMCU:
    nombre_personaje: str
    nombre_superheroe: str
    genero: str  # 'M' o 'F'

def cargar_personajes():
    return deque([
        PersonajeMCU("Tony Stark", "Iron Man", "M"),
        PersonajeMCU("Steve Rogers", "Capitán América", "M"),
        PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
        PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
        PersonajeMCU("Scott Lang", "Ant-Man", "M"),
        PersonajeMCU("Stephen Strange", "Doctor Strange", "M"),
        PersonajeMCU("Sam Wilson", "Falcon", "M"),
        PersonajeMCU("Shuri", "Black Panther", "F")
    ])

# a
def obtener_personaje_de_superheroe(cola, nombre_superheroe):
    for personaje in cola:
        if personaje.nombre_superheroe.lower() == nombre_superheroe.lower():
            return personaje.nombre_personaje
    return "No encontrado"

# b
def mostrar_superheroinas(cola):
    return [p.nombre_superheroe for p in cola if p.genero.upper() == "F"]

# c
def mostrar_personajes_masculinos(cola):
    return [p.nombre_personaje for p in cola if p.genero.upper() == "M"]

# d
def obtener_superheroe_de_personaje(cola, nombre_personaje):
    for personaje in cola:
        if personaje.nombre_personaje.lower() == nombre_personaje.lower():
            return personaje.nombre_superheroe
    return "No encontrado"

# e
def mostrar_datos_comienzan_con_s(cola):
    return [
        p for p in cola
        if p.nombre_superheroe.lower().startswith('s') or p.nombre_personaje.lower().startswith('s')
    ]

# f
def buscar_personaje(cola, nombre_personaje):
    for personaje in cola:
        if personaje.nombre_personaje.lower() == nombre_personaje.lower():
            return True, personaje.nombre_superheroe
    return False, None

cola_personajes = cargar_personajes()

print("a. Personaje de 'Capitana Marvel':", obtener_personaje_de_superheroe(cola_personajes, "Capitana Marvel"))

print("\nb. Superhéroes femeninos:")
print(mostrar_superheroinas(cola_personajes))

print("\nc. Personajes masculinos:")
print(mostrar_personajes_masculinos(cola_personajes))

print("\nd. Superhéroe de 'Scott Lang':", obtener_superheroe_de_personaje(cola_personajes, "Scott Lang"))

print("\ne. Personajes o superhéroes cuyos nombres comienzan con 'S':")
for p in mostrar_datos_comienzan_con_s(cola_personajes):
    print(p)

print("\nf. ¿Está Carol Danvers?")
encontrado, heroe = buscar_personaje(cola_personajes, "Carol Danvers")
if encontrado:
    print(f"Sí, su nombre de superhéroe es: {heroe}")
else:
    print("No se encuentra en la cola.")