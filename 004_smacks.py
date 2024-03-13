import random


preguntas = [
    ("¿En qué categorías pueden agruparse las conexiones de un router Cisco?", [
        "q) Routers de interfaz y routers de administración de banda.",
        "w) Interfaces de router de administración y routers de puertos de banda.",
        "e) Interfaces de router en banda y puertos de administración.",
        "r) Routers de banda y router de administración."
    ], "e"),
        ("¿Qué formas de acceder al modo EXEC en el entorno CLI en un router Cisco existen?", [
        "q) Consola, Shell Seguro (SSH) y Telnet.",
        "w) Modo seguro y modo experto.",
        "e) Modo cliente y modo experto.",
        "r) Modo cliente, modo seguro y Telnet."
    ], "q"),
        ("¿Qué descripción define mejor el modo de acceder al modo EXEC en el entorno CLI en modo consola?", [
        "q) Es un puerto de administración lógica que proporciona acceso en banda a un dispositivo de Cisc.",
        "w)  Es un puerto de administración físico que proporciona acceso fuera de banda a un dispositivo de Cisco.",
        "e) Es un puerto de administración lógica que proporciona acceso fuera de banda a un dispositivo de Cisc.",
        "r) Es un puerto de administración físico que proporciona acceso en banda a un dispositivo de Cisc."
    ], "w"),
        ("¿A qué hace referencia el acceso fuera de banda?", [
        "q) Al acceso por un canal de administración inclusivo que se usa únicamente con fines de administración del dispositivo.",
        "w) Al acceso por un canal de administración inclusivo que se usa únicamente con fines de mantenimiento del dispositivo.",
        "e) Al acceso por un canal de administración exclusivo que se usa únicamente con fines de administración del dispositivo.",
        "r)  Al acceso por un canal de administración exclusivo que se usa únicamente con fines de mantenimiento del dispositivo."
    ], "r"),
        ("¿Cómo se caracteriza el modo de accedo en Shell Seguro (SSH)?", [
        "q) Es un método para establecer de manera remota una conexión CLI segura a través de una interfaz virtual por medio de una red.",
        "w) Es un método para establecer de manera local una conexión CLI segura a través de una interfaz virtual por medio de una red.",
        "e) Es un método para establecer de manera local una conexión CLI segura a través de una interfaz física por medio de una red.",
        "r) Es un método para establecer de manera remota una conexión CLI segura a través de una interfaz física por medio de una red."
    ], "q"),
        ("A diferencia de las conexiones de consola, las conexiones SSH requieren...", [
        "q) ...dispositivos físicos de red activos, incluida una interfaz activa configurada con una dirección.",
        "w) ...servicios de red activos en el dispositivo, incluida una interfaz activa configurada con una dirección.",
        "e) ...servicios de red activos en el dispositivo, incluida una interfaz lógica configurada con una dirección.",
        "r) ...servicios de red activos en el dispositivo, sin que sea necesaria una interfaz activa configurada con una dirección."
    ], "w"),
        ("¿Qué es Telnet, tío?", [
        "q) Es un método seguro para establecer una sesión CLI de manera remota a través de una interfaz virtual por medio de una red.",
        "w) Es un método seguro para establecer una sesión CLI de manera local a través de una interfaz virtual por medio de una red.",
        "e) Es un método inseguro para establecer una sesión CLI de manera remota a través de una interfaz virtual por medio de una red.",
        "r) Es un método inseguro para establecer una sesión CLI de manera remota a través de una interfaz física por medio de una red."
    ], "e"),
        ("A diferencia de las conexiones SSH, Telnet no proporciona una conexión cifrada de manera segura.", [
        "q) Es así.",
        "r) No, es al revés."
    ], "q"),
            ("A diferencia de las conexiones Telnet, SSH no proporciona una conexión cifrada de manera segura.", [
        "q) Es así.",
        "r) No, es al revés."
    ], "r"),
        ("En Telnet,  La autenticación de usuario, las contraseñas y los comandos se envían...", [
        "q) ...por la red en texto no cifrado.",
        "w) ...por la red en texto cifrado.",
        "e) ...por la red en hexadecimal.",
        "r) ...por la red, sin importar el cómo."
    ], "q"),
        ("Elije la opción correcta", [
        "q) Algunos dispositivos, como los routers, también pueden admitir un puerto auxiliar nuevo que se haya utilizado para establecer una sesión CLI vía remota con un módem. De manera similar a la conexión de consola, el puerto auxiliar está fuera de banda y no se requieren servicios de red para configurarlo o para que esté disponible.",
        "w) Algunos dispositivos, como los routers, también pueden admitir un puerto auxiliar antiguo que se haya utilizado para establecer una sesión CLI vía remota con un módem. De manera similar a la conexión de consola, el puerto auxiliar está fuera de banda y no se requieren servicios de red para configurarlo o para que esté disponible.",
        "e) Algunos dispositivos, como los routers, también pueden admitir un puerto auxiliar antiguo que se haya utilizado para establecer una sesión Telnet vía remota con un módem. De manera similar a la conexión de consola, el puerto auxiliar está fuera de banda y no se requieren servicios de red para configurarlo o para que esté disponible.",
        "r) Algunos dispositivos, como los routers, también pueden admitir un puerto auxiliar antiguo que se haya utilizado para establecer una sesión CLI vía remota con un módem. De manera similar a la conexión de consola, el puerto auxiliar está en banda y se requieren servicios de red para configurarlo o para que esté disponible."
    ], "w"),
        ("Telnet y SSH necesitan una conexión de red en banda, lo que significa que un administrador debe acceder al router a través de una de las interfaces de la red LAN o WAN.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("Telnet y SSH no necesitan una conexión de red en banda, lo que significa que un administrador no tiene por qué acceder al router a través de una de las interfaces de la red LAN o WAN.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"),
        ("¿Qué reciben y envían las interfaces en banda?", [
        "q) Sentimientos.",
        "w) Protocolos IP.",
        "e) Paquetes IP.",
        "r) Direcciones MAC."
    ], "e"),
        ("¿Qué es cada interfaz configurada y activa en el router?", [
        "q) Una terminal lista para introducir instrucciones y configuraciones, como IPs.",
        "w) Un canal de trasmisión de paquetes IP.",
        "e) Un canal de trasmisión de bytes.",
        "r) Un miembro o host de una red IP diferente."
    ], "r"),
        ("Se debe configurar cada interfaz con una dirección IPv4 y una máscara de subred de una red diferente", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("No es necesario configurar cada interfaz con una dirección IPv4 y una máscara de subred de una red diferente, basta con configurar una única interfaz", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"),
        ("Cisco IOS no permite que dos interfaces activas en el mismo router pertenezcan a la misma red", [
        "q) Exacto.",
        "r) Mentira."
    ], "q"),
        ("Cisco IOS permite que dos interfaces activas en el mismo router pertenezcan a la misma red", [
        "q) Exacto.",
        "r) Mentira."
    ], "r")

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
