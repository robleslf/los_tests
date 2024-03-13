import random


preguntas = [
    ("¿Qué cargan los switches y routers Cisco al iniciarse, y dónde?", [
        "q) La imagen IOS y el archivo de configuración de incicio, en la RAM.",
        "w) La imagen IOS, el archivo de configuración de incicio y la tabla de enrutamiento, en la RAM.",
        "e) La imagen IOS y el archivo de configuración de incicio, en la ROM.",
        "r) La imagen IOS, el archivo de configuración de incicio y la tabla de enrutamiento, en la ROM."
    ], "q"),
        ("¿Cuándo se modifica la configuración en ejecución del router?", [
        "q) Cuando el router detecta problemas en la configuración.",
        "w) Cuando el administrador de redes realiza configuraciones de dispositivo.",
        "e) Automáticamente cada 24 horas.",
        "r) Nunca."
    ], "w"),
        ("Los cambios que se hayan realizado en el archivo running-config se deben guardar en el archivo de configuración en la NVRAM, en caso de que se reinicie el router o este no reciba energía.", [
        "q) Verdadero.",
        "r) Falso."
    ], "q"),
        ("No es necesario guardar los cambios que se hayan realizado en el archivo running-configen el archivo de configuración en la NVRAM..", [
        "q) Verdadero.",
        "r) Falso."
    ], "r"),
        ("¿Cuál es la primera fase del proceso de arranque de un router?", [
        "q) Se carga la tabla de enrutamiento.",
        "w) Se ubica y se carga el software Cisco IOS.",
        "e) Se realiza el POST y se carga el programa de arranque.",
        "r) Se ubica y se carga el archivo de configuración de inicio o se ingresa al modo de configuración."
    ], "e"),
        ("¿Cuál es la segunda fase del proceso de arranque de un router?", [
        "q) Se carga la tabla de enrutamiento.",
        "w) Se ubica y se carga el software Cisco IOS.",
        "e) Se realiza el POST y se carga el programa de arranque.",
        "r) Se ubica y se carga el archivo de configuración de inicio o se ingresa al modo de configuración."
    ], "w"),
        ("¿Cuál es la tercera y última fase del proceso de arranque de un router?", [
        "q) Se carga la tabla de enrutamiento.",
        "w) Se ubica y se carga el software Cisco IOS.",
        "e) Se realiza el POST y se carga el programa de arranque.",
        "r) Se ubica y se carga el archivo de configuración de inicio o se ingresa al modo de configuración."
    ], "r"),
        ("¿Qué hace el router durante el autodiagnóstico al encender (POST)?", [
        "q) Realiza diagnósticos en la ROM sobre varios componentes de hardware, incluidas la CPU, la RAM y la NVRAM.",
        "w) Realiza diagnósticos en la RAM sobre varios componentes de hardware, incluidas la CPU, la ROM y la NVRAM.",
        "e) Realiza diagnósticos en la CPU sobre varios componentes de hardware, incluidas la RAM, la ROM y la NVRAM.",
        "r) Realiza diagnósticos en la NVRAM sobre varios componentes de hardware, incluidas la RAM, la ROM y la CPU."
    ], "q"),
        ("¿Qué pasa después del POST?", [
        "q) El programa de arranque se copia de la RAM a la ROM.",
        "w) El programa de arranque se copia de la ROM a la RAM.",
        "e) El programa de arranque se borra de la RAM.",
        "r) El programa de arranque se borra de la ROM."
    ], "w"),
        ("¿Cuál es la tarea principal del programa de arranque del router?", [
        "q) Apagar otra vez el router.",
        "w) Ejecutar la conexión con las demás interfaces de red.",
        "e) Ejecutar los comandos necesarios antes de entrar en CLI.",
        "r) Ubicar al Cisco IOS y cargarlo en la RAM."
    ], "r"),
        ("¿Dónde se almacena generalmente el IOS del router?", [
        "q) En la memoria flash.",
        "w) En la memoria ROM.",
        "e) En la memoria RAM.",
        "r) En la memoria USB."
    ], "q"),
        ("Elije la opción correcta", [
        "q) Por lo general, el IOS se almacena en la memoria ROM y se copia en la flash para que lo ejecute la CPU.",
        "w) Por lo general, el IOS se almacena en la memoria ROM y se copia en la RAM para que lo ejecute la CPU.",
        "e) Por lo general, el IOS se almacena en la memoria flash y se copia en la RAM para que lo ejecute la CPU.",
        "r) Por lo general, el IOS se almacena en la memoria RAM y se copia en la ROM para que lo ejecute la CPU."
    ], "e"),
        ("¿Qué pasa si la imagen de IOS no está en la memoria flash durante la fase de ubicación y carga de Cisco IOS?", [
        "q) El router puede buscarla en las memorias ROM y RAM.",
        "w) El router puede buscarla en la memoria RAM.",
        "e) El router puede buscarla en la memoria ROM.",
        "r) El router puede buscarla con un servidor de protocolo trivial de transferencia de archivos (TFTP)."
    ], "r"),
        ("¿Qué sucede si no se puede ubicar una imagen de IOS completa durante la ubicación y carga de Cisco IOS?", [
        "q) Se copia un IOS limitado en la RAM, que puede usarse para diagnosticar problemas y transferir un IOS completo a la memoria flash.",
        "w) No se puede arrancar el router y se apaga.",
        "e) El router permance en espera hasta que el administrador de redes facilite una imagen completa.",
        "r) Explota."
    ], ""),
        ("¿Dónde copia el programa de arranque el archivo de configuración de inicio?", [
        "q) De la NVRAM a la RAM.",
        "w) De la RAM a la NVRAM.",
        "e) De la ROM a la RAM.",
        "r) De la ROM a la NVRAM."
    ], "q"),
        ("¿Qué pasa si el archivo de configuración de inicio no existe en la NVRAM?", [
        "q) Nada, ya que el archivo de configuración no debe estar en la NVRAM, sino en la ROM.",
        "w) No se puede iniciar el router.",
        "e) Se puede configurar al router para que busque un servidor TFTP.",
        "r) Se puede buscar en la ROM."
    ], "e"),
        ("Si el archivo de configuración de inicio no existe en la NVRAM, se puede configurar al router para que busque un servidor TFTP. Si no encuentra ningún servidor TFTP,...", [
        "q) ...el router muestra la petición de entrada del modo de configuración.",
        "w) ...el router se apaga.",
        "e) ...buscará un servidor HTTP.",
        "r) ...el router se reinicia."
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
