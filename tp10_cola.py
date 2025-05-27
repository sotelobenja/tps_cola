from collections import deque
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Notificacion:
    hora: str  # 'HH:MM'
    aplicacion: str
    mensaje: str

def convertir_hora(hora_str):
    return datetime.strptime(hora_str, "%H:%M").time()

# a
def eliminar_facebook(cola):
    nueva_cola = deque()
    while cola:
        noti = cola.popleft()
        if noti.aplicacion.lower() != "facebook":
            nueva_cola.append(noti)
    return nueva_cola

# b
def mostrar_twitter_python(cola):
    tamaño = len(cola)
    for _ in range(tamaño):
        noti = cola.popleft()
        if (noti.aplicacion.lower() == "twitter" and "python" in noti.mensaje.lower()):
            print(f"[{noti.hora}] {noti.aplicacion}: {noti.mensaje}")
        cola.append(noti)

# c
def notificaciones_entre_horas(cola, hora_inicio_str="11:43", hora_fin_str="15:57"):
    hora_inicio = convertir_hora(hora_inicio_str)
    hora_fin = convertir_hora(hora_fin_str)
    pila = []
    tamaño = len(cola)
    for _ in range(tamaño):
        noti = cola.popleft()
        hora_noti = convertir_hora(noti.hora)
        if hora_inicio <= hora_noti <= hora_fin:
            pila.append(noti)
        cola.append(noti)
    return len(pila), pila

cola_notificaciones = deque([
    Notificacion("10:15", "Facebook", "Nuevo comentario en tu foto"),
    Notificacion("11:50", "Twitter", "Python 3.10 ya está disponible"),
    Notificacion("14:22", "Instagram", "Te etiquetaron en una historia"),
    Notificacion("15:00", "Twitter", "Curso de Python avanzado"),
    Notificacion("16:05", "Facebook", "Recordatorio de evento"),
])

cola_notificaciones = eliminar_facebook(cola_notificaciones)

print("Notificaciones de Twitter con 'Python':")
mostrar_twitter_python(cola_notificaciones)

cantidad, pila_resultado = notificaciones_entre_horas(cola_notificaciones)
print(f"\nCantidad de notificaciones entre 11:43 y 15:57: {cantidad}")