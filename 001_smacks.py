import random


preguntas = [
    ("La CPU de un router necesita que un SO le provea las funciones de routing y switching", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
    ("¿Cuáles el software de sistema que se usa para la mayoría de los dispositivos Cisco ?", [
        "q) Depende el tamaño y tipo de dispositivo.",
        "w) El sistema operativo Internetwork (IOS) de Cisco.",
        "e) El sistema operativo Dualway (DOS) de Cisco.",
        "r) El sistema operativo NetworkRouting  (NR-OS) de Cisco."
    ], "w"),
    ("El sistema operativo Internetwork (IOS) de CISCO...", [
        "q) ...se usa tanto para routers como para switches.",
        "w) ...se usa exclusivamente para routers.",
        "e) ...se usa para routers, switches LAN, puntos de acceso inalámbrico pequeños, routers grandes con múltiples interfaces y muchos otros dispositivos.",
        "r) ...se usa ."
    ], "e"),
    ("¿A qué tiene acceso un router en cuanto a la memoria?", [
        "q) Tanto a un almacenamiento de memoria volátil como no volátil.",
        "w) No tiene acceso a ningún almacenamiento de memoria.",
        "e) A un almacenamiento de memoria volátil.",
        "r) A un almacenamiento de memoria no volatil."
    ], "q"),
    ("¿Qué pasa con la memoria volátil del router cuando este se apaga o se reinicia?", [
        "q) El contenido se borra y se pierde cuando se apaga, pero no cuando se reinicia.",
        "w) El contenido se borra y se pierde en ambas situaciones.",
        "e) El contenido se mantiene en ambas situaciones.",
        "r) El contenido se borra y se pierde solo al reiniciar, pero no al apagar."
    ], "w"),
    ("La memoria no volátil retiene la información incluso cuando se reinicia el dispositivo.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
    ("¿Qué tipos de memoria utiliza un router CISCO?", [
        "q) RAM, ROM y NVRAM.",
        "w) RAM, ROM, NVRAM, SD y Flash.",
        "e) RAM y ROM.",
        "r) RAM, ROM, NVRAM y Flash."
    ], "r"),
    ("Los routers Cisco usan un tipo rápido de RAM denominado...", [
        "q) memoria asincrónica dinámica de acceso aleatorio (ADRAM).",
        "w) memoria asíncrona dinámica de acceso aleatorio (ADRAM).",
        "e) memoria sincrónica estática de acceso aleatorio (SSRAM).",
        "r) memoria sincrónica dinámica de acceso aleatorio (SDRAM)."
    ], "r"),
    ("¿Para que usa la memoria RAM un router CISCO?", [
        "q)  se usa como almacenamiento permanente del IOS y otros archivos relacionados con el sistema, como archivos de registro, archivos de configuración de voz, archivos HTML, configuraciones de respaldo, entre otros.",
        "w)  para almacenar instrucciones operativas cruciales y un IOS limitado. .",
        "e) para almacenar aplicaciones, procesos y los datos necesarios para que la CPU los pueda ejecutar.",
        "r) se usa como almacenamiento permanente para el archivo de configuración de inicio (startup-config)."
    ], "e"),
    ("¿Para que usa la memoria ROM un router CISCO?", [
        "q)  se usa como almacenamiento permanente del IOS y otros archivos relacionados con el sistema, como archivos de registro, archivos de configuración de voz, archivos HTML, configuraciones de respaldo, entre otros.",
        "w)  para almacenar instrucciones operativas cruciales y un IOS limitado. .",
        "e) para almacenar aplicaciones, procesos y los datos necesarios para que la CPU los pueda ejecutar.",
        "r) se usa como almacenamiento permanente para el archivo de configuración de inicio (startup-config)."
    ], "w"),
    ("¿Para que usa la memoria NVRAM un router CISCO?", [
        "q)  se usa como almacenamiento permanente del IOS y otros archivos relacionados con el sistema, como archivos de registro, archivos de configuración de voz, archivos HTML, configuraciones de respaldo, entre otros.",
        "w)  para almacenar instrucciones operativas cruciales y un IOS limitado. .",
        "e) para almacenar aplicaciones, procesos y los datos necesarios para que la CPU los pueda ejecutar.",
        "r) se usa como almacenamiento permanente para el archivo de configuración de inicio (startup-config)."
    ], "r"),
    ("¿Para que usa la memoria Flash un router CISCO?", [
        "q)  se usa como almacenamiento permanente del IOS y otros archivos relacionados con el sistema, como archivos de registro, archivos de configuración de voz, archivos HTML, configuraciones de respaldo, entre otros.",
        "w)  para almacenar instrucciones operativas cruciales y un IOS limitado. .",
        "e) para almacenar aplicaciones, procesos y los datos necesarios para que la CPU los pueda ejecutar.",
        "r) se usa como almacenamiento permanente para el archivo de configuración de inicio (startup-config)."
    ], "q"),
    ("Todas las plataformas de router tienen componentes y configuraciones predeterminadas. Por ejemplo, el router Cisco de la serie 1941 viene con 512 MB de memoria SDRAM, pero se la puedeexpandir hasta 2 GB", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
    (" El router Cisco 1941 viene con ... de memoria flash, pero se puede expandir con ... ranuras para tarjeta de memoria externa CompactFlash. Cada ranura puede admitir tarjetas de memoria de alta velocidad de hasta ... GB.", [
        "q) 256MB/Dos/4.",
        "w) 256MB/Cuatro/8.",
        "e) 64MB/Dos/4.",
        "r) 256MB/Tres/6."
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
