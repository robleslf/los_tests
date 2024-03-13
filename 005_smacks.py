import random


preguntas = [
    ("¿Cuáles son las interfaces de router en banda?", [
        "q) Las interfaces de la red PAN (es decir, Gigabit Ethernet) y WAN (es decir, tarjetas de interfaz WAN de alta velocidad mejorada) configuradas con la asignación de direcciones IP para transportar el tráfico de usuarios.",
        "w) Las interfaces de la red LAN (es decir, Gigabit Ethernet) y WAN (es decir, tarjetas de interfaz WAN de alta velocidad mejorada) configuradas con la asignación de direcciones MAC para transportar el tráfico de usuarios.",
        "e) Las interfaces de la red LAN (es decir, Gigabit Ethernet) y WAN (es decir, Ethernet y RJ-45) configuradas con la asignación de direcciones IP para transportar el tráfico de usuarios.",
        "r) Las interfaces de la red LAN (es decir, Gigabit Ethernet) y WAN (es decir, tarjetas de interfaz WAN de alta velocidad mejorada) configuradas con la asignación de direcciones IP para transportar el tráfico de usuarios."
    ], "r"),
        ("¿Cuáles son las conexiones LAN más frecuentes?", [
        "q) Las interfaces WAN de alta velocidad mejorada.",
        "w) Las interfaces Ethernet.",
        "e) Las interfaces Serial.",
        "r) Las interfaces de consola."
    ], "w"),
        ("¿Qué interfaces incluyen las conexiones WAN comunes?", [
        "q) Ethernet.",
        "w) De consola.",
        "e) Seriales y DSL.",
        "r) De alta velocidad mejorada."
    ], "e"),
        ("¿Dónde se incluyen los puertos de administración?", [
        "q) En los puertos de consola y auxiliares.",
        "w) En los puertos Ethernet.",
        "e) En los puertos Gigabit Ethernet.",
        "r) En los puertos Ethernet y Gigabit Ethernet."
    ], "q"),
        ("¿Para qué se usan los puertos de administración incluidos en los puertos de consola y auxiliares?", [
        "q) Para configurar y administrar el router.",
        "w) Para configurar, administrar y solucionar problemas del puerto principal.",
        "e) Para configurar, administrar y solucionar problemas del router.",
        "r) Para configurar, administrar y solucionar problemas de la consola."
    ], "e"),
        ("Elije la opción correcta:", [
        "q) A diferencia de las interfaces de la red LAN, las redes WAN y los puertos de administración se utilizan para el envío de paquetes de tráfico de usuarios.",
        "w) A diferencia de las interfaces de la red LAN, las redes WAN y los puertos de administración no se utilizan para el envío de paquetes de tráfico de usuarios.",
        "e) A diferencia de las interfaces de la red LAN y WAN, los puertos de administración se utilizan para el envío de paquetes de tráfico de usuarios.",
        "r) A diferencia de las interfaces de la red LAN y WAN, los puertos de administración no se utilizan para el envío de paquetes de tráfico de usuarios."
    ], "r"),
        ("¿Dónde se agregan las interfaces WAN seriales?", [
        "q) A los puertos RJ-45.",
        "w) A las eHWIC0.",
        "e) A las eHWIC1.",
        "r) Al cable de consola."
    ], "w"),
        ("¿Qué rótulos tienen las interfaces WAN seriales?", [
        "q) Serial 0 (S0/0/0) y Serial 1 (S0/0/1).",
        "w) Serial 0 (S0/0) y Serial 1 (S0/1).",
        "e) Serial 0 (S0) y Serial 1 (S1).",
        "r) Serial 0 (S0/0) y Serial 1 (S1/1)."
    ], "q"),
        ("¿Para qué se usan las interfaces seriales?", [
        "q) Para conectar los routers a una red LAN interna.",
        "w) Para conectar los routers a una red WAN interna.",
        "e) Para conectar los routers a una red WAN externa.",
        "r) Para conectar los routers a una red LAN externa."
    ], "e"),
        ("Cada interfaz WAN serial tiene su propia dirección IP y su máscara de subred, que la identifican como miembro de una red específica.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("¿Qué rótulos tienen las interfaces de la red LAN Ethernet?", [
        "q) GbE 0/0 y GbE 0/1.",
        "w) GE 0/0 y GE 0/1.",
        "e) GB 0/0 y GB 0/1.",
        "r) GigE 0/0 y GigE 0/1."
    ], "W"),
        ("¿Para qué se usan las interfaces Ethernet?", [
        "q) Para conectar el mando de la play.",
        "w) Para conectarse a otros dispositivos sin necesidad de tener Ethernet habilitado, lo que incluye shiwtches, routers, firewalls, etc.",
        "e) Para conectarse a otros dispositivos con Ethernet habilitado, lo que actualmente solo incluye routers.",
        "r) Para conectarse a otros dispositivos con Ethernet habilitado, lo que incluye shiwtches, routers, firewalls, etc."
    ], "r"),
            ("Cada interfaz de la red LAN tiene su propia dirección IPv4 y su máscara de subred, o una dirección IPv6 y un prefijo, que la identifican como miembro de una red específica.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),

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
