import random


preguntas = [
    ("¿Qué utilizan los dispositivos CISCO para brindar información acerca de su estado?", [
        "q) Un monitor portátil de pequeño tamaño.",
        "w) Indicadores de diodo emisor de luz (LED).",
        "e) Calambres y descargas eléctricas, por lo que es recomendable el uso de guantes aislantes de goma.",
        "r) Señales acústicas similares a las utilizadas por la BIOS."
    ], "w"),
    ("¿Qué indica un LED de interfaz?", [
        "q) La actividad de la interfaz correspondiente.",
        "w) Que la interfaz está desactivada.",
        "e) Nada, su único fin es estético.",
        "r) El LED de interfaz no indica nada relacionado con la propia interfaz."
    ], "q"),
    ("¿Qué puede indicar un LED que está apagado cuando la interfaz está activa y la interfaz está conectada correctamente?", [
        "q) Que hay un problema con esa interfaz.",
        "w) Que la interfaz está funcionando correctamente.",
        "e) Que la conexión se ha perdido temporalmente en esa interfaz.",
        "r) Las interfaces no llevan leds asignados."
    ], "q"),
    ("Si una interfaz está sobrecargada, su LED está...", [
        "q) Apagado permanentemente.",
        "w) Encendido y apagado intermitentemente.",
        "e) Encendido permanentemente.",
        "r) parpadenado en ráfagas de tres intermitencias."
    ], "e"),
    ("¿Cuál de estas ranuras tiene un router?", [
        "q) Ranuras para tarjeta de interfaz LAN de alta velocidad (eHLIC).",
        "w) Ranuras para tarjeta de interfaz LAN de alta velocidad mejorada (eHLIC).",
        "e) Ranuras para tarjeta de interfaz WAN de alta velocidad mejorada (eHWIC).",
        "r) Ranuras para tarjeta de interfaz WAN de alta velocidad (eHWIC)."
    ], "e"),
    ("¿Por qué las ranuras para tarjeta de interfaz WAN tienen el rótulo eHWIC 0 y eHWIC 1?", [
        "q) ¿Cómo pretendes que lo sepa si no he estudiado?.",
        "w) Los routers no incluyen ranuras para ese tipo de tarjetas.",
        "e) para proporcionar modularidad y flexibilidad al permitir que el router admita distintos tipos de módulos de interfaz, din incluir serial, línea de suscriptor digital (DSL), puerto de switch y tecnología inalámbrica.",
        "r) para proporcionar modularidad y flexibilidad al permitir que el router admita distintos tipos de módulos de interfaz, incluidos serial, línea de suscriptor digital (DSL), puerto de switch y tecnología inalámbrica."
    ], ""),
    ("¿Qué rótulo tienen las ranuras CompactFlash de un router?", [
        "q) el rótulo CF1 y CF2.",
        "w) el rótulo CF0 y CF1.",
        "e) el rótulo CF01 y CF11.",
        "r) el rótulo CF01 y CF02."
    ], "w"),
    ("¿Por qué en los routers, las ranuras CompactFlash vienen con el rótulo CF0 y CF1?", [
        "q) Para proporcionar una mayor cantidad de espacio de almacenamiento en memoria flash expansible con tarjetas CompactFlash de hasta 8 GB por ranura.",
        "w) Para proporcionar una mayor cantidad de espacio de almacenamiento en memoria flash compacta con tarjetas CompactFlash de hasta 4 GB por ranura.",
        "e) Para proporcionar una mayor cantidad de espacio de almacenamiento en memoria flash expansible con tarjetas CompactFlash de hasta 4 GB por ranura.",
        "r) Para proporcionar una mayor cantidad de espacio de almacenamiento en memoria flash expansible con tarjetas CompactFlash de hasta 16 GB por ranura."
    ], "e"),
    (" De manera predeterminada, la ranura CF0 tiene una tarjeta CompactFlash de ...(1) MB y es la ubicación predeterminada de ...(2).", [
        "q) (1): 128; (2): arranque.",
        "w) (1): 256; (2): conexión.",
        "e) (1): 128; (2): conexión.",
        "r) (1): 256; (2): arranque."
    ], "r"),
    ("¿Para qué y cuál es el puerto Auxiliar (AUX) de un router?", [
        "q) Para el acceso a la administración remota, similar al puerto de consola, es un puerto RJ-45.",
        "w) Para el acceso a la administración local, similar al puerto de consola, es un puerto Gigabit.",
        "e) Para el acceso a la administración remota, similar al puerto de consola, es un puerto Gigabit.",
        "r) Para el acceso a la administración local, similar al puerto de consola."
    ], "q"),
    ("El puerto AUX de un router ahora se considera un puerto antiguo, ya que se lo usaba para admitir los módems dial up.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
    ("Qué rotulos tienen las interfaces Gigabit Ethernet de un router?", [
        "q) GE0/0 y GE1/1.",
        "w) GE0/0 y GE0/1.",
        "e) GE1/0 y GE1/1.",
        "r) GE1/0 y GE0/1."
    ], "w"),
    ("¿Para qué se usan por lo general las interfaces Gigabit Ethernet?", [
        "q) Para proporcionar acceso remoto mediante la conexión con routers y usuarios.",
        "w) Para proporcionar acceso LAN mediante la conexión con switches y routers.",
        "e) Para proporcionar acceso LAN mediante la conexión con switches y usuarios, o para interconectarse a otro router.",
        "r) Para nada, no vamos a engañarnos."
    ], "e"),
    ("¿Para qué se usan por lo general los puertos de consola de un router?", [
        "q) Para echarse un mario kart.",
        "w) Para el acceso a la administración local, similar al puerto de consola, es un puerto RJ-45.",
        "e) Para proporcionar acceso LAN mediante la conexión con switches y usuarios, o para interconectarse a otro router.",
        "r) Para acceder a la administración de la configuración inicial y de la interfaz de línea de comandos (CLI)."
    ], "r"),
    ("¿Cuántos y cuáles son los puertos de consola más comunes en un router CISCO?", [
        "q) Dos: el puerto de uso más frecuente (puerto RJ-45 común) y un nuevo conector USB de tipo B (USB mini-B).",
        "w) Tres: el puerto de uso más frecuente (puerto RJ-45 común) y dos nuevos conectores USB de tipo A (USB mini-A) y tipo B (USB mini-B).",
        "e) Uno, un puerto RJ-45.",
        "r) Depende del modelo y del tipo de router utilizado."
    ], "q"),
    ("Se puede acceder a la consola del router por varios puertos a la vez.", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"),
    ("¿Para qué sirven los puertos USB con los rótulos USB 0 y USB 1 de un router?", [
        "q) Para guardar las tablas de enrutamiento.",
        "w) Para conectar un ratón o teclado y poder operar en la consola (CLI).",
        "e) Para proporcionar espacio de almacenamiento adicional, similar a la memoria flash.",
        "r) Para pasar música al router."
    ], ""),
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
