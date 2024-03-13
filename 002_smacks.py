import random


preguntas = [
    ("¿Cuál de las siguientes aplicaciones y procesos no utiliza la RAM del router?", [
        "q) El archivo de configuración en ejecución y la imagen de IOS.",
        "w) La tabla de routing se utiliza para determinar el mejor camino para reenviar paquetes.",
        "e) IOS limitado para proporcionar una versión de respaldo del IOS",
        "r) La caché ARP que se usa para asignar direcciones IPv4 a las direcciones MAC.",
        "d) El búfer de paquetes que se usa de manera temporal para almacenar paquetes antes de reenviarlos al destino."
    ], "e"),
        ("La memoria RAM utiliza Información de arranque que proporciona las instrucciones de inicio.", [
        "q) Verdadero.",
        "r) Falso."
    ], "f"),
        ("La memoria RAM utiliza Autodiagnóstico al encender (POST) que evalúa todos los componentes de hardware.", [
        "q) Verdadero.",
        "r) Falso."
    ], "f"),
        ("La memoria RAM utiliza IOS limitado para proporcionar una versión de respaldo del IOS. Se usa para cargar el IOS con todas las funciones si este se daña o elimina.", [
        "q) Verdadero.",
        "r) Falso."
    ], "f"),    
            ("La memoria RAM utiliza IOS limitado para proporcionar una versión de respaldo del IOS. Se usa para cargar el IOS con todas las funciones si este se daña o elimina.", [
        "q) Verdadero.",
        "r) Falso."
    ], "f"), 
            ("La memoria RAM utiliza El archivo de configuración en ejecución y la imagen de IOS.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"), 
                ("La memoria RAM utiliza La tabla de routing que se utiliza para determinar el mejor camino para reenviar paquetes.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"), 
                    ("La memoria RAM utiliza La caché ARP que se usa para asignar direcciones IPv4 a las direcciones MAC.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"), 
                        ("La memoria RAM utiliza El búfer de paquetes que se usa de manera temporal para almacenar paquetes antes de reenviarlos al destino.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"), 
            ("La memoria ROM almacena Información de arranque que proporciona las instrucciones de inicio.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("La memoria ROM almacena Autodiagnóstico al encender (POST) que evalúa todos los componentes de hardware.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("La memoria ROM almacena IOS limitado para proporcionar una versión de respaldo del IOS. Se usa para cargar el IOS con todas las funciones si este se daña o elimina.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),    
            ("La memoria ROM almacena IOS limitado para proporcionar una versión de respaldo del IOS. Se usa para cargar el IOS con todas las funciones si este se daña o elimina.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"), 
            ("La memoria ROM almacena El archivo de configuración en ejecución y la imagen de IOS.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"), 
                ("La memoria ROM almacena La tabla de routing que se utiliza para determinar el mejor camino para reenviar paquetes.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"), 
                    ("La memoria ROM almacena La caché ARP que se usa para asignar direcciones IPv4 a las direcciones MAC.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"), 
                        ("La memoria ROM almacena El búfer de paquetes que se usa de manera temporal para almacenar paquetes antes de reenviarlos al destino.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"), 
            ("Aunque existen diferentes tipos y modelos de routers, todos tienen los mismos componentes generales de hardware", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
            (" Un profesional de redes no tiene por qué conocer y comprender la función de los componentes internos principales de un router, sino la ubicación exacta de estos dentro de un router específico. Estos componentes se encuentran siempre en el mismo sitio sin importar el modelo", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"),
            ("Por lo general, los switches, routers y dispositivos Cisco interconectan muchos dispositivos. Es por este motivo que estos dispositivos tienen diferentes tipos de puertos e interfaces que se usen para conectarse al dispositivo.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q")
]



######################################################################################

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)

# Función para calcular la equivalencia de la puntuación en una nota sobre 10
def calcular_equivalencia_puntuacion(puntuacion, total_preguntas):
    escala_maxima = 10.0
    equivalencia = (puntuacion / total_preguntas) * escala_maxima
    return equivalencia

# Función para realizar el test
def realizar_test():
    puntaje = 0
    total_preguntas = len(preguntas)

    for i, (pregunta, opciones, respuesta) in enumerate(preguntas, 1):
        print(f"\nPregunta {i}: {pregunta}")
        random.shuffle(opciones)
        for opcion in opciones:
            print(opcion)
        respuesta_usuario = input("\nTu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta:
            print("-------------------------")
            print("¡Respuesta correcta! ✔✔✔✔✔✔✔✔✔")
            print("-------------------------\n")
            puntaje += 1
        else:
            print("-------------------------")
            print(f"✖✖✖✖✖✖✖ Respuesta incorrecta. La opción correcta es: {respuesta}\n")
            print("-------------------------\n")
    
    equivalencia = calcular_equivalencia_puntuacion(puntaje, total_preguntas)
    
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f"  Has completado el test, {nombre_usuario}. Puntuación final: {puntaje}/{total_preguntas}")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                                                  ==========")
    print(f"Tu equivalencia de nota sobre 10 es ━━━━━━━━━━━━❯✷ {equivalencia:.2f}/10 ✷❮━━━━━━━━━━━━")
    print("                                                  ==========")

# Solicitar el nombre del usuario
nombre_usuario = input("Bienvenido al test de Fundamentos. Por favor, introduce tu nombre: ")

# Solicitar el número de preguntas
num_preguntas = int(input("¿Cuántas preguntas deseas en el test? "))
while num_preguntas > len(preguntas):
    print(f"Lo siento, solo hay {len(preguntas)} preguntas disponibles.")
    num_preguntas = int(input("Por favor, elige un número igual o menor: "))

# Mezclar las preguntas en orden aleatorio
random.shuffle(preguntas)
preguntas = preguntas[:num_preguntas]

# Ejecutar el test
print(f"Muy bien, {nombre_usuario}! Comencemos con tu test de Fundamentos con {num_preguntas} preguntas.")
realizar_test()
