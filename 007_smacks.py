import random

preguntas = [
    ("¿Para qué sirve el comando 'show version'?", [
        "q) Muestra información sobre la versión del software Cisco IOS que se ejecuta en ese momento en el router.",
        "w) Muestra información sobre la versión del software Cisco IOS que se ejecuta en ese momento en el router, la versión del programa de arranque e información sobre la configuración del hardware, incluida la cantidad de memoria del sistema.",
        "e) Muestra información sobre la versión del software Cisco IOS que se ejecuta en ese momento en el router, la versión del programa de arranque e información sobre la configuración del hardware, sin incluir la cantidad de memoria del sistema.",
        "r) Muestra información sobre la versión del software Cisco IOS que se ejecuta en ese momento en el router y la versión del programa de arranque."
    ], "w"),
        ("Los routers y switches Cisco tienen muchas similitudes. Admiten un sistema operativo similar, estructuras de comandos similares y muchos de los mismos comandos", [
        "q) Verdad.",
        "r) Mentira."
    ], "q"),
        ("Los routers y switches Cisco tienen muchas diferencias. Poseen un sistema operativo diferente cada uno, estructuras de comandos independientes y muchos de los comandos son diferentes en cada tipo de dispositivo.", [
        "q) Verdad.",
        "r) Mentira."
    ], "r"),
        ("Los routers y los switches de Cisco  usan los mismos pasos de configuración inicial cuando se implementan en una red.", [
        "q) Sí.",
        "r) No."
    ], "q"),
        ("Los routers y los switches de Cisco  usan pasos de configuración inicial diferentes cuando se implementan en una red.", [
        "q) Sí.",
        "r) No."
    ], "r"),
        ("¿Cuál es el comando para configurar el nombre de dispositivo en un swithc?", [
        "q) switch-name (nombre).",
        "w) host-name (nombre).",
        "e) hostname (nombre).",
        "r) switch-name (nombre)."
    ], "e"),
        ("Proteger el modo EXEC del usuario en un switch:", [
        "q) line console 0 → password (contraseña) → login.",
        "w) line console 0 → password (contraseña) → exit.",
        "e) execmode → password (contraseña) → login.",
        "r) execmode → password (contraseña) → exit."
    ], "q"),
        ("Proteger el modo EXEC privilegiado en un switch", [
        "q) enable mode (contraseña).",
        "w) enable secret (contraseña).",
        "e) exec secret (contraseña).",
        "r) enable password (contraseña)."
    ], "w"),    
    ("Proteger el acceso remoto por Telnet y SSH en un switch", [
        "q) line vty 0 15 → password (contraseña) → login.",
        "w) line 15 → password (contraseña) → login.",
        "e) line vty → password (contraseña) → login.",
        "r) line vty 0 15 → password (contraseña) → exit."
    ], "q"),
        ("Proteger todas las contraseñas en el archivo de configuración", [
        "q) protect password encryption.",
        "w) protect password-encryption.",
        "e) service password-encryption.",
        "r) service password encryption."
    ], "e"),
        ("Proporcionar la notificación legal en un switch:", [
        "q) banner motd (delimitador mensaje delimitador).",
        "w) banner mod (delimitador mensaje delimitador).",
        "e) warning mod (delimitador mensaje delimitador).",
        "r) warning mod (mensaje)."
    ], "q"),
        ("Configurar la SVI de administración en un switch:", [
        "q) interface vlan → ip address (dirección IP).",
        "w) interface vlan 1 → ipv4 mask (dirección IP máscara de subred).",
        "e) interface vlan → ip mask (dirección IP máscara de subred).",
        "r) interface vlan 1 → ip address (dirección IP máscara de subred)."
    ], "r"),
        ("Guardar la configuración de un switch:", [
        "q) copy startup-config running-config.",
        "w) copy running-config start-config.",
        "e) copy running-config startup-config.",
        "r) copy running config start config."
    ], "e"),
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
