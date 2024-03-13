import random


preguntas = [
    ("¿Cuántos tipo de routers de infraestructura hay disponibles?", [
        "q) Muchos.",
        "w) Pocos.",
        "e) Uno.",
        "r) No lo sé."
    ], "q"),
    ("Los routers Cisco están diseñados para satisfacer las necesidades de muchos tipos diferentes de redes y empresas", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
    ("¿Qué tipo de redes satisface los routers CISCO?", [
        "q) De sucursal, WAN, Proveedor de servicios.",
        "w) Clase A, de clase B y de clase C.",
        "e) LAN, WAN, PAN.",
        "r) No te voy a mentir: no lo sé."
    ], "q"),
    ("¿Qué routers incluye CISCO para las redes de sucursal, como teletrabajadores, pequeñas empresas y sitios de sucursales medianas?", [
        "q) ACA15 y LNDK93.",
        "w) ISR (routers de servicios integrados) y CISCO G2.",
        "e) CISCO primera generación (G1) y CISCO segunda generación (2G).",
        "r) CRS-3 y los de la serie 7600."
    ], "w"),
    ("¿Qué routers incluye CISCO para las redes WAN, como las de grandes empresas, organizaciones y empresas?", [
        "q) Switches de clase G3 y routers ISR.",
        "w) Switches de la serie CISCO Catalyst y los routers de servicios de agregación (ASR) de CISCO.",
        "e) Switches de la serie CISCO Blackwhite y los routers de servicios de agregación (ARR) de CISCO.",
        "r) Cisco CSR-3 y los routers de la serie 7600."
    ], "w"),
    ("¿Qué routers incluye CISCO para las redes de proveedor de servicios, como grandes proveedores de servicios?", [
        "q) el sistema de proveedor de routing CISCO G2  y los routers de la serie 7600.",
        "w) Los ASR de CISCO, el sistema de proveedor de routing CISCO CRS-3  y los routers de la serie 7600.",
        "e) El sistema de proveedor de routing CISCO CRS-3  y los routers de la serie 7600.",
        "r) el sistema de proveedor de routing CISCO CRS-2  y los routers de la serie 6700."
    ], "w"),
    ("La certificación CCNA se concentra...", [
        "q) En todas las anteriores.",
        "w) En los routers de redes WAN.",
        "e) En los routers de sucursal.",
        "r) En los routers de proveedores de servicios."
    ], "e"),
    ("Sin importar cuál sea su función, tamaño o complejidad, todos los modelos de router son, en esencia, ...", [
        "q) ...PC.",
        "w) ...Memorias RAM.",
        "e) ...Microprocesadores.",
        "r) ...Switches."
    ], "q"),
    ("Al igual que las PC, las tabletas y los dispositivos inteligentes, los routers también necesitan lo siguiente:", [
        "q) Una batería, un monitor para la salida de datos y algún dispositivo de entrada.",
        "w) CPU, Sistema Operativo, RAM y algún dispositivo para la entrada de datos.",
        "e) CPU, Sistema Operativo y RAM.",
        "r) CPU, Sistema Operativo, RAM, ROM y NVRAM."
    ], "r"),
    ("Al igual que todas las PC, las tabletas, las consolas de juegos y los dispositivos inteligentes, los dispositivos Cisco necesitan una ...(1) para ejecutar las instrucciones del ...(2), como la inicialización del sistema, las funciones de ...(3) y de ...(4)", [
        "q) (1) RAM; (2) microprocesador; (3) encendido; (4) apagado.",
        "w) (1) RAM; (2) CPU; (3) routing; (4) switching.",
        "e) (1) CPU; (2) Microprocesador; (3) encendido; (4) apagado.",
        "r) (1) CPU; (2) SO; (3) routing; (4) switching."
    ], "r"),
    ("¿Qué función desempeña el disipador térmico de un router?", [
        "q) Ayuda a disipar el calor que generan la tarjeta de red y la RAM.",
        "w) Ayuda a disipar el calor que genera la RAM.",
        "e) Ayuda a disipar el calor que genera la CPU.",
        "r) Ayuda a disipar el exceso de voltaje que generan los diferentes componentes del router."
    ], "e")
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
